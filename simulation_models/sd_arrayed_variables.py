
#      _                   _ _
#  _____| |__ ___ _ __  _ __(_| |___ _ _
# (_-/ _` / _/ _ | '  \| '_ | | / -_| '_|
# /__\__,_\__\___|_|_|_| .__|_|_\___|_|
#                      |_|
# Copyright (c) 2013-2016 transentis management & consulting. All rights reserved.
#
try:
    from sdmodel import LERP, SDModel
except:
    from BPTK_Py.sdcompiler.sdmodel import LERP, SDModel
    
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import gammaln
import math, statistics
import random, logging


def random_with_seed(seed):
    random.seed(seed)
    return random.random()

def beta_with_seed(a,b,seed):
    np.random.seed(seed)
    return np.random.beta(a,b)
    
def binomial_with_seed(n,p,seed):
    np.random.seed(seed)
    return np.random.binomial(n,p)
    
def gamma_with_seed(shape,scale,seed):
    np.random.seed(seed)
    return np.random.gamma(shape,scale)
    
def exprnd_with_seed(plambda,seed):
    np.random.seed(seed)
    return np.random.exponential(plambda)
    
def geometric_with_seed(p,seed):
    np.random.seed(seed)
    return np.random.geometric(p)
    


class simulation_model(SDModel):
    import logging
    def rank(self, lis, rank):
        rank = int(rank)
        sorted_list = sorted(lis)
        try:
            rankth_elem = sorted_list[rank-1]
        except IndexError as e:
            logging.error("RANK: Rank {} too high for array of size {}".format(rank,len(lis)))
        return lis.index(rankth_elem)+1
        
    def __init__(self):
        # Simulation Buildins
        self.dt = 0.25
        self.starttime = 1
        self.stoptime = 13
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
        'averageInventoryUsingSize'      : lambda t: np.sum(self.memoize('inventory[*,*]', t)) / len( self.memoize('inventory[*,*]', t)),
        'inventorySize'      : lambda t: 12,
        'largestGermanInventory'      : lambda t: self.memoize('inventory['+ str(self.rank(self.memoize('inventory[*,germany]', t), len( self.memoize('inventory[*,germany]', t))))+',germany]', t),
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
    
    def specs(self):
        return self.starttime, self.stoptime, self.dt, 'months', 'Euler'
    