#      _                   _ _
#  _____| |__ ___ _ __  _ __(_| |___ _ _
# (_-/ _` / _/ _ | '  \| '_ | | / -_| '_|
# /__\__,_\__\___|_|_|_| .__|_|_\___|_|
#                      |_|
# Copyright (c) 2013-2016 transentis management & consulting. All rights reserved.
#





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
    self.dt = 1
    self.starttime = 0
    self.stoptime = 60
    self.equations = {
  	# Stocks 
  		'advertisingCustomers': lambda t : ( (0) if ( t  <=  self.starttime ) else (self.memoize('advertisingCustomers',t-self.dt) +  self.dt  * ( self.memoize('advCustIn',t-self.dt) )) ),

  		'customers': lambda t : ( (self.memoize('initialCustomers', t)) if ( t  <=  self.starttime ) else (self.memoize('customers',t-self.dt) +  self.dt  * ( self.memoize('customerAcquisition',t-self.dt) )) ),

  		'profit': lambda t : ( (0 - self.memoize('initialInvestmentInService', t)) if ( t  <=  self.starttime ) else (self.memoize('profit',t-self.dt) +  self.dt  * ( self.memoize('earnings',t-self.dt) - ( self.memoize('spending',t-self.dt) ) )) ),

  		'referralCustomers': lambda t : ( (0) if ( t  <=  self.starttime ) else (self.memoize('referralCustomers',t-self.dt) +  self.dt  * ( self.memoize('referralCustIn',t-self.dt) )) ),
    # flows 
  		'advCustIn': lambda t : max( 0, self.memoize('acquisitionThroughAdvertising', t) ),
  	
  		'customerAcquisition': lambda t : max( 0, self.memoize('acquisitionThroughAdvertising', t) + self.memoize('acquisitionThroughReferrals', t) ),
  	
  		'earnings': lambda t : max( 0, self.memoize('serviceMargin', t) * self.memoize('serviceFee', t) * self.memoize('customers', t) ),
  	
  		'referralCustIn': lambda t : max( 0, self.memoize('acquisitionThroughReferrals', t) ),
  	
  		'spending': lambda t : max( 0, ( (self.memoize('acquisitionThroughReferrals', t) * ( self.memoize('referralFreeMonths', t) * self.memoize('serviceFee', t) / self.memoize('referrals', t) ) + self.memoize('referralAdvertisingCost', t) + self.memoize('classicalAdvertisingCost', t)) if (self.memoize('referrals', t) > 0) else (self.memoize('classicalAdvertisingCost', t)) ) ),
  		# converters 
  		'acquisitionThroughAdvertising': lambda t : self.memoize('potentialCustomersReachedThroughAdvertising', t) * self.memoize('advertisingSuccessPct', t) / 100,

  		'acquisitionThroughReferrals': lambda t : self.memoize('referrals', t) * self.memoize('customers', t) * ( 1 - self.memoize('marketSaturationPct', t) / 100 ) * self.memoize('referralProgramAdoptionPct', t) / 100,

  		'marketSaturationPct': lambda t : 100 * self.memoize('customers', t) / self.memoize('targetMarket', t),

  		'potentialCustomersReachedThroughAdvertising': lambda t : self.memoize('personsReachedPerEuro', t) * self.memoize('classicalAdvertisingCost', t) * self.memoize('targetCustomerDilutionPct', t) / 100 * ( 1 - self.memoize('marketSaturationPct', t) / 100 ),
    # gf     #constants
  		'advertisingSuccessPct': lambda t : 0.1
      ,
  		'classicalAdvertisingCost': lambda t : 10000
      ,
  		'initialCustomers': lambda t : 0
      ,
  		'initialInvestmentInService': lambda t : 1000000
      ,
  		'personsReachedPerEuro': lambda t : 100
      ,
  		'referralAdvertisingCost': lambda t : 10000
      ,
  		'referralFreeMonths': lambda t : 3
      ,
  		'referralProgramAdoptionPct': lambda t : 30
      ,
  		'referrals': lambda t : 0
      ,
  		'serviceFee': lambda t : 10
      ,
  		'serviceMargin': lambda t : 0.5
      ,
  		'targetCustomerDilutionPct': lambda t : 80
      ,
  		'targetMarket': lambda t : 6000000
      ,
    }

    self.points = {
  	 }

    self.dimensions = {
  	 }

    self.stocks = ['advertisingCustomers','customers','profit','referralCustomers']
    self.flows = ['advCustIn','customerAcquisition','earnings','referralCustIn','spending']
    self.converters = ['acquisitionThroughAdvertising','acquisitionThroughReferrals','marketSaturationPct','potentialCustomersReachedThroughAdvertising']
    self.gf = []
    self.constants= ['advertisingSuccessPct','classicalAdvertisingCost','initialCustomers','initialInvestmentInService','personsReachedPerEuro','referralAdvertisingCost','referralFreeMonths','referralProgramAdoptionPct','referrals','serviceFee','serviceMargin','targetCustomerDilutionPct','targetMarket']
    self.events = [
    	]

    self.memo = {}
    for key in list(self.equations.keys()):
      self.memo[key] = {}  # DICT OF DICTS!

  def specs(self):
    return self.starttime, self.stoptime, self.dt, 'Months', 'Euler'

  def setDT(self,v):
    self.dt = v

  def setStarttime(self,v):
    self.starttime = v

  def setStoptime(self,v):
    self.stoptime = v

