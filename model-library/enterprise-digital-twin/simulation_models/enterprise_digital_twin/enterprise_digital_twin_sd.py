from BPTK_Py import sd_functions as sd

class EnterpriseDigitalTwinSD():
    def __init__(self,model):
        self.model = model

        # cash

        self.cash = model.stock("cash")
        self.cash_in = model.flow("cash_in")
        self.cash_out = model.flow("cash_out")
        self.cash_flow = model.converter("cash_flow")
        self.cash_flow.equation = self.cash_in - self.cash_out
        self.cash.initial_value = 0.0
        self.cash.equation=self.cash_in-self.cash_out

        # receivables

        self.receivables = model.stock("receivables")
        self.receivables.initial_value= 0.0
        self.receivables_in = model.flow("receivables_in")
        self.receivables_out = model.flow("receivables_out")
        self.collection_time = model.converter("collection_time")
        self.collection_time.equation = 2.0
        self.receivables_out.equation = sd.delay(self.model,self.receivables_in,self.collection_time,0.0)
        self.receivables.equation = self.receivables_in-self.receivables_out

        self.cash_in.equation = self.receivables_out

        self.salaries = model.converter("salaries")
        model.points["salaries"]=[]
        self.salaries.equation=sd.lookup(sd.time(),"salaries")

        self.cash_out.equation = self.salaries

        # revenue

        self.revenue = model.converter("revenue")
        model.points["revenue"]=[]
        self.revenue.equation = sd.lookup(sd.time(),"revenue")

        self.receivables_in.equation = self.revenue
        # expenses

        self.expenses = model.converter("expenses")
        self.expenses.equation = self.salaries

        # profit

        self.profit = model.converter("profit")
        self.profit.equation=self.revenue - self.expenses

        self.accumulated_profit = model.stock("accumulated_profit")
        self.accumulated_profit.initial_value = 0.0
        self.accumulated_profit_in = model.flow("accumulated_profit_in")
        self.accumulated_profit.equation = self.accumulated_profit_in
        self.accumulated_profit_in.equation=self.profit        
