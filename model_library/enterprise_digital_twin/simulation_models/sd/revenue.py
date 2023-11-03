from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Revenue(Module):

    def initialize(self):

        # stocks
        receivables = self.stock("receivables")
        accumulated_revenue = self.stock("accumulated_revenue")

        # flows
        receivables_in = self.flow("receivables_in")
        receivables_out = self.flow("receivables_out")
        collection_time = self.converter("collection_time")
        accumulated_revenue_in = self.converter ("accumulated_revenue_in")

        # converters
        revenue = self.converter("revenue")
        revenue_risk = self.converter("revenue_risk")
        
        # equations

        ## read data from abm model
        revenue.equation=self.model.function("get_revenue",lambda model,t:model.abm_model._exchange["revenue"][t] if t>=self.model.starttime else 0.0)() 
        revenue_risk.equation=self.model.function("get_revenue_risk",lambda model,t:model.abm_model._exchange["revenue_risk"][t] if t>=self.model.starttime else 0.0)()
        
        receivables.initial_value= 0.0
        collection_time.equation = 2.0
        receivables_out.equation = sd.delay(self.model,receivables_in,collection_time,0.0)
        receivables_in.equation = revenue
        receivables.equation = receivables_in-receivables_out

        accumulated_revenue.initial_value = 0.0
        accumulated_revenue.equation = accumulated_revenue_in
        accumulated_revenue_in.equation = revenue
        
