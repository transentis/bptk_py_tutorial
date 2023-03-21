from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Cost(Module):

    def initialize(self):

        #converters
        expenses = self.converter("expenses")
        salaries = self.converter("salaries")
        
        salaries.equation=self.model.function("get_salaries",lambda model,t: model._exchange["salaries"][t] if t>0.0 else 0.0)()
        expenses.equation = salaries

