from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Cash(Module):

    def initialize(self,revenue,cost):

        # stocks
        cash = self.stock("cash")

        #flows

        cash_in = self.flow("cash_in")
        cash_out = self.flow("cash_out")

        # converters

        cash_flow = self.converter("cash_flow")
        cash_flow.equation = cash_in - cash_out

        #equations

        cash.initial_value = 0.0
        cash.equation = cash_in-cash_out

        cash_in.equation = revenue.flow("receivables_out")
        cash_out.equation = cost.converter("expenses")
