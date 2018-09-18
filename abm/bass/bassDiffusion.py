from BPTK_Py import Model


class BassDiffusion(Model):

    def __init__(self, model, data_collector, schedule):
        super().__init__(model, data_collector, schedule)

        self.WOM_SUCCESS = 0
        self.WOM_CONTACT_RATE = 0
        self.ADVERTISING_BUDGET = 0
        self.PERSONS_REACHED_PER_EURO = 0
        self.ADVERTISING_SUCCESS = 0
        self.CUSTOMERS_REACHED = 0

    def configure(self, config):
        super().configure(config)

        self.WOM_SUCCESS = self.get_property("womSuccess")["value"]
        self.WOM_CONTACT_RATE = self.get_property("womContactRate")["value"]
        self.ADVERTISING_BUDGET = self.get_property("advertisingBudget")["value"]
        self.PERSONS_REACHED_PER_EURO = self.get_property("personsReachedPerEuro")["value"]
        self.ADVERTISING_SUCCESS = self.get_property("advertisingSuccess")["value"]
        self.CUSTOMERS_REACHED = self.PERSONS_REACHED_PER_EURO * self.ADVERTISING_BUDGET
