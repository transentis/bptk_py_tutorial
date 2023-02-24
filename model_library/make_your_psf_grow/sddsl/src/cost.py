from BPTK_Py import sd_functions as sd
from BPTK_Py import Module

class Cost(Module):
    def __init__(self, model, name):
        super().__init__(model, name)
        #Exports
        self.cost = self.converter("cost")
    
    def initialize(self,staff):
        staffSalary = self.converter("staffSalary")
        workplaceCost = self.converter("workplaceCost")
        staffCost = self.converter("staffCost")
        overheadCost = self.converter("overheadCost")

        workplaceCost.equation=1.0
        staffSalary.equation = 80.0/12
        overheadCost.equation = 306.0
        staffCost.equation = staff.professionalStaff*(workplaceCost+staffSalary)
        self.cost.equation=staffCost+overheadCost
