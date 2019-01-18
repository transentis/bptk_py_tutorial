from BPTK_Py import Model
from BPTK_Py.widgets import WidgetLoader
from .company import Company
from .customer import Customer

class BassDiffusion(Model):

        @property
        def customers_reached(self):
                 return self.persons_reached_per_euro * self.advertising_budget

        def instantiate_model(self):
                self.register_agent_factory("company", lambda agent_id, model, properties: Company(agent_id, model, properties))
                self.register_agent_factory("customer", lambda agent_id, model, properties: Customer(agent_id, model, properties))

        def build_widget(self):
            widget_loader = WidgetLoader()

            states = {1: "potentialCustomer", 2: "currentCustomer"}
            agents = [agent for agent in self.agents if isinstance(agent, Customer)]

            widget_loader.create_widget("AgentStatusWidget", states=states, agents=agents)

            return widget_loader
