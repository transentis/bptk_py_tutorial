from BPTK_Py import Agent
from BPTK_Py import Event


class Company(Agent):

    def act(self, time, time_step, step_num):
        self.model.random_events(
            "customer",
            self.model.customers_reached,
            lambda agent_id: Event("advert", self.id, agent_id)
        )

    def initialize(self):
        self.agent_type = "company"
        self.state = "company"
