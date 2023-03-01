
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
        self.units = 'Weeks'
        self.method = 'Euler'
        self.equations = {

        # Stocks
        
    
        'brewery.deliveries'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('brewery.deliveries',t-self.dt) + self.dt * ( self.memoize('brewery.outgoingDeliveryRate',t-self.dt) )) ),
        'brewery.incomingOrders'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('brewery.incomingOrders',t-self.dt) + self.dt * ( self.memoize('brewery.incomingOrderRate',t-self.dt) )) ),
        'brewery.inventory'          : lambda t: ( (400.0) if ( t  <=  self.starttime ) else (self.memoize('brewery.inventory',t-self.dt) + self.dt * ( self.memoize('brewery.incomingDeliveryRate',t-self.dt) - ( self.memoize('brewery.outgoingDeliveryRate',t-self.dt) ) )) ),
        'brewery.openOrders'          : lambda t: ( (200.0) if ( t  <=  self.starttime ) else (self.memoize('brewery.openOrders',t-self.dt) + self.dt * ( self.memoize('brewery.orderRate',t-self.dt) - ( self.memoize('brewery.incomingDeliveryRate',t-self.dt) ) )) ),
        'brewery.orderLine'          : lambda t: ( (100.0) if ( t  <=  self.starttime ) else (self.memoize('brewery.orderLine',t-self.dt) + self.dt * ( self.memoize('brewery.makingOrders',t-self.dt) - ( self.memoize('brewery.sendingOrders',t-self.dt) ) )) ),
        'distributor.deliveries'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('distributor.deliveries',t-self.dt) + self.dt * ( self.memoize('distributor.outgoingDeliveryRate',t-self.dt) )) ),
        'distributor.incomingOrders'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('distributor.incomingOrders',t-self.dt) + self.dt * ( self.memoize('distributor.incomingOrderRate',t-self.dt) )) ),
        'distributor.inventory'          : lambda t: ( (400.0) if ( t  <=  self.starttime ) else (self.memoize('distributor.inventory',t-self.dt) + self.dt * ( self.memoize('distributor.incomingDeliveryRate',t-self.dt) - ( self.memoize('distributor.outgoingDeliveryRate',t-self.dt) ) )) ),
        'distributor.openOrders'          : lambda t: ( (200.0) if ( t  <=  self.starttime ) else (self.memoize('distributor.openOrders',t-self.dt) + self.dt * ( self.memoize('distributor.orderRate',t-self.dt) - ( self.memoize('distributor.incomingDeliveryRate',t-self.dt) ) )) ),
        'distributor.orderLine'          : lambda t: ( (100.0) if ( t  <=  self.starttime ) else (self.memoize('distributor.orderLine',t-self.dt) + self.dt * ( self.memoize('distributor.makingOrders',t-self.dt) - ( self.memoize('distributor.sendingOrders',t-self.dt) ) )) ),
        'performanceControlling.breweryInventory'          : lambda t: ( (0) if ( t  <=  self.starttime ) else (self.memoize('performanceControlling.breweryInventory',t-self.dt) + self.dt * 0) ),
        'performanceControlling.distributorInventory'          : lambda t: ( (0) if ( t  <=  self.starttime ) else (self.memoize('performanceControlling.distributorInventory',t-self.dt) + self.dt * 0) ),
        'performanceControlling.retailerCostAcc'          : lambda t: ( (max([0 , 0.0])) if ( t  <=  self.starttime ) else (self.memoize('performanceControlling.retailerCostAcc',t-self.dt) + self.dt * ( self.memoize('performanceControlling.monthlyCostIn',t-self.dt) )) ),
        'performanceControlling.retailerInventory'          : lambda t: ( (0) if ( t  <=  self.starttime ) else (self.memoize('performanceControlling.retailerInventory',t-self.dt) + self.dt * 0) ),
        'performanceControlling.supplyChainCostAcc'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('performanceControlling.supplyChainCostAcc',t-self.dt) + self.dt * ( self.memoize('performanceControlling.accSupplyChainCost',t-self.dt) )) ),
        'performanceControlling.wholesalerInventory'          : lambda t: ( (0) if ( t  <=  self.starttime ) else (self.memoize('performanceControlling.wholesalerInventory',t-self.dt) + self.dt * 0) ),
        'retailer.deliveries'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('retailer.deliveries',t-self.dt) + self.dt * ( self.memoize('retailer.outgoingDeliveryRate',t-self.dt) )) ),
        'retailer.incomingOrders'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('retailer.incomingOrders',t-self.dt) + self.dt * ( self.memoize('retailer.incomingOrderRate',t-self.dt) )) ),
        'retailer.inventory'          : lambda t: ( (400.0) if ( t  <=  self.starttime ) else (self.memoize('retailer.inventory',t-self.dt) + self.dt * ( self.memoize('retailer.incomingDeliveryRate',t-self.dt) - ( self.memoize('retailer.outgoingDeliveryRate',t-self.dt) ) )) ),
        'retailer.openOrders'          : lambda t: ( (200.0) if ( t  <=  self.starttime ) else (self.memoize('retailer.openOrders',t-self.dt) + self.dt * ( self.memoize('retailer.orders',t-self.dt) - ( self.memoize('retailer.incomingDeliveryRate',t-self.dt) ) )) ),
        'retailer.orderLine'          : lambda t: ( (100.0) if ( t  <=  self.starttime ) else (self.memoize('retailer.orderLine',t-self.dt) + self.dt * ( self.memoize('retailer.makingOrders',t-self.dt) - ( self.memoize('retailer.sendingOrders',t-self.dt) ) )) ),
        'wholesaler.deliveries'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('wholesaler.deliveries',t-self.dt) + self.dt * ( self.memoize('wholesaler.outgoingDeliveryRate',t-self.dt) )) ),
        'wholesaler.incomingOrders'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('wholesaler.incomingOrders',t-self.dt) + self.dt * ( self.memoize('wholesaler.incomingOrderRate',t-self.dt) )) ),
        'wholesaler.inventory'          : lambda t: ( (400.0) if ( t  <=  self.starttime ) else (self.memoize('wholesaler.inventory',t-self.dt) + self.dt * ( self.memoize('wholesaler.incomingDeliveryRate',t-self.dt) - ( self.memoize('wholesaler.outgoingDeliveryRate',t-self.dt) ) )) ),
        'wholesaler.openOrders'          : lambda t: ( (200.0) if ( t  <=  self.starttime ) else (self.memoize('wholesaler.openOrders',t-self.dt) + self.dt * ( self.memoize('wholesaler.orders',t-self.dt) - ( self.memoize('wholesaler.incomingDeliveryRate',t-self.dt) ) )) ),
        'wholesaler.orderLine'          : lambda t: ( (100.0) if ( t  <=  self.starttime ) else (self.memoize('wholesaler.orderLine',t-self.dt) + self.dt * ( self.memoize('wholesaler.makingOrders',t-self.dt) - ( self.memoize('wholesaler.sendingOrders',t-self.dt) ) )) ),
        
    
        # Flows
        'brewery.incomingDeliveryRate'             : lambda t: max([0 , self.memoize('brewery.incomingDelivery', t)]),
        'brewery.incomingOrderRate'             : lambda t: max([0 , self.memoize('brewery.incomingOrder', t)]),
        'brewery.makingOrders'             : lambda t: max([0 , self.memoize('brewery.orderDecision', t)]),
        'brewery.orderRate'             : lambda t: max([0 , self.memoize('brewery.makingOrders', t)]),
        'brewery.outgoingDeliveryRate'             : lambda t: max([0 , min([self.memoize('brewery.inventory', t) + self.memoize('brewery.incomingDeliveryRate', t) , self.memoize('brewery.outgoingDelivery', t)])]),
        'brewery.sendingOrders'             : lambda t: max([0 , self.delay( self.memoize('brewery.makingOrders', ( t - (self.memoize('policySettings.orderDelay', t)) )),self.memoize('policySettings.orderDelay', t),100.0,t)]),
        'distributor.incomingDeliveryRate'             : lambda t: max([0 , self.memoize('distributor.incomingDelivery', t)]),
        'distributor.incomingOrderRate'             : lambda t: max([0 , self.memoize('distributor.incomingOrder', t)]),
        'distributor.makingOrders'             : lambda t: max([0 , self.memoize('distributor.orderDecision', t)]),
        'distributor.orderRate'             : lambda t: max([0 , self.memoize('distributor.makingOrders', t)]),
        'distributor.outgoingDeliveryRate'             : lambda t: max([0 , min([self.memoize('distributor.inventory', t) + self.memoize('distributor.incomingDeliveryRate', t) , self.memoize('distributor.outgoingDelivery', t)])]),
        'distributor.sendingOrders'             : lambda t: max([0 , self.delay( self.memoize('distributor.makingOrders', ( t - (self.memoize('policySettings.orderDelay', t)) )),self.memoize('policySettings.orderDelay', t),100.0,t)]),
        'performanceControlling.accSupplyChainCost'             : lambda t: max([0 , self.memoize('performanceControlling.supplyChainCost', t)]),
        'performanceControlling.monthlyCostIn'             : lambda t: max([0 , self.memoize('performanceControlling.retailerCost', t)]),
        'retailer.incomingDeliveryRate'             : lambda t: max([0 , self.memoize('retailer.incomingDelivery', t)]),
        'retailer.incomingOrderRate'             : lambda t: max([0 , self.memoize('retailer.incomingOrder', t)]),
        'retailer.makingOrders'             : lambda t: max([0 , self.memoize('policySettings.gameModeOn', t) * ( 1.0 - self.memoize('policySettings.multiplayerModeOn', t) ) * self.memoize('retailer.order', t) + ( 1.0 - self.memoize('policySettings.gameModeOn', t) ) * self.memoize('retailer.orderDecision', t)]),
        'retailer.orders'             : lambda t: max([0 , self.memoize('retailer.orderDecision', t)]),
        'retailer.outgoingDeliveryRate'             : lambda t: max([0 , min([self.memoize('retailer.inventory', t) + self.memoize('retailer.incomingDeliveryRate', t) , self.memoize('retailer.outgoingDelivery', t)])]),
        'retailer.sendingOrders'             : lambda t: max([0 , self.delay( self.memoize('retailer.makingOrders', ( t - (self.memoize('policySettings.orderDelay', t)) )),self.memoize('policySettings.orderDelay', t),100.0,t)]),
        'wholesaler.incomingDeliveryRate'             : lambda t: max([0 , self.memoize('wholesaler.incomingDelivery', t)]),
        'wholesaler.incomingOrderRate'             : lambda t: max([0 , self.memoize('wholesaler.incomingOrder', t)]),
        'wholesaler.makingOrders'             : lambda t: max([0 , self.memoize('wholesaler.orderDecision', t)]),
        'wholesaler.orders'             : lambda t: max([0 , self.memoize('wholesaler.makingOrders', t)]),
        'wholesaler.outgoingDeliveryRate'             : lambda t: max([0 , min([self.memoize('wholesaler.inventory', t) + self.memoize('wholesaler.incomingDeliveryRate', t) , self.memoize('wholesaler.outgoingDelivery', t)])]),
        'wholesaler.sendingOrders'             : lambda t: max([0 , self.delay( self.memoize('wholesaler.makingOrders', ( t - (self.memoize('policySettings.orderDelay', t)) )),self.memoize('policySettings.orderDelay', t),100.0,t)]),
        
    
        # converters
        'brewery.actualOrder'      : lambda t: 0.0,
        'brewery.actualProduction'      : lambda t: self.memoize('policySettings.gameModeOn', t) * ( self.memoize('policySettings.multiplayerModeOn', t) * self.memoize('brewery.production', t) + ( 1.0 - self.memoize('policySettings.multiplayerModeOn', t) ) * self.memoize('brewery.orderFromOrderLine', t) ) + ( 1.0 - self.memoize('policySettings.gameModeOn', t) ) * self.memoize('brewery.orderFromOrderLine', t),
        'brewery.backorder'      : lambda t: max([self.memoize('brewery.incomingOrders', t) - self.memoize('brewery.deliveries', t) , 0.0]),
        'brewery.converter1'      : lambda t: 0.0,
        'brewery.deliveryDelay'      : lambda t: 0.0,
        'brewery.deliveryPolicy'      : lambda t: min([self.memoize('brewery.backorder', t) + self.memoize('brewery.incomingOrder', t) , self.memoize('brewery.inventory', t) + self.memoize('brewery.incomingDeliveryRate', t)]),
        'brewery.expectedOrder'      : lambda t: self.memoize('brewery.incomingOrder', t),
        'brewery.incomingDelivery'      : lambda t: self.delay( self.memoize('brewery.actualProduction', ( t - (self.memoize('policySettings.deliveryDelay', t)) )),self.memoize('policySettings.deliveryDelay', t),100.0,t),
        'brewery.incomingOrder'      : lambda t: self.memoize('distributor.actualOrder', t),
        'brewery.multiplayerModeOn'      : lambda t: 0.0,
        'brewery.naiveOrderDecision'      : lambda t: max([self.memoize('policySettings.weightingInventory', t) * ( self.memoize('policySettings.targetInventory', t) - self.memoize('brewery.inventory', t) ) + self.memoize('policySettings.weightingBackorder', t) * self.memoize('brewery.backorder', t) + self.memoize('brewery.expectedOrder', t) , 0.0]),
        'brewery.orderDecision'      : lambda t: self.memoize('brewery.sophisticatedOrderDecision', t) * self.memoize('policySettings.sophisticatedOrderDecisionOn', t) + ( 1.0 - self.memoize('policySettings.sophisticatedOrderDecisionOn', t) ) * self.memoize('brewery.naiveOrderDecision', t),
        'brewery.orderDelay'      : lambda t: 0.0,
        'brewery.orderFromOrderLine'      : lambda t: self.memoize('brewery.sendingOrders', t),
        'brewery.outgoingDelivery'      : lambda t: self.memoize('brewery.deliveryPolicy', t),
        'brewery.production'      : lambda t: 100.0,
        'brewery.singlePlayerSimplePolicyOn'      : lambda t: 0.0,
        'brewery.sophisticatedOrderDecision'      : lambda t: math.floor( max([self.memoize('brewery.expectedOrder', t) + ( self.memoize('policySettings.targetInventory', t) - self.memoize('brewery.inventory', t) + self.memoize('policySettings.weightingOpenOrders', t) * ( self.memoize('brewery.targetSupplyLine', t) - self.memoize('brewery.openOrders', t) ) ) / self.memoize('policySettings.stockAdjustmentTime', t) , 0.0]) ),
        'brewery.sophisticatedOrderDecisionOn'      : lambda t: 0.0,
        'brewery.stockAdjustmentTime'      : lambda t: 0.0,
        'brewery.surplus'      : lambda t: self.memoize('brewery.inventory', t) - self.memoize('brewery.backorder', t),
        'brewery.targetSupplyLine'      : lambda t: self.memoize('policySettings.targetSupplyLineFactor', t) * self.memoize('brewery.expectedOrder', t),
        'brewery.targetSupplyLineFactor'      : lambda t: 0.0,
        'brewery.targetTotalStock'      : lambda t: self.memoize('brewery.targetSupplyLine', t) + self.memoize('policySettings.targetInventory', t),
        'brewery.totalStock'      : lambda t: self.memoize('brewery.openOrders', t) + self.memoize('brewery.inventory', t),
        'brewery.weightOnBackorder'      : lambda t: 0.0,
        'brewery.weightOnInventory'      : lambda t: 0.0,
        'brewery.weightingOnSupplyLine'      : lambda t: 0.0,
        'distributor.actualOrder'      : lambda t: self.memoize('policySettings.gameModeOn', t) * ( self.memoize('policySettings.multiplayerModeOn', t) * self.memoize('distributor.order', t) + ( 1.0 - self.memoize('policySettings.multiplayerModeOn', t) ) * self.memoize('distributor.orderFromOrderLine', t) ) + ( 1.0 - self.memoize('policySettings.gameModeOn', t) ) * self.memoize('distributor.orderFromOrderLine', t),
        'distributor.backorder'      : lambda t: max([self.memoize('distributor.incomingOrders', t) - self.memoize('distributor.deliveries', t) , 0.0]),
        'distributor.converter3'      : lambda t: 0.0,
        'distributor.converter4'      : lambda t: 0.0,
        'distributor.converter5'      : lambda t: 0.0,
        'distributor.converter6'      : lambda t: 0.0,
        'distributor.deliveryPolicy'      : lambda t: min([self.memoize('distributor.backorder', t) + self.memoize('distributor.incomingOrder', t) , self.memoize('distributor.inventory', t) + self.memoize('distributor.incomingDeliveryRate', t)]),
        'distributor.expectedOrder'      : lambda t: self.memoize('distributor.incomingOrder', t),
        'distributor.incomingDelivery'      : lambda t: self.delay( self.memoize('brewery.outgoingDeliveryRate', ( t - (self.memoize('policySettings.deliveryDelay', t)) )),self.memoize('policySettings.deliveryDelay', t),100.0,t),
        'distributor.incomingOrder'      : lambda t: self.memoize('wholesaler.actualOrder', t),
        'distributor.multiplayerModeOn'      : lambda t: 0.0,
        'distributor.naiveOrderDecision'      : lambda t: max([self.memoize('policySettings.weightingInventory', t) * ( self.memoize('policySettings.targetInventory', t) - self.memoize('distributor.inventory', t) ) + self.memoize('policySettings.weightingBackorder', t) * self.memoize('distributor.backorder', t) + self.memoize('distributor.expectedOrder', t) , 0.0]),
        'distributor.order'      : lambda t: 100.0,
        'distributor.orderDecision'      : lambda t: self.memoize('distributor.sophisticatedOrderDecision', t) * self.memoize('policySettings.sophisticatedOrderDecisionOn', t) + ( 1.0 - self.memoize('policySettings.sophisticatedOrderDecisionOn', t) ) * self.memoize('distributor.naiveOrderDecision', t),
        'distributor.orderDelay'      : lambda t: 0.0,
        'distributor.orderFromOrderLine'      : lambda t: self.memoize('distributor.sendingOrders', t),
        'distributor.outgoingDelivery'      : lambda t: self.memoize('distributor.deliveryPolicy', t),
        'distributor.singlePlayerSimplePolicyOn'      : lambda t: 0.0,
        'distributor.sophisticatedOrderDecision'      : lambda t: math.floor( max([self.memoize('distributor.expectedOrder', t) + ( self.memoize('policySettings.targetInventory', t) - self.memoize('distributor.inventory', t) + self.memoize('policySettings.weightingOpenOrders', t) * ( self.memoize('distributor.targetSupplyLine', t) - self.memoize('distributor.openOrders', t) ) ) / self.memoize('policySettings.stockAdjustmentTime', t) , 0.0]) ),
        'distributor.sophisticatedOrderDecisionOn'      : lambda t: 0.0,
        'distributor.stockAdjustmentTime'      : lambda t: 0.0,
        'distributor.surplus'      : lambda t: self.memoize('distributor.inventory', t) - self.memoize('distributor.backorder', t),
        'distributor.targetSupplyLine'      : lambda t: self.memoize('policySettings.targetSupplyLineFactor', t) * self.memoize('distributor.expectedOrder', t),
        'distributor.targetSupplyLineFactor'      : lambda t: 0.0,
        'distributor.totalStock'      : lambda t: self.memoize('distributor.inventory', t) + self.memoize('distributor.openOrders', t),
        'distributor.weightOnBackorder'      : lambda t: 0.0,
        'distributor.weightOnInventory'      : lambda t: 0.0,
        'distributor.weightingOnSupplyLine'      : lambda t: 0.0,
        'performanceControlling.breweryBackorder'      : lambda t: 0.0,
        'performanceControlling.breweryBackorderCost'      : lambda t: self.memoize('performanceControlling.costPerItemInBackorder', t) * self.memoize('brewery.backorder', t),
        'performanceControlling.breweryCost'      : lambda t: self.memoize('performanceControlling.breweryInventoryCost', t) + self.memoize('performanceControlling.breweryBackorderCost', t),
        'performanceControlling.breweryInventoryCost'      : lambda t: self.memoize('performanceControlling.costPerItemInInventory', t) * max([self.memoize('brewery.inventory', t) , self.memoize('policySettings.targetInventory', t)]),
        'performanceControlling.costPerItemInBackorder'      : lambda t: 1.0,
        'performanceControlling.costPerItemInInventory'      : lambda t: 0.5,
        'performanceControlling.distributorBackorderCost'      : lambda t: self.memoize('performanceControlling.costPerItemInBackorder', t) * self.memoize('distributor.backorder', t),
        'performanceControlling.distributorCost'      : lambda t: self.memoize('performanceControlling.distributorBackorderCost', t) + self.memoize('performanceControlling.distributorInventoryCost', t),
        'performanceControlling.distributorDeliveryShortfall'      : lambda t: 0.0,
        'performanceControlling.distributorInventoryCost'      : lambda t: self.memoize('performanceControlling.costPerItemInInventory', t) * max([self.memoize('distributor.inventory', t) , self.memoize('policySettings.targetInventory', t)]),
        'performanceControlling.retailBackorder'      : lambda t: 0.0,
        'performanceControlling.retailerBackorderCost'      : lambda t: self.memoize('performanceControlling.costPerItemInBackorder', t) * self.memoize('retailer.backorder', t),
        'performanceControlling.retailerCost'      : lambda t: self.memoize('performanceControlling.retailerBackorderCost', t) + self.memoize('performanceControlling.retailerInventoryCost', t),
        'performanceControlling.retailerInventoryCost'      : lambda t: self.memoize('performanceControlling.costPerItemInInventory', t) * max([self.memoize('retailer.inventory', t) , self.memoize('policySettings.targetInventory', t)]),
        'performanceControlling.supplyChainCost'      : lambda t: self.memoize('performanceControlling.breweryCost', t) + self.memoize('performanceControlling.retailerCost', t) + self.memoize('performanceControlling.distributorCost', t) + self.memoize('performanceControlling.wholesalerCost', t),
        'performanceControlling.targetInventory'      : lambda t: 0.0,
        'performanceControlling.wholesalerBackorder'      : lambda t: 0.0,
        'performanceControlling.wholesalerBackorderCost'      : lambda t: self.memoize('performanceControlling.costPerItemInBackorder', t) * self.memoize('wholesaler.backorder', t),
        'performanceControlling.wholesalerCost'      : lambda t: self.memoize('performanceControlling.wholesalerBackorderCost', t) + self.memoize('performanceControlling.wholesalerInventoryCost', t),
        'performanceControlling.wholesalerInventoryCost'      : lambda t: self.memoize('performanceControlling.costPerItemInInventory', t) * max([self.memoize('wholesaler.inventory', t) , self.memoize('policySettings.targetInventory', t)]),
        'policySettings.deliveryDelay'      : lambda t: 1.0,
        'policySettings.dynamicCustomerBehaviourOn'      : lambda t: 0.0,
        'policySettings.gameModeOn'      : lambda t: 0.0,
        'policySettings.multiplayerModeOn'      : lambda t: 0.0,
        'policySettings.orderDelay'      : lambda t: 1.0,
        'policySettings.riseInOrder'      : lambda t: 300.0,
        'policySettings.sophisticatedOrderDecisionOn'      : lambda t: 0.0,
        'policySettings.steadyStateOn'      : lambda t: 0.0,
        'policySettings.stockAdjustmentTime'      : lambda t: 8.0,
        'policySettings.targetInventory'      : lambda t: 400.0,
        'policySettings.targetRetailerCost'      : lambda t: 8300.0,
        'policySettings.targetSupplyChainCost'      : lambda t: 29300.0,
        'policySettings.targetSupplyLineFactor'      : lambda t: 2.0,
        'policySettings.targetSurplus'      : lambda t: 250.0,
        'policySettings.weightingBackorder'      : lambda t: 1.0,
        'policySettings.weightingInventory'      : lambda t: 1.0,
        'policySettings.weightingOpenOrders'      : lambda t: 1.0,
        'retailer.actualOrder'      : lambda t: self.memoize('policySettings.gameModeOn', t) * self.memoize('policySettings.multiplayerModeOn', t) * self.memoize('retailer.order', t) + self.memoize('policySettings.gameModeOn', t) * ( 1.0 - self.memoize('policySettings.multiplayerModeOn', t) ) * self.memoize('retailer.orderFromOrderLine', t) + ( 1.0 - self.memoize('policySettings.gameModeOn', t) ) * self.memoize('retailer.orderFromOrderLine', t),
        'retailer.backorder'      : lambda t: max([self.memoize('retailer.incomingOrders', t) - self.memoize('retailer.deliveries', t) , 0.0]),
        'retailer.converter1'      : lambda t: 0.0,
        'retailer.customerOrder'      : lambda t: ( 1.0 - self.memoize('policySettings.dynamicCustomerBehaviourOn', t) ) * ( 100.0 + ( 1.0 - self.memoize('policySettings.steadyStateOn', t) ) * ( self.memoize('retailer.unexpectedRiseInCustomerOrders', t) ) ) + self.memoize('policySettings.dynamicCustomerBehaviourOn', t) * self.memoize('retailer.dynamicCustomerOrder', t),
        'retailer.deliveryDelay'      : lambda t: 0.0,
        'retailer.deliveryPolicy'      : lambda t: min([self.memoize('retailer.backorder', t) + self.memoize('retailer.incomingOrder', t) , self.memoize('retailer.inventory', t) + self.memoize('retailer.incomingDeliveryRate', t)]),
        'retailer.deliveryRate'      : lambda t: 0.0,
        'retailer.dynamicCustomerBehaviourOn'      : lambda t: 0.0,
        'retailer.expectedOrder'      : lambda t: self.memoize('retailer.incomingOrder', t),
        'retailer.incomingDelivery'      : lambda t: self.delay( self.memoize('wholesaler.outgoingDeliveryRate', ( t - (self.memoize('policySettings.deliveryDelay', t)) )),self.memoize('policySettings.deliveryDelay', t),100.0,t),
        'retailer.incomingOrder'      : lambda t: self.memoize('retailer.customerOrder', t),
        'retailer.multiplayerModeOn'      : lambda t: 0.0,
        'retailer.naiveOrderDecision'      : lambda t: max([self.memoize('policySettings.weightingInventory', t) * ( self.memoize('policySettings.targetInventory', t) - self.memoize('retailer.inventory', t) ) + self.memoize('policySettings.weightingBackorder', t) * self.memoize('retailer.backorder', t) + self.memoize('retailer.expectedOrder', t) , 0.0]),
        'retailer.order'      : lambda t: 100.0,
        'retailer.orderDecision'      : lambda t: self.memoize('retailer.sophisticatedOrderDecision', t) * self.memoize('policySettings.sophisticatedOrderDecisionOn', t) + ( 1.0 - self.memoize('policySettings.sophisticatedOrderDecisionOn', t) ) * self.memoize('retailer.naiveOrderDecision', t),
        'retailer.orderDelay'      : lambda t: 0.0,
        'retailer.orderFromOrderLine'      : lambda t: self.memoize('retailer.sendingOrders', t),
        'retailer.outgoingDelivery'      : lambda t: self.memoize('retailer.deliveryPolicy', t),
        'retailer.riseInOrder'      : lambda t: 0.0,
        'retailer.singlePlayerSimplePolicyOn'      : lambda t: 0.0,
        'retailer.sophisticatedOrderDecision'      : lambda t: math.floor( max([self.memoize('retailer.expectedOrder', t) + ( self.memoize('policySettings.targetInventory', t) - self.memoize('retailer.inventory', t) + self.memoize('policySettings.weightingOpenOrders', t) * ( self.memoize('retailer.targetSupplyLine', t) - self.memoize('retailer.openOrders', t) ) ) / self.memoize('policySettings.stockAdjustmentTime', t) , 0.0]) ),
        'retailer.sophisticatedOrderDecisionOn'      : lambda t: 0.0,
        'retailer.steadyStateOn'      : lambda t: 0.0,
        'retailer.stockAdjustmentTime'      : lambda t: 0.0,
        'retailer.surplus'      : lambda t: self.memoize('retailer.inventory', t) - self.memoize('retailer.backorder', t),
        'retailer.targetSupplyLine'      : lambda t: self.memoize('policySettings.targetSupplyLineFactor', t) * self.memoize('retailer.expectedOrder', t),
        'retailer.targetTotalStock'      : lambda t: self.memoize('policySettings.targetInventory', t) + self.memoize('policySettings.weightingOpenOrders', t) * self.memoize('retailer.targetSupplyLine', t),
        'retailer.totalStock'      : lambda t: self.memoize('policySettings.weightingOpenOrders', t) * self.memoize('retailer.openOrders', t) + self.memoize('retailer.inventory', t),
        'retailer.transitAveragingTime'      : lambda t: 0.0,
        'retailer.unexpectedRiseInCustomerOrders'      : lambda t: (0 if t < 2.0 else self.memoize('policySettings.riseInOrder', t)),
        'retailer.weightOnBackorder'      : lambda t: 0.0,
        'retailer.weightOnInventory'      : lambda t: 0.0,
        'retailer.weightingOnSupplyLine'      : lambda t: 0.0,
        'wholesaler.actualOrder'      : lambda t: self.memoize('policySettings.gameModeOn', t) * ( self.memoize('policySettings.multiplayerModeOn', t) * self.memoize('wholesaler.order', t) + ( 1.0 - self.memoize('policySettings.multiplayerModeOn', t) ) * self.memoize('wholesaler.orderFromOrderLine', t) ) + ( 1.0 - self.memoize('policySettings.gameModeOn', t) ) * self.memoize('wholesaler.orderFromOrderLine', t),
        'wholesaler.backorder'      : lambda t: max([self.memoize('wholesaler.incomingOrders', t) - self.memoize('wholesaler.deliveries', t) , 0.0]),
        'wholesaler.converter2'      : lambda t: 0.0,
        'wholesaler.converter3'      : lambda t: 0.0,
        'wholesaler.converter4'      : lambda t: 0.0,
        'wholesaler.converter5'      : lambda t: 0.0,
        'wholesaler.deliveryDecision'      : lambda t: min([self.memoize('wholesaler.backorder', t) + self.memoize('wholesaler.incomingOrder', t) , self.memoize('wholesaler.inventory', t) + self.memoize('wholesaler.incomingDeliveryRate', t)]),
        'wholesaler.expectedOrder'      : lambda t: self.memoize('wholesaler.incomingOrder', t),
        'wholesaler.incomingDelivery'      : lambda t: self.delay( self.memoize('distributor.outgoingDeliveryRate', ( t - (self.memoize('policySettings.deliveryDelay', t)) )),self.memoize('policySettings.deliveryDelay', t),100.0,t),
        'wholesaler.incomingOrder'      : lambda t: self.memoize('retailer.actualOrder', t),
        'wholesaler.multiplayerModeOn'      : lambda t: 0.0,
        'wholesaler.naiveOrderDecision'      : lambda t: max([self.memoize('policySettings.weightingInventory', t) * ( self.memoize('policySettings.targetInventory', t) - self.memoize('wholesaler.inventory', t) ) + self.memoize('policySettings.weightingBackorder', t) * self.memoize('wholesaler.backorder', t) + self.memoize('wholesaler.expectedOrder', t) , 0.0]),
        'wholesaler.order'      : lambda t: 100.0,
        'wholesaler.orderDecision'      : lambda t: self.memoize('wholesaler.sophisticatedOrderDecision', t) * self.memoize('policySettings.sophisticatedOrderDecisionOn', t) + ( 1.0 - self.memoize('policySettings.sophisticatedOrderDecisionOn', t) ) * self.memoize('wholesaler.naiveOrderDecision', t),
        'wholesaler.orderDelay'      : lambda t: 0.0,
        'wholesaler.orderFromOrderLine'      : lambda t: self.memoize('wholesaler.sendingOrders', t),
        'wholesaler.outgoingDelivery'      : lambda t: self.memoize('wholesaler.deliveryDecision', t),
        'wholesaler.singlePlayerSimplePolicyOn'      : lambda t: 0.0,
        'wholesaler.sophisticatedOrderDecision'      : lambda t: math.floor( max([self.memoize('wholesaler.expectedOrder', t) + ( self.memoize('policySettings.targetInventory', t) - self.memoize('wholesaler.inventory', t) + self.memoize('policySettings.weightingOpenOrders', t) * ( self.memoize('wholesaler.targetSupplyLine', t) - self.memoize('wholesaler.openOrders', t) ) ) / self.memoize('policySettings.stockAdjustmentTime', t) , 0.0]) ),
        'wholesaler.sophisticatedOrderDecisionOn'      : lambda t: 0.0,
        'wholesaler.stockAdjustmentTime'      : lambda t: 0.0,
        'wholesaler.surplus'      : lambda t: self.memoize('wholesaler.inventory', t) - self.memoize('wholesaler.backorder', t),
        'wholesaler.targetSupplyLine'      : lambda t: self.memoize('policySettings.targetSupplyLineFactor', t) * self.memoize('wholesaler.expectedOrder', t),
        'wholesaler.targetTotalStock'      : lambda t: self.memoize('wholesaler.targetSupplyLine', t) + self.memoize('policySettings.targetInventory', t),
        'wholesaler.totalStock'      : lambda t: self.memoize('wholesaler.inventory', t) + self.memoize('wholesaler.openOrders', t),
        'wholesaler.transitAveragingTime'      : lambda t: 0.0,
        'wholesaler.weightOnBackorder'      : lambda t: 0.0,
        'wholesaler.weightOnInventory'      : lambda t: 0.0,
        'wholesaler.weightingOnSupplyLine'      : lambda t: 0.0,
        
    
        # gf
        'retailer.dynamicCustomerOrder' : lambda t: LERP(  t , self.points['retailer.dynamicCustomerOrder']),
        
    
        #constants
        'brewery.actualOrder' : lambda t: 0.0,
        'brewery.converter1' : lambda t: 0.0,
        'brewery.deliveryDelay' : lambda t: 0.0,
        'brewery.multiplayerModeOn' : lambda t: 0.0,
        'brewery.orderDelay' : lambda t: 0.0,
        'brewery.singlePlayerSimplePolicyOn' : lambda t: 0.0,
        'brewery.sophisticatedOrderDecisionOn' : lambda t: 0.0,
        'brewery.stockAdjustmentTime' : lambda t: 0.0,
        'brewery.targetSupplyLineFactor' : lambda t: 0.0,
        'brewery.weightOnBackorder' : lambda t: 0.0,
        'brewery.weightOnInventory' : lambda t: 0.0,
        'brewery.weightingOnSupplyLine' : lambda t: 0.0,
        'distributor.converter3' : lambda t: 0.0,
        'distributor.converter4' : lambda t: 0.0,
        'distributor.converter5' : lambda t: 0.0,
        'distributor.converter6' : lambda t: 0.0,
        'distributor.multiplayerModeOn' : lambda t: 0.0,
        'distributor.orderDelay' : lambda t: 0.0,
        'distributor.singlePlayerSimplePolicyOn' : lambda t: 0.0,
        'distributor.sophisticatedOrderDecisionOn' : lambda t: 0.0,
        'distributor.stockAdjustmentTime' : lambda t: 0.0,
        'distributor.targetSupplyLineFactor' : lambda t: 0.0,
        'distributor.weightOnBackorder' : lambda t: 0.0,
        'distributor.weightOnInventory' : lambda t: 0.0,
        'distributor.weightingOnSupplyLine' : lambda t: 0.0,
        'performanceControlling.breweryBackorder' : lambda t: 0.0,
        'performanceControlling.distributorDeliveryShortfall' : lambda t: 0.0,
        'performanceControlling.retailBackorder' : lambda t: 0.0,
        'performanceControlling.targetInventory' : lambda t: 0.0,
        'performanceControlling.wholesalerBackorder' : lambda t: 0.0,
        'retailer.converter1' : lambda t: 0.0,
        'retailer.deliveryDelay' : lambda t: 0.0,
        'retailer.deliveryRate' : lambda t: 0.0,
        'retailer.dynamicCustomerBehaviourOn' : lambda t: 0.0,
        'retailer.multiplayerModeOn' : lambda t: 0.0,
        'retailer.orderDelay' : lambda t: 0.0,
        'retailer.riseInOrder' : lambda t: 0.0,
        'retailer.singlePlayerSimplePolicyOn' : lambda t: 0.0,
        'retailer.sophisticatedOrderDecisionOn' : lambda t: 0.0,
        'retailer.steadyStateOn' : lambda t: 0.0,
        'retailer.stockAdjustmentTime' : lambda t: 0.0,
        'retailer.transitAveragingTime' : lambda t: 0.0,
        'retailer.weightOnBackorder' : lambda t: 0.0,
        'retailer.weightOnInventory' : lambda t: 0.0,
        'retailer.weightingOnSupplyLine' : lambda t: 0.0,
        'wholesaler.converter2' : lambda t: 0.0,
        'wholesaler.converter3' : lambda t: 0.0,
        'wholesaler.converter4' : lambda t: 0.0,
        'wholesaler.converter5' : lambda t: 0.0,
        'wholesaler.multiplayerModeOn' : lambda t: 0.0,
        'wholesaler.orderDelay' : lambda t: 0.0,
        'wholesaler.singlePlayerSimplePolicyOn' : lambda t: 0.0,
        'wholesaler.sophisticatedOrderDecisionOn' : lambda t: 0.0,
        'wholesaler.stockAdjustmentTime' : lambda t: 0.0,
        'wholesaler.transitAveragingTime' : lambda t: 0.0,
        'wholesaler.weightOnBackorder' : lambda t: 0.0,
        'wholesaler.weightOnInventory' : lambda t: 0.0,
        'wholesaler.weightingOnSupplyLine' : lambda t: 0.0,
        
    
    
        }
    
        self.points = {
            'retailer.dynamicCustomerOrder' :  [(1.0, 100.0), (2.0, 100.0), (3.0, 100.0), (4.0, 100.0), (5.0, 100.0), (6.0, 116.393442622951), (7.0, 162.295081967213), (8.0, 757.28813559322), (9.0, 800.0), (10.0, 800.0), (11.0, 800.0), (12.0, 800.0), (13.0, 800.0), (14.0, 800.0), (15.0, 800.0), (16.0, 527.118644067797), (17.0, 508.135593220339), (18.0, 512.881355932203), (19.0, 531.864406779661), (20.0, 553.220338983051), (21.0, 572.203389830509), (22.0, 593.559322033898), (23.0, 655.254237288136), (24.0, 724.067796610169), (25.0, 769.152542372881), (26.0, 764.406779661017), (27.0, 754.915254237288), (28.0, 740.677966101695), (29.0, 716.949152542373), (30.0, 695.593220338983), (31.0, 674.237288135593), (32.0, 624.406779661017), (33.0, 610.169491525424), (34.0, 553.220338983051), (35.0, 496.271186440678), (36.0, 489.152542372881), (37.0, 489.152542372881), (38.0, 486.779661016949), (39.0, 486.779661016949), (40.0, 486.779661016949)]  , 
        }
    
    
        self.dimensions = {
        	'': {
                'labels': [  ],
                'variables': [  ],
            },
        }
                
        self.dimensions_order = {}     
    
        self.stocks = ['brewery.deliveries',   'brewery.incomingOrders',   'brewery.inventory',   'brewery.openOrders',   'brewery.orderLine',   'distributor.deliveries',   'distributor.incomingOrders',   'distributor.inventory',   'distributor.openOrders',   'distributor.orderLine',   'performanceControlling.breweryInventory',   'performanceControlling.distributorInventory',   'performanceControlling.retailerCostAcc',   'performanceControlling.retailerInventory',   'performanceControlling.supplyChainCostAcc',   'performanceControlling.wholesalerInventory',   'retailer.deliveries',   'retailer.incomingOrders',   'retailer.inventory',   'retailer.openOrders',   'retailer.orderLine',   'wholesaler.deliveries',   'wholesaler.incomingOrders',   'wholesaler.inventory',   'wholesaler.openOrders',   'wholesaler.orderLine'  ]
        self.flows = ['brewery.incomingDeliveryRate',   'brewery.incomingOrderRate',   'brewery.makingOrders',   'brewery.orderRate',   'brewery.outgoingDeliveryRate',   'brewery.sendingOrders',   'distributor.incomingDeliveryRate',   'distributor.incomingOrderRate',   'distributor.makingOrders',   'distributor.orderRate',   'distributor.outgoingDeliveryRate',   'distributor.sendingOrders',   'performanceControlling.accSupplyChainCost',   'performanceControlling.monthlyCostIn',   'retailer.incomingDeliveryRate',   'retailer.incomingOrderRate',   'retailer.makingOrders',   'retailer.orders',   'retailer.outgoingDeliveryRate',   'retailer.sendingOrders',   'wholesaler.incomingDeliveryRate',   'wholesaler.incomingOrderRate',   'wholesaler.makingOrders',   'wholesaler.orders',   'wholesaler.outgoingDeliveryRate',   'wholesaler.sendingOrders'  ]
        self.converters = ['brewery.actualOrder',   'brewery.actualProduction',   'brewery.backorder',   'brewery.converter1',   'brewery.deliveryDelay',   'brewery.deliveryPolicy',   'brewery.expectedOrder',   'brewery.incomingDelivery',   'brewery.incomingOrder',   'brewery.multiplayerModeOn',   'brewery.naiveOrderDecision',   'brewery.orderDecision',   'brewery.orderDelay',   'brewery.orderFromOrderLine',   'brewery.outgoingDelivery',   'brewery.production',   'brewery.singlePlayerSimplePolicyOn',   'brewery.sophisticatedOrderDecision',   'brewery.sophisticatedOrderDecisionOn',   'brewery.stockAdjustmentTime',   'brewery.surplus',   'brewery.targetSupplyLine',   'brewery.targetSupplyLineFactor',   'brewery.targetTotalStock',   'brewery.totalStock',   'brewery.weightOnBackorder',   'brewery.weightOnInventory',   'brewery.weightingOnSupplyLine',   'distributor.actualOrder',   'distributor.backorder',   'distributor.converter3',   'distributor.converter4',   'distributor.converter5',   'distributor.converter6',   'distributor.deliveryPolicy',   'distributor.expectedOrder',   'distributor.incomingDelivery',   'distributor.incomingOrder',   'distributor.multiplayerModeOn',   'distributor.naiveOrderDecision',   'distributor.order',   'distributor.orderDecision',   'distributor.orderDelay',   'distributor.orderFromOrderLine',   'distributor.outgoingDelivery',   'distributor.singlePlayerSimplePolicyOn',   'distributor.sophisticatedOrderDecision',   'distributor.sophisticatedOrderDecisionOn',   'distributor.stockAdjustmentTime',   'distributor.surplus',   'distributor.targetSupplyLine',   'distributor.targetSupplyLineFactor',   'distributor.totalStock',   'distributor.weightOnBackorder',   'distributor.weightOnInventory',   'distributor.weightingOnSupplyLine',   'performanceControlling.breweryBackorder',   'performanceControlling.breweryBackorderCost',   'performanceControlling.breweryCost',   'performanceControlling.breweryInventoryCost',   'performanceControlling.costPerItemInBackorder',   'performanceControlling.costPerItemInInventory',   'performanceControlling.distributorBackorderCost',   'performanceControlling.distributorCost',   'performanceControlling.distributorDeliveryShortfall',   'performanceControlling.distributorInventoryCost',   'performanceControlling.retailBackorder',   'performanceControlling.retailerBackorderCost',   'performanceControlling.retailerCost',   'performanceControlling.retailerInventoryCost',   'performanceControlling.supplyChainCost',   'performanceControlling.targetInventory',   'performanceControlling.wholesalerBackorder',   'performanceControlling.wholesalerBackorderCost',   'performanceControlling.wholesalerCost',   'performanceControlling.wholesalerInventoryCost',   'policySettings.deliveryDelay',   'policySettings.dynamicCustomerBehaviourOn',   'policySettings.gameModeOn',   'policySettings.multiplayerModeOn',   'policySettings.orderDelay',   'policySettings.riseInOrder',   'policySettings.sophisticatedOrderDecisionOn',   'policySettings.steadyStateOn',   'policySettings.stockAdjustmentTime',   'policySettings.targetInventory',   'policySettings.targetRetailerCost',   'policySettings.targetSupplyChainCost',   'policySettings.targetSupplyLineFactor',   'policySettings.targetSurplus',   'policySettings.weightingBackorder',   'policySettings.weightingInventory',   'policySettings.weightingOpenOrders',   'retailer.actualOrder',   'retailer.backorder',   'retailer.converter1',   'retailer.customerOrder',   'retailer.deliveryDelay',   'retailer.deliveryPolicy',   'retailer.deliveryRate',   'retailer.dynamicCustomerBehaviourOn',   'retailer.expectedOrder',   'retailer.incomingDelivery',   'retailer.incomingOrder',   'retailer.multiplayerModeOn',   'retailer.naiveOrderDecision',   'retailer.order',   'retailer.orderDecision',   'retailer.orderDelay',   'retailer.orderFromOrderLine',   'retailer.outgoingDelivery',   'retailer.riseInOrder',   'retailer.singlePlayerSimplePolicyOn',   'retailer.sophisticatedOrderDecision',   'retailer.sophisticatedOrderDecisionOn',   'retailer.steadyStateOn',   'retailer.stockAdjustmentTime',   'retailer.surplus',   'retailer.targetSupplyLine',   'retailer.targetTotalStock',   'retailer.totalStock',   'retailer.transitAveragingTime',   'retailer.unexpectedRiseInCustomerOrders',   'retailer.weightOnBackorder',   'retailer.weightOnInventory',   'retailer.weightingOnSupplyLine',   'wholesaler.actualOrder',   'wholesaler.backorder',   'wholesaler.converter2',   'wholesaler.converter3',   'wholesaler.converter4',   'wholesaler.converter5',   'wholesaler.deliveryDecision',   'wholesaler.expectedOrder',   'wholesaler.incomingDelivery',   'wholesaler.incomingOrder',   'wholesaler.multiplayerModeOn',   'wholesaler.naiveOrderDecision',   'wholesaler.order',   'wholesaler.orderDecision',   'wholesaler.orderDelay',   'wholesaler.orderFromOrderLine',   'wholesaler.outgoingDelivery',   'wholesaler.singlePlayerSimplePolicyOn',   'wholesaler.sophisticatedOrderDecision',   'wholesaler.sophisticatedOrderDecisionOn',   'wholesaler.stockAdjustmentTime',   'wholesaler.surplus',   'wholesaler.targetSupplyLine',   'wholesaler.targetTotalStock',   'wholesaler.totalStock',   'wholesaler.transitAveragingTime',   'wholesaler.weightOnBackorder',   'wholesaler.weightOnInventory',   'wholesaler.weightingOnSupplyLine'  ]
        self.gf = ['retailer.dynamicCustomerOrder'  ]
        self.constants= ['brewery.actualOrder',   'brewery.converter1',   'brewery.deliveryDelay',   'brewery.multiplayerModeOn',   'brewery.orderDelay',   'brewery.singlePlayerSimplePolicyOn',   'brewery.sophisticatedOrderDecisionOn',   'brewery.stockAdjustmentTime',   'brewery.targetSupplyLineFactor',   'brewery.weightOnBackorder',   'brewery.weightOnInventory',   'brewery.weightingOnSupplyLine',   'distributor.converter3',   'distributor.converter4',   'distributor.converter5',   'distributor.converter6',   'distributor.multiplayerModeOn',   'distributor.orderDelay',   'distributor.singlePlayerSimplePolicyOn',   'distributor.sophisticatedOrderDecisionOn',   'distributor.stockAdjustmentTime',   'distributor.targetSupplyLineFactor',   'distributor.weightOnBackorder',   'distributor.weightOnInventory',   'distributor.weightingOnSupplyLine',   'performanceControlling.breweryBackorder',   'performanceControlling.distributorDeliveryShortfall',   'performanceControlling.retailBackorder',   'performanceControlling.targetInventory',   'performanceControlling.wholesalerBackorder',   'retailer.converter1',   'retailer.deliveryDelay',   'retailer.deliveryRate',   'retailer.dynamicCustomerBehaviourOn',   'retailer.multiplayerModeOn',   'retailer.orderDelay',   'retailer.riseInOrder',   'retailer.singlePlayerSimplePolicyOn',   'retailer.sophisticatedOrderDecisionOn',   'retailer.steadyStateOn',   'retailer.stockAdjustmentTime',   'retailer.transitAveragingTime',   'retailer.weightOnBackorder',   'retailer.weightOnInventory',   'retailer.weightingOnSupplyLine',   'wholesaler.converter2',   'wholesaler.converter3',   'wholesaler.converter4',   'wholesaler.converter5',   'wholesaler.multiplayerModeOn',   'wholesaler.orderDelay',   'wholesaler.singlePlayerSimplePolicyOn',   'wholesaler.sophisticatedOrderDecisionOn',   'wholesaler.stockAdjustmentTime',   'wholesaler.transitAveragingTime',   'wholesaler.weightOnBackorder',   'wholesaler.weightOnInventory',   'wholesaler.weightingOnSupplyLine'  ]
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
        return self.starttime, self.stoptime, self.dt, 'Weeks', 'Euler'
    