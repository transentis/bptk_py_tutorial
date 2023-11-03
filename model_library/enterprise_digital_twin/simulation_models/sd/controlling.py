from BPTK_Py import sd_functions as sd
from BPTK_Py import Module


class Controlling(Module):

    def initialize(self,revenue,earnings,projects):

        # constants
        days_per_month = self.constant("days_per_month")
        
        # converters
        avg_consulting_fee = self.converter("avg_consulting_fee")
        overall_avg_consulting_fee = self.converter("overall_avg_consulting_fee")

        consultant_capacity = self.converter("consultant_capacity")
        avg_utilization = self.converter("avg_utilization")
        overall_avg_utilization = self.converter("overall_avg_utilization")

        profit_margin = self.converter("profit_margin")
        overall_profit_margin = self.converter("overall_profit_margin")

        #stocks
        total_consultant_capacity = self.stock("total_consultant_capacity")

        #flows

        total_consultant_capacity_in = self.flow("total_consultant_capacity_in")
        
        # equations

        days_per_month.equation = 18.0

        avg_consulting_fee.equation = sd.If(projects.converter("consulting_effort")==0.0,0.0,revenue.converter("revenue")/(projects.converter("consulting_effort")*days_per_month))

        overall_avg_consulting_fee.equation = sd.If(projects.stock("total_consulting_effort")==0.0,0.0,revenue.stock("accumulated_revenue")/(projects.stock("total_consulting_effort")*days_per_month))

        total_consultant_capacity.initial_value = 0.0
        total_consultant_capacity.equation = total_consultant_capacity_in
        total_consultant_capacity_in.equation = consultant_capacity

        consultant_capacity.equation=self.model.function("get_consultant_capacity",lambda model,t:model.abm_model._exchange["consultant_capacity"][t] if t>=self.model.starttime else 0.0)()

        avg_utilization.equation = sd.If(consultant_capacity==0.0,0.0,projects.converter("consulting_effort")/consultant_capacity)
        overall_avg_utilization.equation = sd.If(total_consultant_capacity==0.0,0.0,projects.stock("total_consulting_effort")/total_consultant_capacity)

        profit_margin.equation = sd.If(revenue.converter("revenue")==0.0,0.0,earnings.converter("earnings")/revenue.converter("revenue"))

        overall_profit_margin.equation= sd.If(revenue.stock("accumulated_revenue")==0.0,0.0,earnings.stock("accumulated_earnings")/revenue.stock("accumulated_revenue"))

        
