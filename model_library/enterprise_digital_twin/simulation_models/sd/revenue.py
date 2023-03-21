from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Revenue(Module):

    def initialize(self):

        # stocks
        receivables = self.stock("receivables")

        # flows
        receivables_in = self.flow("receivables_in")
        receivables_out = self.flow("receivables_out")
        collection_time = self.converter("collection_time")

        # converters
        revenue = self.converter("revenue")
        
        # equations
        revenue.equation=self.model.function("get_revenue",lambda model,t:model._exchange["revenue"][t] if t>0 else 0.0)()
        receivables.initial_value= 0.0
        collection_time.equation = 2.0
        receivables_out.equation = sd.delay(self.model,receivables_in,collection_time,0.0)
        receivables_in.equation = revenue
        receivables.equation = receivables_in-receivables_out

