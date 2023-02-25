from BPTK_Py import Agent

class Controlling(Agent):

    def initialize(self):

        self.agent_type = "controlling"
        self.state = "active"

        self._revenue=0.0
        self._salaries=0.0
        self._consultant_demand=0.0

        self.register_event_handler(["active"], "revenue", self.handle_revenue_event)
        self.register_event_handler(["active"], "salary", self.handle_salary_event)
        self.register_event_handler(["active"], "consultant_demand", self.handle_consultant_demand_event)

        self.set_property("revenue", {"type": "Double", "value": 0.0})
        self.set_property("expenses", {"type": "Double", "value": 0.0})
        self.set_property("earnings",{"type":"Double","value":0.0})
        self.set_property("cash",{"type":"Double","value":0.0})
        self.set_property("accumulated_earnings",{"type":"Double","value":0.0})
        self.set_property("consultant_demand",{"type":"Double","value":0.0})


    def reset_cache(self):
        self._revenue=0.0
        self._salaries=0.0
        self._consultant_demand=0.0

        self.revenue=0.0
        self.expenses=0.0
        self.earnings=0.0
        self.cash=0.0
        self.accumulated_earnings=0.0
        self.consultant_demand=0.0 


    def handle_revenue_event(self,event):
        self._revenue = self._revenue + event.data["revenue"]

    def handle_salary_event(self,event):
        self._salaries = self._salaries + event.data["salary"]
    
    def handle_consultant_demand_event(self,event):
        self._consultant_demand= self._consultant_demand + event.data["consultant_demand"]

    def act(self, time, round_no, step_no):
        self.model._exchange["salaries"][time]=self._salaries
        self._salaries=0.0
        self.model._exchange["revenue"][time]=self._revenue
        self._revenue=0.0
        self.consultant_demand=self._consultant_demand
        self._consultant_demand=0.0
        self.revenue = self.model.evaluate_equation("revenue.revenue",time)
        self.expenses = self.model.evaluate_equation("cost.expenses",time)
        self.earnings = self.model.evaluate_equation("earnings.earnings",time)
        self.accumulated_earnings = self.model.evaluate_equation("earnings.accumulated_earnings",time)
        self.cash = self.model.evaluate_equation("cash.cash",time)



