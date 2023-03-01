from BPTK_Py import sd_functions as sd
from BPTK_Py import Module

class SupplyChainModule(Module):
    def __init__(self, model, name):
        super().__init__(model, name)
        
        # Exports for supply chain
        self.sending_orders = self.flow("sending_orders")
        self.outgoing_deliveries = self.flow("outgoing_deliveries")
        
        # Exports for performance controlling
        
        self.inventory = self.stock("inventory")
        self.backorder = self.converter("backorder")
        
        # Exports for subclasses
        self.incoming_delivery_rate = self.converter("incoming_delivery_rate")

    def initialize(self, supplier, customer, policy_settings):
        # Stocks

        open_orders = self.stock("open_orders")
        deliveries_made = self.stock("deliveries_made")
        orders_received = self.stock("orders_received")

        # Flows

        incoming_orders = self.flow("incoming_orders")
        outgoing_orders = self.flow("outgoing_orders")
        incoming_deliveries = self.flow("incoming_deliveries")

        # Converters

        outgoing_delivery_rate = self.converter("outgoing_delivery_rate")
        incoming_order_rate = self.converter("incoming_order_rate")
        total_stock = self.converter("total_stock")
        surplus = self.converter("surplus")
        order_decision = self.converter("order_decision")
        naive_order_decision = self.converter("naive_order_decision")
        sophisticated_order_decision = self.converter("sophisticated_order_decision")
        target_supply_line = self.converter("target_supply_line")

        # Initial Values

        open_orders.initial_value = 200.0
        self.inventory.initial_value = 400.0
        deliveries_made.initial_value = 0.0
        incoming_orders.initial_value = 0.0

        # Equations

        ## Inflows and Outflows

        open_orders.equation = outgoing_orders-incoming_deliveries
        self.inventory.equation = incoming_deliveries-self.outgoing_deliveries
        deliveries_made.equation = self.outgoing_deliveries
        orders_received.equation = incoming_orders

        ## Flows and Rates
        surplus.equation = self.inventory - self.backorder
        self.backorder.equation = sd.max(orders_received-deliveries_made,0)

        incoming_orders.equation = incoming_order_rate
        incoming_order_rate.equation = customer.sending_orders

        outgoing_orders.equation = order_decision

        incoming_deliveries.equation = self.incoming_delivery_rate

        self.incoming_delivery_rate.equation = sd.delay(self.model,supplier.outgoing_deliveries,policy_settings.delivery_delay,100.0) if supplier is not None else None

        self.outgoing_deliveries.equation = outgoing_delivery_rate
        outgoing_delivery_rate.equation = sd.min(self.backorder+incoming_orders,self.inventory+incoming_deliveries)

        self.sending_orders.equation = sd.delay(self.model,order_decision,policy_settings.order_delay, 100.0)

        ## Decision Policies

        target_supply_line.equation = incoming_order_rate*(policy_settings.order_delay+policy_settings.delivery_delay)

        ### Order Decision

        order_decision.equation = sd.If(policy_settings.sophisticated_order_decision_on == 1.0, sophisticated_order_decision,naive_order_decision)

        ### Naive Order Decision

        naive_order_decision.equation = sd.max(policy_settings.target_inventory - self.inventory + self.backorder + incoming_order_rate,0.0)

        ### Sophisticated Order Decision

        sophisticated_order_decision.equation = 1.0*sd.round((sd.max(incoming_order_rate+(policy_settings.target_inventory-self.inventory + policy_settings.include_supply_line_on*(target_supply_line-open_orders))/policy_settings.inventory_adjustment_time,0.0)),0)














