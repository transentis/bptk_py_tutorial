from BPTK_Py import sd_functions as sd
from BPTK_Py import Module

class Cash(Module):
    def __init__(self, model, name):
        super().__init__(model, name)
        self.cashFlow = self.converter("cashFlow")
        
    
    def initialize(self,cost,revenue):
        cash = self.stock("cash")
        cashIn = self.flow("cashIn")
        cashOut= self.flow("cashOut")
        minimumCash = self.converter("minimumCash")
        easyTargetCash = self.converter("easyTargetCash")
        expertTargetCash = self.converter("expertTargetCash")

        cash.initial_value=1000.0
        cashIn.equation=revenue.collectingRevenue
        cashOut.equation = cost.cost
        cash.equation = cashIn-cashOut
        self.cashFlow.equation = cashIn -cashOut
        minimumCash.equation = 23463.0
        easyTargetCash.equation = 30000.0
        expertTargetCash.equation = 40000.0