from BPTK_Py import Agent
from BPTK_Py import Event
from .events import Events


class Customer(Agent):

    class States:
        POTENTIAL_CUSTOMER="potentialCustomer"
        CURRENT_CUSTOMER="currentCustomer"

    states = States()

    TYPE = "customer"

    def handle_advert_event(self, event):
        if self.is_event_relevant(self.sim.ADVERTISING_SUCCESS):
            self.state = Customer.states.CURRENT_CUSTOMER

    def handle_wom_event(self, event):
        if self.is_event_relevant(self.sim.WOM_SUCCESS):
            self.state = Customer.states.CURRENT_CUSTOMER

    def act(self, time, time_step, step_num):

        super().act(time, time_step, step_num)

        if self.state == Customer.states.CURRENT_CUSTOMER:
            self.sim.random_events(
                Customer.TYPE,
                self.sim.WOM_CONTACT_RATE,
                lambda agent_id: Event(Events.WOM, self.id, agent_id)
            )

    def initialize(self):
        self.agent_type = Customer.TYPE
        self.state = Customer.states.POTENTIAL_CUSTOMER

        self.register_event_handler(
            [Customer.states.POTENTIAL_CUSTOMER],
            Events.ADVERT,
            self.handle_advert_event
        )

        self.register_event_handler(
            [Customer.states.POTENTIAL_CUSTOMER],
            Events.WOM,
            self.handle_wom_event
        )
