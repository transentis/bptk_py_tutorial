from .supplyChainAgent import SupplyChainAgent


class Retailer(SupplyChainAgent):

    def initialize(self):
        super().initialize()
        self.agent_type = "retailer"
        self.supplier = "wholesaler"
        self.customer = "consumer"




