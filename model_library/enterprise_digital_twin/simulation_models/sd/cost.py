from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Cost(Module):

    def initialize(self):

        #converters
        expenses = self.converter("expenses")
        salaries = self.converter("salaries")
        workplace_cost = self.converter("workplace_cost")
        fixed_cost = self.converter("fixed_cost")

        #stocks
        accumulated_expenses = self.stock("accumulated_expenses")

        #flows
        accumulated_expenses_in = self.flow("accumulated_expenses_in")
        
        salaries.equation=self.model.function("get_salaries",lambda model,t: model.abm_model._exchange["salaries"][t] if t>=self.model.starttime else 0.0)()
        workplace_cost.equation=self.model.function("get_workplace_cost",lambda model,t: model.abm_model._exchange["workplace_cost"][t] if t>=self.model.starttime else 0.0)()
        fixed_cost.equation=self.model.function("get_fixed_cost",lambda model,t: model.abm_model._exchange["fixed_cost"][t] if t>=self.model.starttime else 0.0)()
        
        expenses.equation = salaries+workplace_cost+fixed_cost

        accumulated_expenses_in.equation = expenses

        accumulated_expenses.initial_value= 0.0
        accumulated_expenses.equation = accumulated_expenses_in

