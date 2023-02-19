from BPTK_Py import Module


class Earnings(Module):

    def __init__(self, model,name):
        super().__init__(model,name)


    def initialize(self,revenue, cost):

        # stocks
        accumulated_earnings = self.stock("accumulated_earnings")

        # flows
        accumulated_earnings_in = self.biflow("accumulated_earnings_in")

        # converters
        earnings = self.converter("earnings")

        # equations
        earnings.equation=revenue.revenue - cost.expenses

        accumulated_earnings.initial_value = 0.0
        accumulated_earnings_in.equation=earnings       
        accumulated_earnings.equation = accumulated_earnings_in