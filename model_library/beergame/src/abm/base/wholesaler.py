from .supplyChainAgent import SupplyChainAgent


class Wholesaler(SupplyChainAgent):

    def initialize(self):
        super().initialize()
        self.agent_type = "wholesaler"
        self.supplier = "distributor"
        self.customer = "retailer"


