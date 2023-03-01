from BPTK_Py import Agent


class Controlling(Agent):

    def initialize(self):
        self.agent_type = "controlling"
        self.state = "active"
        self.set_property("supply_chain_cost", {"type": "Integer", "value": 0})
        self.set_property("target_supply_chain_cost", {"type": "Integer", "value": 30100})
        self.register_event_handler(["active"], "cost", self.handle_cost_event)

    def handle_cost_event(self, event):
        self.supply_chain_cost += event.data["cost"]


