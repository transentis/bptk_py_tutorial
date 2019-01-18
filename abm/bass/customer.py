from BPTK_Py import Agent
from BPTK_Py import Event


class Customer(Agent):

    def handle_advert_event(self, event):
        if self.is_event_relevant(self.model.advertising_success):
            self.state = "currentCustomer"

    def handle_wom_event(self, event):
        if self.is_event_relevant(self.model.wom_success):
            self.state = "currentCustomer"

    def act(self, time, time_step, step_num):

        super().act(time, time_step, step_num)

        if self.state == "currentCustomer":
            self.model.random_events(
                "customer",
                self.model.wom_contact_rate,
                lambda agent_id: Event("wordOfMouth", self.id, agent_id)
            )

    def initialize(self):
        self.agent_type = "customer"
        self.state = "potentialCustomer"

        self.register_event_handler(
            ["potentialCustomer"],
            "advert",
            self.handle_advert_event
        )

        self.register_event_handler(
            ["potentialCustomer"],
            "wordOfMouth",
            self.handle_wom_event
        )
