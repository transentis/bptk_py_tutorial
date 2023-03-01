from BPTK_Py import Agent
from BPTK_Py import Event


class Consumer(Agent):

    def initialize(self):
        self.agent_type = "consumer"
        self.state = "active"

        self.set_property("outstanding_orders", {"type": "Integer", "value": 0})
        self.set_property("outgoing_order", {"type": "Integer", "value": 0})
        self.set_property("outgoing_orders", {"type": "Integer", "value": 0})
        self.set_property("incoming_delivery", {"type": "Integer", "value": 0})
        self.set_property("incoming_deliveries", {"type": "Integer", "value": 0})

        self.supplier = "retailer"

        self.register_event_handler(["active"], "delivery", self.handle_delivery_event)

    def handle_delivery_event(self, event):
        self.incoming_delivery = event.data["delivery"]

    def order(self, time, sim_round, step):
        amount = self.weekly_order if time > 1 else 100

        self.model.next_agent(self.supplier,"active").receive_instantaneous_event(Event("order", self.id, 0, {"order": amount}))
        # self.model.broadcast_event(self.supplier, lambda agent_id: Event("order", self.id, agent_id, {"order": amount}))
        self.outgoing_order = amount

    def act(self, time, sim_round, step):
        self.order(time, sim_round, step)
        self.incoming_deliveries += self.incoming_delivery
        self.outgoing_orders += self.outgoing_order
        self.outstanding_orders = self.outgoing_orders-self.incoming_deliveries
