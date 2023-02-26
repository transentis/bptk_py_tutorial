from BPTK_Py import Model

from .cash import Cash
from .cost import Cost
from .projects import Projects
from .revenue import Revenue
from .staff import Staff
from .kpi import Kpi

class Mypsfg(Model):
    def __init__(self):
        super().__init__(starttime=1.0,stoptime=24.0, dt=1.0, name="Make Your PSF Grow SD DSL")
                 
        ####
        # Step 1: create the modules
        ####

        staff = Staff(
            model=self,
            name="staff")

        cost = Cost(
            model=self,
            name="cost"
        )

        cash = Cash(
            model=self,
            name="cash"
        )

        revenue = Revenue(
            model=self,
            name="revenue"
        )

        projects = Projects(
            model=self,
            name="projects"
        )

        kpi = Kpi(
            model=self,
            name="kpi"
        )

        ####
        # Step 2: initialize the modules
        ###

        staff.initialize(kpi=kpi)
        projects.initialize(staff=staff)
        cost.initialize(staff=staff)
        cash.initialize(cost=cost,revenue=revenue)
        revenue.initialize(projects=projects)
        kpi.initialize(staff=staff,cash=cash,projects=projects)
        
      



 
