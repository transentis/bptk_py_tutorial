
#      _                   _ _
#  _____| |__ ___ _ __  _ __(_| |___ _ _
# (_-/ _` / _/ _ | '  \| '_ | | / -_| '_|
# /__\__,_\__\___|_|_|_| .__|_|_\___|_|
#                      |_|
# Copyright (c) 2013-2020 transentis management & consulting. All rights reserved.
#
    
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import gammaln
from scipy.stats import norm
import math, statistics, random, logging
from datetime import datetime
import re
import itertools
from copy import copy, deepcopy



def cartesian_product(listoflists):
    """
    Helper for Cartesian product
    :param listoflists:
    :return:
    """
    if len(listoflists) == 1:
        return listoflists[0]
    res = list(itertools.product(*listoflists))

    if len(res) == 1:
        return res[0]

    return res

def LERP(x,points):
    """
    Linear interpolation between a set of points
    :param x: x to obtain y for
    :param points: List of tuples containing the graphical function's points [(x,y),(x,y) ... ]
    :return: y value for x obtained using linear interpolation
    """
    x_vals = np.array([ x[0] for x in points])
    y_vals = np.array([x[1] for x in points])

    if x<= x_vals[0]:
        return y_vals[0]

    if x >= x_vals[len(x_vals)-1]:
        return y_vals[len(x_vals)-1]

    f = interp1d(x_vals, y_vals)
    return float(f(x))

class simulation_model():
    def __init__(self):
        # Simulation Settings
        self.dt = 1
        self.starttime = 1.0
        self.stoptime = 24.0
        self.units = 'Months'
        self.method = 'Euler'
        self.equations = {

        # Stocks
        
    
        'cash.cash'          : lambda t: ( (1000.0) if ( t  <=  self.starttime ) else (self.memoize('cash.cash',t-self.dt) + self.dt * ( self.memoize('cash.cashIn',t-self.dt) - ( self.memoize('cash.cashOut',t-self.dt) ) )) ),
        'cost.professionalStaff'          : lambda t: ( (0) if ( t  <=  self.starttime ) else (self.memoize('cost.professionalStaff',t-self.dt) + self.dt * 0) ),
        'kpi.professionalStaff'          : lambda t: ( (0) if ( t  <=  self.starttime ) else (self.memoize('kpi.professionalStaff',t-self.dt) + self.dt * 0) ),
        'kpi.projects'          : lambda t: ( (0) if ( t  <=  self.starttime ) else (self.memoize('kpi.projects',t-self.dt) + self.dt * 0) ),
        'projects.projects'          : lambda t: ( (320.0) if ( t  <=  self.starttime ) else (self.memoize('projects.projects',t-self.dt) + self.dt * ( self.memoize('projects.winningProjects',t-self.dt) - ( self.memoize('projects.deliveringProjects',t-self.dt) ) )) ),
        'projects.proposals'          : lambda t: ( (320.0) if ( t  <=  self.starttime ) else (self.memoize('projects.proposals',t-self.dt) + self.dt * ( self.memoize('projects.prospectingProjects',t-self.dt) - ( self.memoize('projects.winningProjects',t-self.dt) ) )) ),
        'revenue.receivables'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('revenue.receivables',t-self.dt) + self.dt * ( self.memoize('revenue.makingRevenue',t-self.dt) - ( self.memoize('revenue.collectingRevenue',t-self.dt) ) )) ),
        'staff.professionalStaff'          : lambda t: ( (200.0) if ( t  <=  self.starttime ) else (self.memoize('staff.professionalStaff',t-self.dt) + self.dt * ( self.memoize('staff.staffArriving',t-self.dt) )) ),
        'staff.staffInRecruitment'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('staff.staffInRecruitment',t-self.dt) + self.dt * ( self.memoize('staff.hiringStaff',t-self.dt) - ( self.memoize('staff.staffArriving',t-self.dt) ) )) ),
        
    
        # Flows
        'cash.cashIn'             : lambda t: max([0 , self.memoize('revenue.collectingRevenue', t)]),
        'cash.cashOut'             : lambda t: max([0 , self.memoize('cost.cost', t)]),
        'projects.deliveringProjects'             : lambda t: max([0 , min([self.memoize('projects.projectDeliveryRate', t) , self.memoize('projects.projects', t)])]),
        'projects.prospectingProjects'             : lambda t: max([0 , self.memoize('projects.projectProposalRate', t)]),
        'projects.winningProjects'             : lambda t: max([0 , min([self.delay( self.memoize('projects.prospectingProjects', ( t - (self.memoize('projects.projectAcquisitionDuration', t)) )),self.memoize('projects.projectAcquisitionDuration', t),160.0,t) , self.memoize('projects.proposals', t)])]),
        'revenue.collectingRevenue'             : lambda t: max([0 , self.delay( self.memoize('revenue.makingRevenue', ( t - (self.memoize('revenue.collectionTime', t)) )),self.memoize('revenue.collectionTime', t),2816.0,t)]),
        'revenue.makingRevenue'             : lambda t: max([0 , self.memoize('revenue.revenue', t)]),
        'staff.hiringStaff'             : lambda t: max([0 , ( 1.0 - self.memoize('kpi.steadyGrowthPolicyOn', t) ) * self.memoize('staff.hiringRate', t) + self.memoize('kpi.steadyGrowthPolicyOn', t) * self.memoize('staff.professionalStaff', t) * self.memoize('staff.steadyGrowthRate%', t) / 100.0]),
        'staff.staffArriving'             : lambda t: max([0 , self.delay( self.memoize('staff.hiringStaff', ( t - (self.memoize('staff.hiringDuration', t)) )),self.memoize('staff.hiringDuration', t),0.0,t)]),
        
    
        # converters
        'cash.cashFlow'      : lambda t: self.memoize('cash.cashIn', t) - self.memoize('cash.cashOut', t),
        'cash.collectingRevenue'      : lambda t: 0.0,
        'cash.cost'      : lambda t: 0.0,
        'cash.easyTargetCash'      : lambda t: 30000.0,
        'cash.expertTargetCash'      : lambda t: 40000.0,
        'cash.minimumCash'      : lambda t: 23463.0,
        'cost.cost'      : lambda t: self.memoize('cost.overheadCost', t) + self.memoize('cost.staffCost', t),
        'cost.overheadCost'      : lambda t: 306.0,
        'cost.staffCost'      : lambda t: ( self.memoize('cost.workplaceCost', t) + self.memoize('cost.staffSalary', t) ) * self.memoize('staff.professionalStaff', t),
        'cost.staffSalary'      : lambda t: 80.0 / 12.0,
        'cost.workplaceCost'      : lambda t: 1.0,
        'kpi.acquisitionToDeliveryRatio%'      : lambda t: 100.0 * self.memoize('projects.prospectingEffort', t) / ( self.memoize('projects.prospectingEffort', t) + self.memoize('projects.projectVolume', t) ),
        'kpi.cashFlow'      : lambda t: 0.0,
        'kpi.cashFlowPerProfessional'      : lambda t: self.memoize('cash.cashFlow', t) / self.memoize('staff.professionalStaff', t),
        'kpi.deliveringProjects'      : lambda t: 0.0,
        'kpi.maxiumProjectCapacity'      : lambda t: ( 1.0 - self.memoize('kpi.acquisitionToDeliveryRatio%', t) / 100.0 ) * self.memoize('staff.professionalStaff', t),
        'kpi.minimumBusDevAllocationOn'      : lambda t: 0.0,
        'kpi.projectBacklog'      : lambda t: self.memoize('projects.projects', t) / self.memoize('kpi.maxiumProjectCapacity', t),
        'kpi.projectVolume'      : lambda t: 0.0,
        'kpi.prospectingEffort'      : lambda t: 0.0,
        'kpi.steadyGrowthPolicyOn'      : lambda t: 0.0,
        'kpi.targetBacklog'      : lambda t: 2.0,
        'kpi.targetBusinessDevelopmentAllocation%'      : lambda t: ( 1.0 - self.memoize('kpi.minimumBusDevAllocationOn', t) ) * 100.0 * max([( 1.0 - self.memoize('kpi.targetProjectStaff', t) / self.memoize('staff.professionalStaff', t) ) , 0.0]) + self.memoize('kpi.minimumBusDevAllocationOn', t) * max([100.0 * ( 1.0 - self.memoize('kpi.targetProjectStaff', t) / self.memoize('staff.professionalStaff', t) ) , self.memoize('kpi.acquisitionToDeliveryRatio%', t)]),
        'kpi.targetProjctDeliveryCapacity'      : lambda t: self.memoize('projects.projects', t) / self.memoize('kpi.targetBacklog', t),
        'kpi.targetProjectStaff'      : lambda t: self.memoize('kpi.targetProjctDeliveryCapacity', t),
        'kpi.utilization%'      : lambda t: 100.0 * self.memoize('projects.deliveringProjects', t) / self.memoize('kpi.maxiumProjectCapacity', t),
        'projects.businessDevelopmentCapacity'      : lambda t: 0.0,
        'projects.projectAcquisitionDuration'      : lambda t: 6.0,
        'projects.projectDeliveryCapacity'      : lambda t: 0.0,
        'projects.projectDeliveryRate'      : lambda t: self.memoize('staff.projectDeliveryCapacity', t),
        'projects.projectProposalRate'      : lambda t: self.memoize('projects.projectVolume', t) * ( self.memoize('staff.businessDevelopmentCapacity', t) / self.memoize('projects.prospectingEffort', t) ),
        'projects.projectVolume'      : lambda t: 16.0,
        'projects.prospectingEffort'      : lambda t: 4.0,
        'revenue.collectionTime'      : lambda t: 2.0,
        'revenue.deliveringProjects'      : lambda t: 0.0,
        'revenue.projectDeliveryFee'      : lambda t: 17.6,
        'revenue.revenue'      : lambda t: self.memoize('revenue.projectDeliveryFee', t) * self.memoize('projects.deliveringProjects', t),
        'staff.actualBusinessDevelopmentAllocation%'      : lambda t: self.memoize('kpi.steadyGrowthPolicyOn', t) * self.memoize('kpi.targetBusinessDevelopmentAllocation%', t) + ( 1.0 - self.memoize('kpi.steadyGrowthPolicyOn', t) ) * self.memoize('staff.businessDevelopmentAllocation%', t),
        'staff.businessDevelopmentCapacity'      : lambda t: self.memoize('staff.workCapacity', t) * self.memoize('staff.actualBusinessDevelopmentAllocation%', t) / 100.0,
        'staff.hiringDuration'      : lambda t: 3.0,
        'staff.projectDeliveryCapacity'      : lambda t: self.memoize('staff.workCapacity', t) * ( 100.0 - self.memoize('staff.actualBusinessDevelopmentAllocation%', t) ) / 100.0,
        'staff.steadyGrowthPolicyOn1'      : lambda t: 0.0,
        'staff.steadyGrowthRate%'      : lambda t: 1.0,
        'staff.targetBusinessDevStaff%'      : lambda t: 0.0,
        'staff.workCapacity'      : lambda t: self.memoize('staff.professionalStaff', t) * self.memoize('staff.workMonth', t),
        'staff.workMonth'      : lambda t: 1.0,
        
    
        # gf
        'staff.businessDevelopmentAllocation%' : lambda t: LERP(  t , self.points['staff.businessDevelopmentAllocation%']),
        'staff.hiringRate' : lambda t: LERP(  t , self.points['staff.hiringRate']),
        
    
        #constants
        'cash.collectingRevenue' : lambda t: 0.0,
        'cash.cost' : lambda t: 0.0,
        'kpi.cashFlow' : lambda t: 0.0,
        'kpi.deliveringProjects' : lambda t: 0.0,
        'kpi.projectVolume' : lambda t: 0.0,
        'kpi.prospectingEffort' : lambda t: 0.0,
        'projects.businessDevelopmentCapacity' : lambda t: 0.0,
        'projects.projectDeliveryCapacity' : lambda t: 0.0,
        'revenue.deliveringProjects' : lambda t: 0.0,
        'staff.targetBusinessDevStaff%' : lambda t: 0.0,
        
    
    
        }
    
        self.points = {
            'staff.businessDevelopmentAllocation%' :  [(1.0, 20.0), (2.0, 20.0), (3.0, 20.0), (4.0, 20.0), (5.0, 20.0), (6.0, 20.0), (7.0, 20.0), (8.0, 20.0), (9.0, 20.0), (10.0, 20.0), (11.0, 20.0), (12.0, 20.0), (13.0, 20.0), (14.0, 20.0), (15.0, 20.0), (16.0, 20.0), (17.0, 20.0), (18.0, 20.0), (19.0, 20.0), (20.0, 20.0), (21.0, 20.0), (22.0, 20.0), (23.0, 20.0), (24.0, 20.0)]  , 'staff.hiringRate' :  [(1.0, 0.0), (2.0, 0.0), (3.0, 0.0), (4.0, 0.0), (5.0, 0.0), (6.0, 0.0), (7.0, 0.0), (8.0, 0.0), (9.0, 0.0), (10.0, 0.0), (11.0, 0.0), (12.0, 0.0), (13.0, 0.0), (14.0, 0.0), (15.0, 0.0), (16.0, 0.0), (17.0, 0.0), (18.0, 0.0), (19.0, 0.0), (20.0, 0.0), (21.0, 0.0), (22.0, 0.0), (23.0, 0.0), (24.0, 0.0)]  , 
        }
    
    
        self.dimensions = {
        	'': {
                'labels': [  ],
                'variables': [  ],
            },
        }
                
        self.dimensions_order = {}     
    
        self.stocks = ['cash.cash',   'cost.professionalStaff',   'kpi.professionalStaff',   'kpi.projects',   'projects.projects',   'projects.proposals',   'revenue.receivables',   'staff.professionalStaff',   'staff.staffInRecruitment'  ]
        self.flows = ['cash.cashIn',   'cash.cashOut',   'projects.deliveringProjects',   'projects.prospectingProjects',   'projects.winningProjects',   'revenue.collectingRevenue',   'revenue.makingRevenue',   'staff.hiringStaff',   'staff.staffArriving'  ]
        self.converters = ['cash.cashFlow',   'cash.collectingRevenue',   'cash.cost',   'cash.easyTargetCash',   'cash.expertTargetCash',   'cash.minimumCash',   'cost.cost',   'cost.overheadCost',   'cost.staffCost',   'cost.staffSalary',   'cost.workplaceCost',   'kpi.acquisitionToDeliveryRatio%',   'kpi.cashFlow',   'kpi.cashFlowPerProfessional',   'kpi.deliveringProjects',   'kpi.maxiumProjectCapacity',   'kpi.minimumBusDevAllocationOn',   'kpi.projectBacklog',   'kpi.projectVolume',   'kpi.prospectingEffort',   'kpi.steadyGrowthPolicyOn',   'kpi.targetBacklog',   'kpi.targetBusinessDevelopmentAllocation%',   'kpi.targetProjctDeliveryCapacity',   'kpi.targetProjectStaff',   'kpi.utilization%',   'projects.businessDevelopmentCapacity',   'projects.projectAcquisitionDuration',   'projects.projectDeliveryCapacity',   'projects.projectDeliveryRate',   'projects.projectProposalRate',   'projects.projectVolume',   'projects.prospectingEffort',   'revenue.collectionTime',   'revenue.deliveringProjects',   'revenue.projectDeliveryFee',   'revenue.revenue',   'staff.actualBusinessDevelopmentAllocation%',   'staff.businessDevelopmentCapacity',   'staff.hiringDuration',   'staff.projectDeliveryCapacity',   'staff.steadyGrowthPolicyOn1',   'staff.steadyGrowthRate%',   'staff.targetBusinessDevStaff%',   'staff.workCapacity',   'staff.workMonth'  ]
        self.gf = ['staff.businessDevelopmentAllocation%',   'staff.hiringRate'  ]
        self.constants= ['cash.collectingRevenue',   'cash.cost',   'kpi.cashFlow',   'kpi.deliveringProjects',   'kpi.projectVolume',   'kpi.prospectingEffort',   'projects.businessDevelopmentCapacity',   'projects.projectDeliveryCapacity',   'revenue.deliveringProjects',   'staff.targetBusinessDevStaff%'  ]
        self.events = [
            ]
    
        self.memo = {}
        for key in list(self.equations.keys()):
          self.memo[key] = {}  # DICT OF DICTS!
          
    
    """
    Builtin helpers
    """
    def ramp(self,slope,start,t):
        if not start:
            start = self.starttime
        if t <= start: return 0
        return (t-start)*slope
        
    def rootn(self,expression,order):
        order = round(order,0)
        if expression < 0 and order % 2 == 0: # Stella does not allow even roots for negative numbers as no complex numbers are supported
            return np.nan
        return -abs(expression)**(1/round(order,0)) if expression < 0 else abs(expression)**(1/round(order,0)) # Stella Logic! No Complex numbers for negative numbers. Hence take the nth root of the absolute value and then add the negativity (if any)
    
    """
    Statistical builtins with Seed
    """
    def pareto_with_seed(self, shape, scale, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.pareto(shape) * scale  
    
    def weibull_with_seed(self, shape, scale, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.weibull(shape) * scale      
    
    def poisson_with_seed(self, mu, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.poisson(mu)   
    
    def negbinomial_with_seed(self, successes, p, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.negative_binomial(successes, p)  
    
    def lognormal_with_seed(self, mean, stdev, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.lognormal(mean, stdev)   
    
    def logistic_with_seed(self, mean, scale, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.logistic(mean, scale)
    
    def random_with_seed(self, seed, t ):
        if t == self.starttime:
            random.seed(int(seed))
        return random.random()

    def beta_with_seed(self, a,b,seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.beta(a,b)
        
    def binomial_with_seed(self, n,p,seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.binomial(n,p)
        
    def gamma_with_seed(self, shape,scale,seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.gamma(shape,scale)
        
    def exprnd_with_seed(self, plambda,seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.exponential(plambda)
        
    def geometric_with_seed(self, p, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.geometric(p)
    
    def triangular_with_seed(self, left, mode, right, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.triangular(left, mode, right)
    
    def rank(self, lis, rank):
        rank = int(rank)
        sorted_list = np.sort(lis)
        try:
            rankth_elem = sorted_list[rank-1]
        except IndexError as e:
            logging.error("RANK: Rank {} too high for array of size {}".format(rank,len(lis)))
        return (lis==rankth_elem).nonzero()[0][0]+1
        

    def interpolate(self, variable, t, *args):
        """
        Helper for builtin "interpolate". Uses the arrayed variable and args to compute the interpolation
        :param variable:
        :param t:
        :param args: Interpolation weight for each dimension, between one or zero
        :return:
        """
        def compute_x(values): #
            """
            Compute x values for interpolation. Always from 0 to 1. E.g. values = [1,2,3], then x = [0, 0.5, 1.0]
            :param values:
            :return:
            """
            #
            x = [0]
            for i in range(1, len(values)): x += [x[i - 1] + 1 / (len(values) - 1)]
            return x

        def interpolate_values(index, y_val):  # Internal interpolate of a dimension's results
            x_val = compute_x(y_val)
            points = [(x_val[i], y_val[i]) for i in range(0, len(x_val))]
            return LERP(index, points)

        # Fix each weight to a value between 0 and 1
        args = [max(0,min(x,1)) for x in args]

        # Get dimensions of variable (2,3,4 ...)
        dimensions = self.dimensions_order[variable]

        # Get Labels
        labels = {key: dim["labels"] for key, dim in
                  dict(filter(lambda elem: elem[0] in dimensions, self.dimensions.items())).items()}

        # Compute
        results = {}
        if len(labels.keys()) == 1:
            return interpolate_values(args[0], self.equation(variable + "[*]", t))
        for index, dimension in enumerate(dimensions):
            results[dimension] = []
            for label in labels[dimension]:
                indices = ["*" if i != index else label for i in
                           range(0, len(dimensions))]  # Build indices, such as "*,element1" or "1,*"

                results[dimension] += [
                    interpolate_values(args[index], self.equation(variable + "[{}]".format(",".join(indices)), t))]

        return [interpolate_values(args[i], v) for i, v in enumerate(results.values())][0]

    def lookupinv(self,gf, value):
        """
        Helper for lookupinv builtin. Looks for the corresponding x of a given y
        :param gf: Name of graphical function
        :param value: Value we are looking for (y)
        :return:
        """
        def lerpfun(x, points):  # Special lerp function for the reversed points
            from scipy.interpolate import interp1d
            x_vals = np.array([x[0] for x in points])
            y_vals = np.array([x[1] for x in points])
            f = interp1d(x_vals, y_vals)
            return f(x)

        results = []
        for t in np.arange(self.starttime, self.stoptime + self.dt,
                           self.dt):  # Compute all y values for graphical functions using standard interpolate (LERP)
            results += [(LERP(t, self.points[gf]), t)] # y,x

        return np.round(lerpfun(value, results),
                     3)  # Use LERP function for the reversed set of points (y,x) and find the correct value. Cannot use standard LERP here because that would require continuous X (1,2,3..)

    def delay(self, tdelayed, offset, initial, t):
        '''
        Delay builtin
        :param tdelayed: Delayed T
        :param offset: Offset
        :param initial: Initial value
        :param t:
        :return:
        '''
        if (t - self.starttime) < offset: return initial
        else: return tdelayed

    def counter(self,start, interval, t):
        '''
        Counter bultin
        :param start:
        :param interval:
        :param t:
        :return:
        '''
        num_elems = (interval / start / self.dt)
        value = interval / num_elems
        t_copy = copy(t)

        while t >= interval: t = t - interval
        if (t_copy > interval): return (start + (t / self.dt) * value)

        return (t / self.dt * value)

    def npv(self, initial, p, t):
        """
        NPV (Net Present Value) builtin
        :param initial:
        :param p:
        :param t:
        :return:
        """
        rate = 1.0 / (1.0 + p) ** (t - self.dt - self.starttime + self.dt)
        return initial if (t <= self.starttime) else ( self.npv(initial, p, t - self.dt) + (self.dt * rate * initial) )# Recurse

    def irr(self, stock_name, missing, t,myname):
        """
        Approximate IRR (Internal Rate of Return)
        :param stock_name: Identifier of Stock to approximate for
        :param missing: Replace missing values with this value
        :param t:
        :return:
        """

        def compute_npv(stock_name, t, i, missing):
            I = missing if missing else self.equation(stock_name, self.starttime)
            return I + sum( [self.memoize(stock_name, t) / (1 + i) ** t for t in np.arange(self.starttime+self.dt , t, self.dt)])

        i = 0
        try:
            i = 0 if t <= self.starttime + self.dt else self.memo[myname][t-self.dt]
        except:
            pass

        if t == self.starttime: return None

        best_kw = {i : compute_npv(stock_name, t, i, missing)}
        for _ in range(0, 300):
            # Here we approximate the IRR
            kw = compute_npv(stock_name, t, i, missing)

            change = 0.001

            best_kw[i] = kw

            if abs(kw) < self.memoize(stock_name, t)*0.1: change = 0.0001

            if abs(kw) < self.memoize(stock_name, t)*0.05: change = 0.00001

            if abs(kw) < self.memoize(stock_name, t)*0.02: change = 0.000001

            if kw < 0: i -= change
            elif kw > 0:  i += change

            if kw == 0: return i
        best_kw = {k: v for k, v in sorted(best_kw.items(), key=lambda item: item[1])}
        x = {v: k for k, v in sorted(best_kw.items(), key=lambda item: item[1])} # Sort by best npv
        return x[min(x.keys())]

    def normalcdf(self,left, right, mean, sigma):
        import scipy.stats
        right = scipy.stats.norm(float(mean), float(sigma)).cdf(float(right))
        left = scipy.stats.norm(float(mean), float(sigma)).cdf(float(left))
        return round(right - left, 3)

    def cgrowth(self, p):
        from sympy.core.numbers import Float
        import sympy as sy
        z = sy.symbols('z', real=True) # We want to find z
        dt = self.dt

        x = (1 + dt * (1 * z))

        for i in range(1, int(1 / dt)): x = (x + dt * (x * z))

        # Definition of the equation to be solved
        eq = sy.Eq(1 + p, x)

        # Solve the equation
        results = [x for x in (sy.solve(eq)) if type(x) is Float and x > 0] # Quadratic problem, hence usually a positive, negative and 2 complex solutions. We only require the positive one
        return float(results[0])

    def montecarlo(self,probability,seed, t):
        """
        Montecarlo builtin
        :param probability:
        :param seed:
        :param t:
        :return:
        """
        if seed and t==self.starttime:
            random.seed(seed)
        rndnumber = random.uniform(0,100)
        return 1 if rndnumber < (probability*self.dt) else 0


    def derivn(self, equation, order, t):
        """
        nth derivative of an equation
        :param equation: Name of the equation
        :param order: n
        :param t: current t
        :return:
        """
        memo = {}
        dt = 0.25

        def mem(eq, t):
            """
            Memo for internal equations
            :param eq:
            :param t:
            :return:
            """
            if not eq in memo.keys(): memo[eq] = {}
            mymemo = memo[eq]
            if t in mymemo.keys(): return mymemo[t]
            else:
                mymemo[t] = s[eq](t)
                return mymemo[t]

        s = {}
        s[1] = lambda t: 0 if t <= self.starttime else (self.memoize(equation, t) - self.memoize(equation, t - dt)) / dt

        def addEquation(n):
            s[n] = lambda t: 0 if t <= self.starttime else (mem(n - 1, t) - mem(n - 1, t - dt)) / dt

        for n in list(range(2, order + 1)): addEquation(n)

        return s[order](t) if ( t >= self.starttime + (dt * order) ) else 0

    def smthn(self, inputstream, averaging_time, initial, n, t):
        """
        Pretty complex operator. Actually we are building a whole model here and have it run
        Find info in https://www.iseesystems.com/resources/help/v1-9/default.htm#08-Reference/07-Builtins/Delay_builtins.htm#kanchor364
        :param inputstream:
        :param averaging_time:
        :param initial:
        :param n:
        :param t:
        :return:
        """
        memo = {}
        dt = self.dt
        from copy import deepcopy

        def mem(eq, t):
            """
            Internal memo for equations
            :param eq:
            :param t:
            :return:
            """
            if not eq in memo.keys(): memo[eq] = {}
            mymemo = memo[eq]
            if t in mymemo.keys():return mymemo[t]
            else:
                mymemo[t] = s[eq](t)
                return mymemo[t]

        s = {}

        def addEquation(n, upper):
            y = deepcopy(n)
            if y == 1:
                s["stock1"] = lambda t: (
                    (max([0, (self.memoize(inputstream, t) if (initial is None) else initial)])) if (
                                t <= self.starttime) else (
                                mem('stock1', t - dt) + dt * (mem('changeInStock1', t - dt))))
                s['changeInStock1'] = lambda t: (self.memoize(inputstream, t) - mem('stock1', t)) / (
                            averaging_time / upper)
            if y > 1:
                s["stock{}".format(y)] = lambda t: (
                    (max([0, (self.memoize(inputstream, t) if (initial is None) else initial)])) if (t <= self.starttime) else (
                                mem("stock{}".format(y), t - dt) + dt * (mem('changeInStock{}'.format(y), t - dt))))
                s['changeInStock{}'.format(y)] = lambda t: (mem("stock{}".format(y - 1), t) - mem("stock{}".format(y),
                                                                                                  t)) / (averaging_time / upper)
        n = int(n)

        for i in list(range(0, n + 1)): addEquation(i, n)

        return s['stock{}'.format(n)](t)

    def forcst(self,inputstream, averaging_time, horizon, initial, t):
        memo = {"change_in_input": {}, "average_input": {}, "trend_in_input": {}, "forecast_input": {}}

        def mem(eq, t):
            """
            Internal memo for equations
            :param eq:
            :param t:
            :return:
            """
            mymemo = memo[eq]
            if t in mymemo.keys(): return mymemo[t]
            else:
                mymemo[t] = s[eq](t)
                return mymemo[t]

        s = {
            "change_in_input": lambda t: max([0, (self.memoize(inputstream,t) - mem('average_input', t)) / averaging_time]),
            "average_input": lambda t: ((self.memoize(inputstream,t)) if (t <= self.starttime) else (
                        mem("average_input", t - self.dt) + self.dt * (mem("change_in_input", t - self.dt)))),
            "trend_in_input": lambda t: (((self.memoize(inputstream,t) - self.memoize('averageInput', t)) / (
                        self.memoize('averageInput', t) * self.memoize('averagingTime', t))) if (
                        self.memoize('averageInput', t) > 0.0) else (np.nan)),
            "forecast_input": lambda t: self.memoize(inputstream,t) * (1.0 + mem("trend_in_input", t) * horizon)
        }

        return s["forecast_input"](t)

    #Helpers for Dimensions (Arrays)

    def find_dimensions(self, stock):
        stockdimensions = {}
        for dimension, values in self.dimensions.items():
            if stock in values["variables"]:
                stockdimensions[dimension] = values["labels"]

        if len(stockdimensions.keys()) == 1:
            return [stock + "[{}]".format(x) for x in stockdimensions[list(stockdimensions.keys())[0]]]

    def get_dimensions(self, equation, t):
        re_find_indices = r'\[([^)]+)\]'
        group = re.search(re_find_indices, equation).group(0).replace("[", "").replace("]", "")
        equation_basic = equation.replace(group, "").replace("[]", "")
        labels = []
        for index, elem in enumerate(group.split(",")):
            if len(elem.split(":")) > 1: # List operator
                try:
                    bounds = [int(x) for x in elem.split(":")]
                except ValueError as e:
                    logging.error(e)
                    continue
                bounds = sorted(bounds)
                if len(bounds) > 2:
                    logging.error("Too many arguments for list operator. Expecting 2, got {}".format(len(bounds)))

                labels += [list(range(bounds[0], bounds[1]+1))]

            elif elem == "*": # Star operator
                dim = self.dimensions_order[equation_basic][index]
                labels += [self.dimensions[dim]["labels"]]
            else:
                if not type(elem) is list:
                    labels += [[elem]]
                else:
                    labels += [elem]

        products = cartesian_product(labels)

        return_list = []

        for product in products:
            prod = str(product).replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            return_list += [self.memoize(equation_basic + "[{}]".format(prod), t)]
            
        return np.array(return_list)


    #Access equations API

    def equation(self, equation, arg):
        return self.memoize(equation,arg)


    #Memoizer for equations. Also does most of API work

    def memoize(self, equation, arg):
        if type(equation) is float or type(equation) is int: # Fallback for values
            return equation
        if "*" in equation or ":" in equation:
            return self.get_dimensions(equation,arg)
            
        if not equation in self.equations.keys():

            # match array pattern and find non-arrayed var
            import re
            match = re.findall(r'\[[a-zA-Z1-9,_]*\]', equation)

            if match:

                equation_replaced = equation.replace(match[0], "")

                if equation_replaced in self.equations:
                    return self.memoize(equation=equation_replaced,arg=arg)
            else:
                logging.error("Equation '{}' not found!".format(equation))

        mymemo = self.memo[equation]

        if arg in mymemo.keys():
            return mymemo[arg]
        else:
            result = self.equations[equation](arg)
            mymemo[arg] = result

        return result


    def setDT(self, v):
        self.dt = v

    def setStarttime(self, v):
        self.starttime = v

    def setStoptime(self, v):
        self.stoptime = v
    
    def specs(self):
        return self.starttime, self.stoptime, self.dt, 'Months', 'Euler'
    