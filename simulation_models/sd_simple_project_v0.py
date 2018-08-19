#      _                   _ _
#  _____| |__ ___ _ __  _ __(_| |___ _ _
# (_-/ _` / _/ _ | '  \| '_ | | / -_| '_|
# /__\__,_\__\___|_|_|_| .__|_|_\___|_|
#                      |_|
# Copyright (c) 2013-2016 transentis management & consulting. All rights reserved.
#




import statistics
import math
import random
import numpy as np
from scipy.interpolate import interp1d

# linear interpolation between a set of points
def LERP(x,points):
    x_vals = np.array([ x[0] for x in points])
    y_vals = np.array([x[1] for x in points])

    if x<= x_vals[0]:
        return y_vals[0]

    if x >= x_vals[len(x_vals)-1]:
        return y_vals[len(x_vals)-1]

    f = interp1d(x_vals, y_vals)
    return float(f(x))


class simulation_model():
  def memoize(self, equation, arg):
    mymemo = self.memo[equation]
    if arg in mymemo.keys():
      return mymemo[arg]
    else:
      result = self.equations[equation](arg)
      mymemo[arg] = result

    return result

  def __init__(self):
    # Simulation Buildins
    self.dt = 0.25
    self.starttime = 1
    self.stoptime = 120
    self.equations = {
  	# Stocks 
  		'closedTasks': lambda t : ( (0) if ( t  <=  self.starttime ) else (self.memoize('closedTasks',t-self.dt) +  self.dt  * ( self.memoize('completionRate',t-self.dt) )) ),

  		'openTasks': lambda t : ( (self.memoize('initialOpenTasks', t)) if ( t  <=  self.starttime ) else (self.memoize('openTasks',t-self.dt) +  self.dt  * ( -1 * ( self.memoize('completionRate',t-self.dt) ) )) ),

  		'staff': lambda t : ( (self.memoize('initialStaff', t)) if ( t  <=  self.starttime ) else (self.memoize('staff',t-self.dt) +  self.dt  * 0) ),
    # flows 
  		'completionRate': lambda t : max( 0, min( self.memoize('openTasks', t), self.memoize('staff', t) * self.memoize('productivity', t) / self.memoize('effortPerTask', t) ) ),
  		# converters 
  		'currentDate': lambda t :  t ,

  		'remainingTime': lambda t : max( self.memoize('deadline', t) - self.memoize('currentDate', t), 0 ),

  		'schedulePressure': lambda t : min( ( self.memoize('openTasks', t) * self.memoize('effortPerTask', t) / self.memoize('staff', t) ) / max( self.memoize('remainingTime', t), 1 ), 2.5 ),
    # gf 
  		'productivity': lambda t : LERP(self.memoize('schedulePressure', t),self.points['productivity']),
    #constants
  		'deadline': lambda t : 100
      ,
  		'effortPerTask': lambda t : 1
      ,
  		'initialOpenTasks': lambda t : 110
      ,
  		'initialStaff': lambda t : 1
      ,
    }

    self.points = {
  		'productivity': [ [0,0.093],[0.25,0.093],[0.5,0.093],[0.75,0.086],[1,1],[1.25,1.186],[1.5,1.236],[1.75,1.25],[2,1.25],[2.25,1.25],[2.5,1.25] ],
  	 }

    self.dimensions = {
  		'Dim_Name_1': {
  			'labels': [ '1' ],
  			'variables': [  ]
  		},
  	 }

    self.stocks = ['closedTasks','openTasks','staff']
    self.flows = ['completionRate']
    self.converters = ['currentDate','remainingTime','schedulePressure']
    self.gf = ['productivity']
    self.constants= ['deadline','effortPerTask','initialOpenTasks','initialStaff']
    self.events = [
    	]

    self.memo = {}
    for key in list(self.equations.keys()):
      self.memo[key] = {}  # DICT OF DICTS!

  def specs(self):
    return self.starttime, self.stoptime, self.dt, 'Days', 'Euler'

  def setDT(self,v):
    self.dt = v

  def setStarttime(self,v):
    self.starttime = v

  def setStoptime(self,v):
    self.stoptime = v

