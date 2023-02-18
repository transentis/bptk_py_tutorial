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
        
        self.points[self.fqn("salaries")]=[]
        
        self.salaries.equation=sd.lookup(sd.time(),self.fqn("salaries"))
        self.expenses.equation = self.salaries

