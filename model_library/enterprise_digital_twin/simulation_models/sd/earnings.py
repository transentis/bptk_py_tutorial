from BPTK_Py import Module


class Earnings(Module):

    def initialize(self,revenue, cost):

        # stocks
        accumulated_earnings = self.stock("accumulated_earnings")

        # flows
        accumulated_earnings_in = self.biflow("accumulated_earnings_in")

        # converters
        earnings = self.converter("earnings")

        # equations
        earnings.equation=revenue.converter("revenue") - cost.converter("expenses")

        accumulated_earnings.initial_value = 0.0
        accumulated_earnings_in.equation=earnings       
        accumulated_earnings.equation = accumulated_earnings_in