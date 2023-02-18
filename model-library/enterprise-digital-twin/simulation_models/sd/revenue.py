from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Revenue(Module):

    def __init__(self, model,name):
        super().__init__(model,name)

        # cash exports
        self.receivables_out = self.flow("receivables_out")

        # earnings exports
        self.revenue = self.converter("revenue")

    def initialize(self):

        # stocks
        receivables = self.stock("receivables")

        # flows
        receivables_in = self.flow("receivables_in")
        collection_time = self.converter("collection_time")

        # converters

        # equations
        self.points[self.fqn("revenue")]=[]
        self.revenue.equation=sd.lookup(sd.time(),self.fqn("revenue"))
        receivables.initial_value= 0.0
        collection_time.equation = 2.0
        self.receivables_out.equation = sd.delay(self.model,receivables_in,collection_time,0.0)
        receivables_in.equation = self.revenue
        receivables.equation = receivables_in-self.receivables_out

