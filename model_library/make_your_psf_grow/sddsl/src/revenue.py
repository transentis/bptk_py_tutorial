from BPTK_Py import sd_functions as sd
from BPTK_Py import Module

class Revenue(Module):
    def __init__(self, model, name):
        super().__init__(model, name)

        # Exports
        self.collectingRevenue = self.flow("collectingRevenue")
    
    def initialize(self,projects):
        receivables = self.stock("receivables")
        makingRevenue = self.flow("makingRevenue")
        collectionTime = self.converter("collectionTime")
        revenue = self.converter("revenue")
        projectDeliveryFee = self.converter("projectDeliveryFee")

        receivables.initial_value = 160*17.6*2
        receivables.equation = makingRevenue-self.collectingRevenue
        projectDeliveryFee.equation = 17.6
        revenue.equation = projectDeliveryFee*projects.deliveringProjects
        makingRevenue.equation = revenue

        collectionTime.equation=2.0
        self.collectingRevenue.equation=sd.delay(self.model,makingRevenue,collectionTime,160*17.6)