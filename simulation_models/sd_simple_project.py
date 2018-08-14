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

# linear interpolation between a set points
def LERP(x, points):
	first = 0
	last = len(points)-1

	def getX(i):
			return points[i][0]

	def getY(i):
			return points[i][1]

	def getOffset(x):
			for i in range(first,last):
					if x < getX(i): return i-1
			return last -1

	if x <= getX(first): return getY(first)
	if x >= getX(last): return getY(last)

	n = getOffset(x)
	x0 = getX(n)
	y0 = getY(n)
	x1 = getX(n+1)
	y1 = getY(n+1)

	return (y1 - y0) * (x - x0) / (x1 - x0) + y0


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
  		'initialOpenTasks': lambda t : 100
      ,
  		'initialStaff': lambda t : 1
      ,
    }

    self.points = {
  		'productivity': [ [0,0.4],[0.25,0.444],[0.5,0.506],[0.75,0.594],[1,1.03400735294118],[1.25,1.119],[1.5,1.1625],[1.75,1.2125],[2,1.2375],[2.25,1.245],[2.5,1.25] ],
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

