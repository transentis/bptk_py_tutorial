from BPTK_Py import sd_functions as sd
from BPTK_Py import Module

class Consumer(Module):

    def __init__(self, model, name):
        super().__init__(model,name)

        # Exports
        self.sending_orders = self.converter("sending_orders")

    def initialize(self, policy_settings):
        # Equations
        self.sending_orders.equation = 100.0 + sd.If(policy_settings.steady_state_on == 0.0,1.0,0.0)*sd.step(policy_settings.rise_in_consumer_order,1.0)


