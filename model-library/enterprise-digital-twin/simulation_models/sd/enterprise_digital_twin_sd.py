from BPTK_Py import sd_functions as sd
from .cash import Cash
from .revenue import Revenue
from .earnings import Earnings
from .cost import Cost

class EnterpriseDigitalTwinSD():
    def __init__(self,model):
        self.model = model

        cash = Cash(
            model = self.model,
            name = "cash"
        )
        
        revenue = Revenue(
            model = self.model,
            name = "revenue"
        )

        earnings = Earnings(
            model = self.model,
            name = "earnings"
        )

        cost = Cost(
            model = self.model,
            name = "cost"
        )

        cash.initialize(revenue=revenue,cost=cost)
        revenue.initialize()
        earnings.initialize(cost=cost,revenue=revenue)
        cost.initialize()
       