from BPTK_Py import Agent
from BPTK_Py import Event


class SupplyChainAgent(Agent):

    def __init__(self, agent_id, model, properties, order_strategy):
        super().__init__(agent_id=agent_id, model=model, properties=properties)
        self.order_strategy = order_strategy

    def initialize(self):
        self.state = "active"
        self.supplier = None
        self.customer = None
        self.register_event_handler(["active"], "delivery", self.handle_delivery_event)
        self.register_event_handler(["active"], "order", self.handle_order_event)
        # initialize properties
        self._initialize_properties()

    def _initialize_properties(self):
        # properties need for the simulation
        self.set_property("outgoing_orders", {"type": "Integer", "value": 600})
        self.set_property("outgoing_order", {"type": "Integer", "value": 100})
        self.set_property("outstanding_orders", {"type": "Integer", "value": 200})
        self.set_property("surplus", {"type": "Integer", "value": 400})
        self.set_property("backorder", {"type": "Integer", "value": 0})
        self.set_property("outgoing_deliveries", {"type": "Integer", "value": 0})
        self.set_property("outgoing_delivery", {"type": "Integer", "value": 100})
        self.set_property("incoming_delivery", {"type": "Integer", "value": 100})
        self.set_property("incoming_deliveries", {"type": "Integer", "value": 0})
        self.set_property("incoming_orders", {"type": "Integer", "value": 0})
        self.set_property("incoming_order", {"type": "Integer", "value": 100})
        self.set_property("inventory", {"type": "Integer", "value": 400})
        self.set_property("cost", {"type": "Integer", "value": 0})
        self.set_property("order_balance", {"type": "Integer", "value": 600})
        self.set_property("total_cost", {"type": "Double", "value": 0.0})
        self.set_property("target_cost", {"type": "Double", "value": 8500.0})
        self.set_property("target_surplus", {"type": "Double", "value": 250.0})
        self.order_strategy.initialize(self)

    def begin_episode(self, episode_no):
        self._initialize_properties()
        
    def handle_delivery_event(self, event):
        self.incoming_delivery = event.data["delivery"]

    def handle_order_event(self, event):
        self.incoming_order = event.data["order"]

    def deliver(self, time, sim_round, step):
        amount = min(self.inventory + self.incoming_delivery, self.backorder + self.incoming_order)
        self.model.broadcast_event(self.customer,
                                   lambda agent_id: Event("delivery", self.id, agent_id, {"delivery": amount}))
        self.outgoing_delivery = amount

    def calculate_order(self, time):
        return self.order_strategy.calculate_order(time)

    def order(self, time, sim_round, step):
        # this is the "typical" behaviour seen by users
        amount = self.calculate_order(time)
        self.model.broadcast_event(self.supplier, lambda agent_id: Event("order", self.id, agent_id, {"order": amount}))
        self.outgoing_order = amount

    def act(self, time, sim_round, step):
        # take care of deliveries and orders
        self.deliver(time, sim_round, step)
        self.order(time, sim_round, step)
        # update the stocks
        self.incoming_orders += self.incoming_order
        self.outgoing_deliveries += self.outgoing_delivery
        self.incoming_deliveries += self.incoming_delivery
        self.outgoing_orders += self.outgoing_order
        # update the KPIs
        self.outstanding_orders += self.outgoing_order-self.incoming_delivery
        self.backorder = self.incoming_orders - self.outgoing_deliveries
        self.inventory += self.incoming_delivery-self.outgoing_delivery
        self.surplus = self.inventory - self.backorder
        self.order_balance = self.outgoing_orders-self.incoming_orders
        # cost kpi
        self.cost = self.backorder * self.model.backorder_item_cost + max(self.inventory * self.model.inventory_item_cost, self.model.minimum_inventory_cost)
        self.total_cost += self.cost
       # send the cost to the controller (in this round)
        
        self.model.next_agent("controlling","active").receive_instantaneous_event(
                                   Event("cost", self.id, 0, {"cost": self.cost}))

