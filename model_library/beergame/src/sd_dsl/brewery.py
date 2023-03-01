from BPTK_Py import sd_functions as sd
from .supplyChainModule import SupplyChainModule


class Brewery(SupplyChainModule):
    def __init__(self, model,name):
        super().__init__(model, name)

    def initialize(self, supplier, customer, policy_settings):
        super().initialize(supplier, customer, policy_settings)
        self.incoming_delivery_rate.equation = sd.delay(self.model,self.sending_orders,policy_settings.delivery_delay, 100.0)



