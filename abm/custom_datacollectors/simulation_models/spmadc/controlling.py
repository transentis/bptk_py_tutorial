from BPTK_Py import Agent


class Controlling(Agent):

    def initialize(self):

        self.agent_type = "controlling"
        self.state = "active"
        self.set_property("productivity", {"type": "Double", "value": 1})
        self.set_property("schedule_pressure", {"type": "Double", "value": 1})

    def act(self,time, round_no, step_no):
        self.productivity = self.model.productivity
        self.schedule_pressure = self.model.schedule_pressure


