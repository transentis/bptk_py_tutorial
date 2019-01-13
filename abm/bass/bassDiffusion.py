from BPTK_Py import Model
from BPTK_Py.widgets import WidgetLoader
from .company import Company
from .customer import Customer

class BassDiffusion(Model):

        @property
        def wom_success(self):
                return self.get_property("womSuccess")["value"]

        @property
        def wom_contact_rate(self):
                return self.get_property("womContactRate")["value"]

        @property
        def advertising_budget(self):
                return self.get_property("advertisingBudget")["value"]

        @property
        def persons_reached_per_euro(self):
                return self.get_property("personsReachedPerEuro")["value"]

        @property
        def advertising_success(self):
                return self.get_property("advertisingSuccess")["value"]

        @property
        def customers_reached(self):
                return self.persons_reached_per_euro * self.advertising_budget

        def instantiate_model(self):
                self.register_agent_factory("company", lambda agent_id, scenario: Company(agent_id, scenario))
                self.register_agent_factory("customer", lambda agent_id, scenario: Customer(agent_id, scenario))

        def build_widget(self):
            widgetLoader = WidgetLoader()

            states = {1: "potentialCustomer", 2: "currentCustomer"}
            agents = [agent for agent in self.agents if isinstance(agent, Customer)]

            widgetLoader.create_widget("AgentStatusWidget", states=states, agents=agents)

            return widgetLoader
