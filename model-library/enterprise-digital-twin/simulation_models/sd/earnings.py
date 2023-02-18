from BPTK_Py import Module


class Earnings(Module):

    def __init__(self, model,name):
        super().__init__(model,name)


    def initialize(self,revenue, cost):

        # stocks
        earnings = self.stock("earnings")

        # flows
        earnings_in = self.flow("earnings_in")

        # converters
        profit = self.converter("profit")

        # equations
        profit.equation=revenue.revenue - cost.expenses

        earnings.initial_value = 0.0
        earnings_in.equation=profit        
        earnings.equation = earnings_in