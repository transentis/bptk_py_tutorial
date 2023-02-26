
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
        self.dt = 0.25
        self.starttime = 1.0
        self.stoptime = 13.0
        self.units = 'months'
        self.method = 'Euler'
        self.equations = {

        # Stocks
        
    
        'inventory'          : lambda t: self.memoize('inventory[1,germany]', t) + self.memoize('inventory[1,england]', t) + self.memoize('inventory[1,austria]', t) + self.memoize('inventory[1,greece]', t) + self.memoize('inventory[2,germany]', t) + self.memoize('inventory[2,england]', t) + self.memoize('inventory[2,austria]', t) + self.memoize('inventory[2,greece]', t) + self.memoize('inventory[3,germany]', t) + self.memoize('inventory[3,england]', t) + self.memoize('inventory[3,austria]', t) + self.memoize('inventory[3,greece]', t),
        'inventory[1,germany]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[1,germany]',t-self.dt) + self.dt * ( self.memoize('productionRate[1,germany]',t-self.dt) )) ),
        'inventory[1,england]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[1,england]',t-self.dt) + self.dt * ( self.memoize('productionRate[1,england]',t-self.dt) )) ),
        'inventory[1,austria]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[1,austria]',t-self.dt) + self.dt * ( self.memoize('productionRate[1,austria]',t-self.dt) )) ),
        'inventory[1,greece]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[1,greece]',t-self.dt) + self.dt * ( self.memoize('productionRate[1,greece]',t-self.dt) )) ),
        'inventory[2,germany]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[2,germany]',t-self.dt) + self.dt * ( self.memoize('productionRate[2,germany]',t-self.dt) )) ),
        'inventory[2,england]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[2,england]',t-self.dt) + self.dt * ( self.memoize('productionRate[2,england]',t-self.dt) )) ),
        'inventory[2,austria]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[2,austria]',t-self.dt) + self.dt * ( self.memoize('productionRate[2,austria]',t-self.dt) )) ),
        'inventory[2,greece]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[2,greece]',t-self.dt) + self.dt * ( self.memoize('productionRate[2,greece]',t-self.dt) )) ),
        'inventory[3,germany]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[3,germany]',t-self.dt) + self.dt * ( self.memoize('productionRate[3,germany]',t-self.dt) )) ),
        'inventory[3,england]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[3,england]',t-self.dt) + self.dt * ( self.memoize('productionRate[3,england]',t-self.dt) )) ),
        'inventory[3,austria]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[3,austria]',t-self.dt) + self.dt * ( self.memoize('productionRate[3,austria]',t-self.dt) )) ),
        'inventory[3,greece]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('inventory[3,greece]',t-self.dt) + self.dt * ( self.memoize('productionRate[3,greece]',t-self.dt) )) ),
        'production'          : lambda t: self.memoize('production[1,germany]', t) + self.memoize('production[1,england]', t) + self.memoize('production[1,austria]', t) + self.memoize('production[1,greece]', t) + self.memoize('production[2,germany]', t) + self.memoize('production[2,england]', t) + self.memoize('production[2,austria]', t) + self.memoize('production[2,greece]', t) + self.memoize('production[3,germany]', t) + self.memoize('production[3,england]', t) + self.memoize('production[3,austria]', t) + self.memoize('production[3,greece]', t),
        'production[1,germany]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[1,germany]',t-self.dt) + self.dt * ( self.memoize('productionStart[1,germany]',t-self.dt) - ( self.memoize('productionRate[1,germany]',t-self.dt) ) )) ),
        'production[1,england]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[1,england]',t-self.dt) + self.dt * ( self.memoize('productionStart[1,england]',t-self.dt) - ( self.memoize('productionRate[1,england]',t-self.dt) ) )) ),
        'production[1,austria]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[1,austria]',t-self.dt) + self.dt * ( self.memoize('productionStart[1,austria]',t-self.dt) - ( self.memoize('productionRate[1,austria]',t-self.dt) ) )) ),
        'production[1,greece]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[1,greece]',t-self.dt) + self.dt * ( self.memoize('productionStart[1,greece]',t-self.dt) - ( self.memoize('productionRate[1,greece]',t-self.dt) ) )) ),
        'production[2,germany]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[2,germany]',t-self.dt) + self.dt * ( self.memoize('productionStart[2,germany]',t-self.dt) - ( self.memoize('productionRate[2,germany]',t-self.dt) ) )) ),
        'production[2,england]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[2,england]',t-self.dt) + self.dt * ( self.memoize('productionStart[2,england]',t-self.dt) - ( self.memoize('productionRate[2,england]',t-self.dt) ) )) ),
        'production[2,austria]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[2,austria]',t-self.dt) + self.dt * ( self.memoize('productionStart[2,austria]',t-self.dt) - ( self.memoize('productionRate[2,austria]',t-self.dt) ) )) ),
        'production[2,greece]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[2,greece]',t-self.dt) + self.dt * ( self.memoize('productionStart[2,greece]',t-self.dt) - ( self.memoize('productionRate[2,greece]',t-self.dt) ) )) ),
        'production[3,germany]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[3,germany]',t-self.dt) + self.dt * ( self.memoize('productionStart[3,germany]',t-self.dt) - ( self.memoize('productionRate[3,germany]',t-self.dt) ) )) ),
        'production[3,england]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[3,england]',t-self.dt) + self.dt * ( self.memoize('productionStart[3,england]',t-self.dt) - ( self.memoize('productionRate[3,england]',t-self.dt) ) )) ),
        'production[3,austria]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[3,austria]',t-self.dt) + self.dt * ( self.memoize('productionStart[3,austria]',t-self.dt) - ( self.memoize('productionRate[3,austria]',t-self.dt) ) )) ),
        'production[3,greece]'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('production[3,greece]',t-self.dt) + self.dt * ( self.memoize('productionStart[3,greece]',t-self.dt) - ( self.memoize('productionRate[3,greece]',t-self.dt) ) )) ),
        
    
        # Flows
        'productionRate'             : lambda t: self.memoize('productionRate[1,germany]', t) + self.memoize('productionRate[1,england]', t) + self.memoize('productionRate[1,austria]', t) + self.memoize('productionRate[1,greece]', t) + self.memoize('productionRate[2,germany]', t) + self.memoize('productionRate[2,england]', t) + self.memoize('productionRate[2,austria]', t) + self.memoize('productionRate[2,greece]', t) + self.memoize('productionRate[3,germany]', t) + self.memoize('productionRate[3,england]', t) + self.memoize('productionRate[3,austria]', t) + self.memoize('productionRate[3,greece]', t),
        'productionRate[1,germany]'             : lambda t: self.delay( self.memoize('productionStart[1,germany]', ( t - (self.memoize('productionDuration[1,germany]', t)) )),self.memoize('productionDuration[1,germany]', t),0.0,t),
        'productionRate[1,england]'             : lambda t: self.delay( self.memoize('productionStart[1,england]', ( t - (self.memoize('productionDuration[1,england]', t)) )),self.memoize('productionDuration[1,england]', t),0.0,t),
        'productionRate[1,austria]'             : lambda t: self.delay( self.memoize('productionStart[1,austria]', ( t - (self.memoize('productionDuration[1,austria]', t)) )),self.memoize('productionDuration[1,austria]', t),0.0,t),
        'productionRate[1,greece]'             : lambda t: self.delay( self.memoize('productionStart[1,greece]', ( t - (self.memoize('productionDuration[1,greece]', t)) )),self.memoize('productionDuration[1,greece]', t),0.0,t),
        'productionRate[2,germany]'             : lambda t: self.delay( self.memoize('productionStart[2,germany]', ( t - (self.memoize('productionDuration[2,germany]', t)) )),self.memoize('productionDuration[2,germany]', t),0.0,t),
        'productionRate[2,england]'             : lambda t: self.delay( self.memoize('productionStart[2,england]', ( t - (self.memoize('productionDuration[2,england]', t)) )),self.memoize('productionDuration[2,england]', t),0.0,t),
        'productionRate[2,austria]'             : lambda t: self.delay( self.memoize('productionStart[2,austria]', ( t - (self.memoize('productionDuration[2,austria]', t)) )),self.memoize('productionDuration[2,austria]', t),0.0,t),
        'productionRate[2,greece]'             : lambda t: self.delay( self.memoize('productionStart[2,greece]', ( t - (self.memoize('productionDuration[2,greece]', t)) )),self.memoize('productionDuration[2,greece]', t),0.0,t),
        'productionRate[3,germany]'             : lambda t: self.delay( self.memoize('productionStart[3,germany]', ( t - (self.memoize('productionDuration[3,germany]', t)) )),self.memoize('productionDuration[3,germany]', t),0.0,t),
        'productionRate[3,england]'             : lambda t: self.delay( self.memoize('productionStart[3,england]', ( t - (self.memoize('productionDuration[3,england]', t)) )),self.memoize('productionDuration[3,england]', t),0.0,t),
        'productionRate[3,austria]'             : lambda t: self.delay( self.memoize('productionStart[3,austria]', ( t - (self.memoize('productionDuration[3,austria]', t)) )),self.memoize('productionDuration[3,austria]', t),0.0,t),
        'productionRate[3,greece]'             : lambda t: self.delay( self.memoize('productionStart[3,greece]', ( t - (self.memoize('productionDuration[3,greece]', t)) )),self.memoize('productionDuration[3,greece]', t),0.0,t),
        'productionStart'             : lambda t: self.memoize('productionStart[1,germany]', t) + self.memoize('productionStart[1,england]', t) + self.memoize('productionStart[1,austria]', t) + self.memoize('productionStart[1,greece]', t) + self.memoize('productionStart[2,germany]', t) + self.memoize('productionStart[2,england]', t) + self.memoize('productionStart[2,austria]', t) + self.memoize('productionStart[2,greece]', t) + self.memoize('productionStart[3,germany]', t) + self.memoize('productionStart[3,england]', t) + self.memoize('productionStart[3,austria]', t) + self.memoize('productionStart[3,greece]', t),
        'productionStart[1,germany]'             : lambda t: self.memoize('productionStartRate[1,germany]', t),
        'productionStart[1,england]'             : lambda t: self.memoize('productionStartRate[1,england]', t),
        'productionStart[1,austria]'             : lambda t: self.memoize('productionStartRate[1,austria]', t),
        'productionStart[1,greece]'             : lambda t: self.memoize('productionStartRate[1,greece]', t),
        'productionStart[2,germany]'             : lambda t: self.memoize('productionStartRate[2,germany]', t),
        'productionStart[2,england]'             : lambda t: self.memoize('productionStartRate[2,england]', t),
        'productionStart[2,austria]'             : lambda t: self.memoize('productionStartRate[2,austria]', t),
        'productionStart[2,greece]'             : lambda t: self.memoize('productionStartRate[2,greece]', t),
        'productionStart[3,germany]'             : lambda t: self.memoize('productionStartRate[3,germany]', t),
        'productionStart[3,england]'             : lambda t: self.memoize('productionStartRate[3,england]', t),
        'productionStart[3,austria]'             : lambda t: self.memoize('productionStartRate[3,austria]', t),
        'productionStart[3,greece]'             : lambda t: self.memoize('productionStartRate[3,greece]', t),
        
    
        # converters
        'averageInventory'      : lambda t: np.mean(self.memoize('inventory[*,*]', t)),
        'averageInventoryUsingSize'      : lambda t: np.sum(self.memoize('inventory[*,*]', t)) / (len(self.memoize('inventory[*,*]', t))),
        'inventorySize'      : lambda t: 12.0,
        'largestGermanInventory'      : lambda t: self.memoize('inventory['+ str(self.rank(self.memoize('inventory[*,germany]', t), (len(self.memoize('inventory[*,germany]', t)))))+',germany]', t),
        'productionDuration'      : lambda t: self.memoize('productionDuration[1,germany]', t) + self.memoize('productionDuration[1,england]', t) + self.memoize('productionDuration[1,austria]', t) + self.memoize('productionDuration[1,greece]', t) + self.memoize('productionDuration[2,germany]', t) + self.memoize('productionDuration[2,england]', t) + self.memoize('productionDuration[2,austria]', t) + self.memoize('productionDuration[2,greece]', t) + self.memoize('productionDuration[3,germany]', t) + self.memoize('productionDuration[3,england]', t) + self.memoize('productionDuration[3,austria]', t) + self.memoize('productionDuration[3,greece]', t),
        'productionDuration[1,germany]'      : lambda t: 1.0,
        'productionDuration[1,england]'      : lambda t: 2.0,
        'productionDuration[1,austria]'      : lambda t: 3.0,
        'productionDuration[1,greece]'      : lambda t: 4.0,
        'productionDuration[2,germany]'      : lambda t: 5.0,
        'productionDuration[2,england]'      : lambda t: 6.0,
        'productionDuration[2,austria]'      : lambda t: 8.0,
        'productionDuration[2,greece]'      : lambda t: 7.0,
        'productionDuration[3,germany]'      : lambda t: 9.0,
        'productionDuration[3,england]'      : lambda t: 10.0,
        'productionDuration[3,austria]'      : lambda t: 11.0,
        'productionDuration[3,greece]'      : lambda t: 12.0,
        'productionStartRate'      : lambda t: self.memoize('productionStartRate[1,germany]', t) + self.memoize('productionStartRate[1,england]', t) + self.memoize('productionStartRate[1,austria]', t) + self.memoize('productionStartRate[1,greece]', t) + self.memoize('productionStartRate[2,germany]', t) + self.memoize('productionStartRate[2,england]', t) + self.memoize('productionStartRate[2,austria]', t) + self.memoize('productionStartRate[2,greece]', t) + self.memoize('productionStartRate[3,germany]', t) + self.memoize('productionStartRate[3,england]', t) + self.memoize('productionStartRate[3,austria]', t) + self.memoize('productionStartRate[3,greece]', t),
        'productionStartRate[1,germany]'      : lambda t: 10.0,
        'productionStartRate[1,england]'      : lambda t: 20.0,
        'productionStartRate[1,austria]'      : lambda t: 30.0,
        'productionStartRate[1,greece]'      : lambda t: 40.0,
        'productionStartRate[2,germany]'      : lambda t: 40.0,
        'productionStartRate[2,england]'      : lambda t: 30.0,
        'productionStartRate[2,austria]'      : lambda t: 20.0,
        'productionStartRate[2,greece]'      : lambda t: 10.0,
        'productionStartRate[3,germany]'      : lambda t: 20.0,
        'productionStartRate[3,england]'      : lambda t: 30.0,
        'productionStartRate[3,austria]'      : lambda t: 40.0,
        'productionStartRate[3,greece]'      : lambda t: 50.0,
        'smallestGermanInventory'      : lambda t: self.memoize('inventory['+ str(self.rank(self.memoize('inventory[*,germany]', t), 1.0))+',germany]', t),
        'totalInventory'      : lambda t: np.sum(self.memoize('inventory[*,*]', t)),
        
    
        # gf
        
    
        #constants
        
    
    
        }
    
        self.points = {
            
        }
    
    
        self.dimensions = {
        	'countries': {
                'labels': [ 'germany',  'england',  'austria',  'greece'  ],
                'variables': [ 'production',  'inventory',  'productionStartRate',  'productionDuration',  'productionStart',  'productionRate'  ],
            },
        	'products': {
                'labels': [ '1',  '2',  '3'  ],
                'variables': [ 'production',  'inventory',  'productionStartRate',  'productionDuration',  'productionStart',  'productionRate'  ],
            },
        	'': {
                'labels': [  ],
                'variables': [  ],
            },
        }
                
        self.dimensions_order = {'inventory': ['products', 'countries'], 'production': ['products', 'countries'], 'productionDuration': ['products', 'countries'], 'productionStartRate': ['products', 'countries'], 'productionRate': ['products', 'countries'], 'productionStart': ['products', 'countries']}     
    
        self.stocks = ['inventory',   'inventory[1,germany]',   'inventory[1,england]',   'inventory[1,austria]',   'inventory[1,greece]',   'inventory[2,germany]',   'inventory[2,england]',   'inventory[2,austria]',   'inventory[2,greece]',   'inventory[3,germany]',   'inventory[3,england]',   'inventory[3,austria]',   'inventory[3,greece]',   'production',   'production[1,germany]',   'production[1,england]',   'production[1,austria]',   'production[1,greece]',   'production[2,germany]',   'production[2,england]',   'production[2,austria]',   'production[2,greece]',   'production[3,germany]',   'production[3,england]',   'production[3,austria]',   'production[3,greece]'  ]
        self.flows = ['productionRate',   'productionRate[1,germany]',   'productionRate[1,england]',   'productionRate[1,austria]',   'productionRate[1,greece]',   'productionRate[2,germany]',   'productionRate[2,england]',   'productionRate[2,austria]',   'productionRate[2,greece]',   'productionRate[3,germany]',   'productionRate[3,england]',   'productionRate[3,austria]',   'productionRate[3,greece]',   'productionStart',   'productionStart[1,germany]',   'productionStart[1,england]',   'productionStart[1,austria]',   'productionStart[1,greece]',   'productionStart[2,germany]',   'productionStart[2,england]',   'productionStart[2,austria]',   'productionStart[2,greece]',   'productionStart[3,germany]',   'productionStart[3,england]',   'productionStart[3,austria]',   'productionStart[3,greece]'  ]
        self.converters = ['averageInventory',   'averageInventoryUsingSize',   'inventorySize',   'largestGermanInventory',   'productionDuration',   'productionDuration[1,germany]',   'productionDuration[1,england]',   'productionDuration[1,austria]',   'productionDuration[1,greece]',   'productionDuration[2,germany]',   'productionDuration[2,england]',   'productionDuration[2,austria]',   'productionDuration[2,greece]',   'productionDuration[3,germany]',   'productionDuration[3,england]',   'productionDuration[3,austria]',   'productionDuration[3,greece]',   'productionStartRate',   'productionStartRate[1,germany]',   'productionStartRate[1,england]',   'productionStartRate[1,austria]',   'productionStartRate[1,greece]',   'productionStartRate[2,germany]',   'productionStartRate[2,england]',   'productionStartRate[2,austria]',   'productionStartRate[2,greece]',   'productionStartRate[3,germany]',   'productionStartRate[3,england]',   'productionStartRate[3,austria]',   'productionStartRate[3,greece]',   'smallestGermanInventory',   'totalInventory'  ]
        self.gf = []
        self.constants= []
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
        return self.starttime, self.stoptime, self.dt, 'months', 'Euler'
    