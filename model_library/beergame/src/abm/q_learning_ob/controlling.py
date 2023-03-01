from ..base.controlling import Controlling

class ControllingQlOB(Controlling):

    def initialize(self):
        super().initialize()
        self.set_property("supply_chain_reward", {"type": "Integer", "value": 0})
        self.register_event_handler(["active"], "supply_chain_reward", self.handle_supply_chain_reward_event)

    def begin_episode(self, episode_no):
        self.supply_chain_cost = 0
        self.supply_chain_reward = 0

    def handle_supply_chain_reward_event(self, event):
        self.supply_chain_reward += event.data["supply_chain_reward"]

