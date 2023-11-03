from BPTK_Py import Model
from BPTK_Py import sd_functions as sd
from .cash import Cash
from .revenue import Revenue
from .earnings import Earnings
from .cost import Cost
from .controlling import Controlling
from .projects import Projects

class EnterpriseDigitalTwinSD(Model):
    def __init__(self,abm_model):
        super().__init__(starttime=abm_model.starttime,stoptime=abm_model.starttime+(abm_model.stoptime-abm_model.starttime)/abm_model.dt, dt=1.0, name="EDT SD DSL")

        self.abm_model = abm_model

        cash = Cash(
            model = self,
            name = "cash"
        )
        
        revenue = Revenue(
            model = self,
            name = "revenue"
        )

        earnings = Earnings(
            model = self,
            name = "earnings"
        )

        cost = Cost(
            model = self,
            name = "cost"
        )

        projects = Projects(
            model = self,
            name = "projects"
        )

        controlling = Controlling(
            model = self,
            name = "controlling"
        )

        cash.initialize(revenue=revenue,cost=cost)
        revenue.initialize()
        earnings.initialize(cost=cost,revenue=revenue)
        cost.initialize()
        projects.initialize()
        controlling.initialize(revenue=revenue,earnings=earnings,projects=projects)
       
