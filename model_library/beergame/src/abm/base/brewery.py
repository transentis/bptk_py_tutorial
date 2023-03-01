from .supplyChainAgent import SupplyChainAgent
from BPTK_Py import DelayedEvent


class Brewery(SupplyChainAgent):

    def initialize(self):
        super().initialize()
        self.agent_type = "brewery"
        self.supplier = "brewery"
        self.customer = "distributor"

    def order(self, time, sim_round, step):
        # this is the "typical" behaviour seen by users
        amount = self.calculate_order(time)
        self.model.broadcast_event(self.supplier, lambda agent_id: DelayedEvent("delivery", self.id, agent_id, delay=1, data={"delivery": amount}))
        self.outgoing_order = amount

