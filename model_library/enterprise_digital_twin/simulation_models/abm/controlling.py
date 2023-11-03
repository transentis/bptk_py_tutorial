from BPTK_Py import Agent

class Controlling(Agent):

    def initialize(self):

        self.agent_type = "controlling"
        self.state = "active"

        self._revenue = 0.0
        self._revenue_risk = 0.0
        self._salaries = 0.0
        self._workplace_cost = 0.0
        self._consultant_demand = 0.0
        self._consultant_capacity = 0.0
        self._consulting_effort = 0.0
        
        self.register_event_handler(["active"], "revenue", self.handle_revenue_event)
        self.register_event_handler(["active"], "consultant_cost", self.handle_consultant_cost_event)
        self.register_event_handler(["active"], "consultant_demand", self.handle_consultant_demand_event)
        self.register_event_handler(["active"], "consultant_capacity", self.handle_consultant_capacity_event)
        self.register_event_handler(["active"], "consulting_effort", self.handle_consulting_effort_event)
        self.register_event_handler(["active"], "count_project", self.handle_count_project_event)

        self.set_property("revenue", {"type": "Double", "value": 0.0})
        self.set_property("projects", {"type": "Double", "value": 0.0})
        self.set_property("revenue_risk", {"type": "Double", "value": 0.0})
        self.set_property("expenses", {"type": "Double", "value": 0.0})
        self.set_property("earnings",{"type":"Double","value":0.0})
        self.set_property("cash",{"type":"Double","value":0.0})
        self.set_property("cash_flow",{"type":"Double","value":0.0})
        self.set_property("accumulated_earnings",{"type":"Double","value":0.0})
        self.set_property("accumulated_revenue",{"type":"Double","value":0.0})
        self.set_property("accumulated_expenses",{"type":"Double","value":0.0})
        self.set_property("consultant_demand",{"type":"Double","value":0.0})
        self.set_property("consultant_capacity",{"type":"Double","value":0.0})
        self.set_property("consultant_capacity_fte",{"type":"Double","value":0.0})
        self.set_property("avg_consulting_fee",{"type":"Double","value":0.0})
        self.set_property("overall_avg_consulting_fee",{"type":"Double","value":0.0})
        self.set_property("avg_utilization",{"type":"Double","value":0.0})
        self.set_property("overall_avg_utilization",{"type":"Double","value":0.0})
        self.set_property("profit_margin",{"type":"Double","value":0.0})
        self.set_property("overall_profit_margin",{"type":"Double","value":0.0})


    def reset_cache(self):
        self._revenue = 0.0
        self._revenue_risk = 0.0
        self._salaries = 0.0
        self._workplace_cost = 0.0
        self._consultant_demand = 0.0
        self._consultant_capacity = 0.0
        self._consulting_effort = 0.0

        self.revenue = 0.0
        self.projects = 0.0
        self.revenue_risk = 0.0
        self.expenses = 0.0
        self.earnings = 0.0
        self.cash = 0.0
        self.cash_flow = 0.0
        self.accumulated_earnings = 0.0
        self.accumulated_revenue = 0.0
        self.accumulated_expenses = 0.0
        self.consultant_demand = 0.0
        self.consultant_capacity = 0.0
        self.consultant_capacity_fte = 0.0
        self.avg_consulting_fee = 0.0
        self.overall_avg_consulting_fee = 0.0
        self.avg_utilization = 0.0
        self.overall_avg_utilization = 0.0
        self.profit_margin = 0.0
        self.overall_profit_margin = 0.0
        self.projects = 0.0
        


    def handle_revenue_event(self,event):
        self._revenue +=  event.data["revenue"]
        self._revenue_risk += event.data["revenue"]*event.data["revenue_risk"]

    def handle_consultant_cost_event(self,event):
        self._salaries +=  event.data["salary"]
        self._workplace_cost += event.data["workplace_cost"]
    
    def handle_consultant_demand_event(self,event):
        self._consultant_demand += event.data["consultant_demand"]

    def handle_consulting_effort_event(self,event):
        self._consulting_effort += event.data["effort_delivered"]

    def handle_consultant_capacity_event(self,event):
        self._consultant_capacity += event.data["capacity"]
    
    def handle_count_project_event(self,event):
        self.projects += event.data["count"]

    def act(self, time, round_no, step_no):
        
        self.model._exchange["salaries"][self.model.sd_time(time)] = self._salaries
        self._salaries = 0.0

        self.model._exchange["workplace_cost"][self.model.sd_time(time)] = self._workplace_cost
        self._workplace_cost = 0.0
        
        self.model._exchange["fixed_cost"][self.model.sd_time(time)] = self.model.fixed_cost*self.model.dt

        self.model._exchange["revenue"][self.model.sd_time(time)] = self._revenue
        self.model._exchange["revenue_risk"][self.model.sd_time(time)] = (self._revenue_risk / self._revenue) if self._revenue > 0.0  else 0.0
        self._revenue = 0.0
        self._revenue_risk = 0.0

        self.model._exchange["consulting_effort"][self.model.sd_time(time)] = self._consulting_effort
        self._consulting_effort = 0.0
        
        self.consultant_demand = self._consultant_demand
        self._consultant_demand = 0.0

        self.consultant_capacity = self._consultant_capacity
        self.consultant_capacity_fte = self._consultant_capacity/self.model.dt
        self.model._exchange["consultant_capacity"][self.model.sd_time(time)] = self._consultant_capacity
        self._consultant_capacity = 0.0


        self.revenue = self.model.sd_model.evaluate_equation("revenue.revenue",self.model.sd_time(time))
        self.accumulated_revenue = self.model.sd_model.evaluate_equation("revenue.accumulated_revenue",self.model.sd_time(time))
        self.revenue_risk = self.model.sd_model.evaluate_equation("revenue.revenue_risk",self.model.sd_time(time))

        self.expenses = self.model.sd_model.evaluate_equation("cost.expenses",self.model.sd_time(time))
        self.accumulated_expenses = self.model.sd_model.evaluate_equation("cost.accumulated_expenses",self.model.sd_time(time))
        
        self.earnings = self.model.sd_model.evaluate_equation("earnings.earnings",self.model.sd_time(time))
        self.accumulated_earnings = self.model.sd_model.evaluate_equation("earnings.accumulated_earnings",self.model.sd_time(time))


        self.cash = self.model.sd_model.evaluate_equation("cash.cash",self.model.sd_time(time))
        self.cash_flow = self.model.sd_model.evaluate_equation("cash.cash_flow",self.model.sd_time(time))

        self.avg_consulting_fee = self.model.sd_model.evaluate_equation("controlling.avg_consulting_fee",self.model.sd_time(time))
        self.overall_avg_consulting_fee = self.model.sd_model.evaluate_equation("controlling.overall_avg_consulting_fee",self.model.sd_time(time))

        self.avg_utilization = self.model.sd_model.evaluate_equation("controlling.avg_utilization",self.model.sd_time(time))
        self.overall_avg_utilization = self.model.sd_model.evaluate_equation("controlling.overall_avg_utilization",self.model.sd_time(time))

        self.profit_margin = self.model.sd_model.evaluate_equation("controlling.profit_margin",self.model.sd_time(time))
        self.overall_profit_margin = self.model.sd_model.evaluate_equation("controlling.overall_profit_margin",self.model.sd_time(time))

