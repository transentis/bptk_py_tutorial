from BPTK_Py import Agent

class Controlling(Agent):

    def initialize(self):

        self.agent_type = "controlling"
        self.state = "active"

        self._revenue=0
        self._salaries=0
        self.register_event_handler(["active"], "revenue", self.handle_revenue_event)
        self.register_event_handler(["active"], "salary", self.handle_salary_event)

        self.set_property("revenue", {"type": "Double", "value": 0.0})
        self.set_property("expenses", {"type": "Double", "value": 0.0})
        self.set_property("profit",{"type":"Double","value":0.0})
        self.set_property("cash",{"type":"Double","value":0.0})
        self.set_property("earnings",{"type":"Double","value":0.0})

    def handle_revenue_event(self,event):
        self._revenue = self._revenue + event.data["revenue"]

    def handle_salary_event(self,event):
        self._salaries = self._salaries + event.data["salary"]

    def act(self, time, round_no, step_no):
        self.model.points["cost.salaries"].append([time,self._salaries])
        self._salaries=0
        self.model.points["revenue.revenue"].append([time,self._revenue])
        self._revenue=0
        self.revenue = self.model.evaluate_equation("revenue.revenue",time)
        self.expenses = self.model.evaluate_equation("cost.expenses",time)
        self.profit = self.model.evaluate_equation("earnings.profit",time)
        self.earnings = self.model.evaluate_equation("earnings.earnings",time)
        self.cash = self.model.evaluate_equation("cash.cash",time)



