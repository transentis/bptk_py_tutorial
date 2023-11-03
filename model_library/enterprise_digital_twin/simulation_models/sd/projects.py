from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Projects(Module):

    def initialize(self):

        # stocks

        total_consulting_effort = self.stock("total_consulting_effort")

        # flows

        total_consulting_effort_in = self.flow("total_consulting_effort_in")
        
        # converters
        consulting_effort = self.converter("consulting_effort")
                
        # equations

        

        ## read data from abm model
        consulting_effort.equation=self.model.function("get_consulting_effort",lambda model,t:model.abm_model._exchange["consulting_effort"][t] if t>=self.model.starttime else 0.0)()

        total_consulting_effort.initial_value = 0.0
        total_consulting_effort.equation = total_consulting_effort_in
        total_consulting_effort_in.equation = consulting_effort
