from BPTK_Py import Agent
from BPTK_Py import Event
from .events import Events
from .customer import Customer


class Company(Agent):
    TYPE = "company"

    def act(self, time, time_step, step_num):
        self.sim.random_events(
            Customer.TYPE,
            self.sim.CUSTOMERS_REACHED,
            lambda agent_id: Event(Events.ADVERT, self.id, agent_id)
        )

    def initialize(self):
        self.agent_type = Company.TYPE
        self.state = "company"
