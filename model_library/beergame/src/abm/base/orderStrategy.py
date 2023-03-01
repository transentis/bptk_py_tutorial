class OrderStrategy:
    def __init__(self):
        self.agent = None

    def calculate_order(self, time):
        pass

    def initialize(self, agent):
        self.agent = agent


class TypicalOrderStrategy(OrderStrategy):
    def calculate_order(self, time):
        return max(
            self.agent.incoming_order +
            self.agent.model.target_inventory -
            self.agent.inventory +
            self.agent.backorder,
            0)


