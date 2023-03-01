from ..base.orderStrategy import OrderStrategy


class SmartOrderStrategy(OrderStrategy):
    def calculate_order(self,time):
        if self.agent.model.ignore_backorder == 1:
            order = max(
                self.agent.incoming_order +
                self.agent.model.target_inventory -
                self.agent.inventory,
                0)
        elif self.agent.model.include_supply_line == 1:
            order = max(self.agent.incoming_order +
                self.agent.model.target_inventory -
                self.agent.inventory +
                2*self.agent.incoming_order -
                self.agent.outstanding_orders,
                0)
        elif self.agent.model.slow_inventory_adjustment == 1:
            order = int(max(
                self.agent.incoming_order +
                (self.agent.model.target_inventory -
                self.agent.inventory+
                2.0*self.agent.incoming_order -
                self.agent.outstanding_orders)/float(self.agent.model.inventory_adjustment_time),
                0))
        elif self.agent.model.order_balance == 1:
            order = int(max(
                self.agent.incoming_order+(2.0*self.agent.incoming_order+self.agent.model.target_inventory-self.agent.order_balance)/float(self.agent.model.inventory_adjustment_time),0))
        else:
            order = max(
                self.agent.incoming_order +
                self.agent.model.target_inventory -
                self.agent.inventory +
                self.agent.backorder,
                0)
        return order