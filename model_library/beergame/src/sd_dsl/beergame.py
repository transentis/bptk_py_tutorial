from BPTK_Py import Model
from BPTK_Py import sd_functions as sd

from .brewery import Brewery
from .consumer import Consumer
from .performanceControlling import PerformanceControlling
from .policySettings import PolicySettings
from .supplyChainModule import SupplyChainModule

class Beergame(Model):
    def __init__(self):
        super().__init__(starttime=1.0,stoptime=24.0, dt=1.0, name="Beergame SD DSL")
        
         
        ####
        # Step 1: create the modules
        ####
        

        # the supply chain modules
        
        consumer = Consumer(
            model=self,
            name="consumer")

        retailer = SupplyChainModule(
            model=self,
            name="retailer")

        wholesaler = SupplyChainModule(
            model=self,
            name="wholesaler")

        distributor = SupplyChainModule(
            model=self,
            name="distributor"
        )

        brewery = Brewery(
            model=self,
            name="brewery")
        
        # modules for settings and controlling
        
        policy_settings = PolicySettings(
            model=self,
            name="policy_settings"
        )

        performance_controlling = PerformanceControlling(
            model=self,
            name="performance_controlling"
        )

        
        ####
        # Step 2: initialize the modules
        ###
        
        consumer.initialize(policy_settings=policy_settings)
        retailer.initialize(supplier=wholesaler,customer=consumer,policy_settings=policy_settings)
        wholesaler.initialize(supplier=distributor, customer=retailer, policy_settings=policy_settings)
        distributor.initialize(supplier=brewery, customer=wholesaler, policy_settings=policy_settings)
        brewery.initialize(supplier=None, customer=distributor, policy_settings=policy_settings)
        performance_controlling.initialize(brewery=brewery,distributor=distributor,wholesaler=wholesaler,retailer=retailer,policy_settings=policy_settings)




