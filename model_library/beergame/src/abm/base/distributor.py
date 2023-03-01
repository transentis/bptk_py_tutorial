from .supplyChainAgent import SupplyChainAgent


class Distributor(SupplyChainAgent):

    def  initialize(self):
        super().initialize()
        self.agent_type = "distributor"
        self.supplier = "brewery"
        self.customer = "wholesaler"




