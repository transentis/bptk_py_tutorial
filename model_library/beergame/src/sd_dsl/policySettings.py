from BPTK_Py import Module


class PolicySettings(Module):
    
    def __init__(self, model, name):
        super().__init__(model, name)
        # constants

        self.target_inventory = self.constant("target_inventory")
        self.target_retailer_cost = self.constant("target_retailer_cost")
        self.target_supply_chain_cost = self.constant("target_supply_chain_cost")
        self.target_surplus = self.constant("target_surplus")

        self.inventory_adjustment_time = self.constant("inventory_adjustment_time")

        self.include_supply_line_on = self.constant("include_supply_line_on")
        self.steady_state_on = self.constant("steady_state_on")
        self.sophisticated_order_decision_on = self.constant("sophisticated_order_decision_on")

        self.order_delay = self.constant("order_delay")
        self.delivery_delay = self.constant("delivery_delay")
        self.rise_in_consumer_order = self.constant("rise_in_consumer_order")

        # Equations

        self.target_inventory.equation = 400.0
        self.target_retailer_cost.equation = 8300.0
        self.target_supply_chain_cost.equation = 29300.0
        self.target_surplus.equation = 250.0

        self.inventory_adjustment_time.equation = 8.0

        self.include_supply_line_on.equation = 0.0
        self.steady_state_on.equation = 0.0
        self.sophisticated_order_decision_on.equation = 0.0

        self.order_delay.equation = 1.0
        self.delivery_delay.equation = 1.0
        self.rise_in_consumer_order.equation = 300.0





