from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Cost(Module):

    def __init__(self, model,name):
        super().__init__(model,name)

        # earnings export
        self.expenses = self.converter("expenses")
       
        # cash exports
        self.salaries = self.converter("salaries")

    def initialize(self):

        #converters
        
        self.salaries.equation=self.model.function("get_salaries",lambda model,t: model._exchange["salaries"][t] if t>0.0 else 0.0)()
        self.expenses.equation = self.salaries

