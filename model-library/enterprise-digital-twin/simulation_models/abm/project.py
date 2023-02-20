from BPTK_Py import Agent
from BPTK_Py import Event

class Project(Agent):

    def initialize(self):
        self.agent_type = "project"
        self.state = "acquired"

        self.set_property("remaining_effort", {"type": "Double", "value": 0.0})
        self.set_property("staff", {"type": "Double", "value": 0.0})

        self.register_event_handler(["ready"], "project_started", self.handle_started_event)
        self.register_event_handler(["started"], "project_joined", self.handle_joined_event)
        self.register_event_handler(["started"], "project_progress", self.handle_progress_event)
        self.register_event_handler(["fully_staffed"], "project_progress", self.handle_progress_event)

        self._effort_spent=0


    def reset_cache(self):
        self._effort_spent=0
        self.state="acquired"
        self.remaning_effort=0.0
        self.staff=0.0

    def handle_started_event(self, event):
        self.remaining_effort = self.effort
        self.staff = self.staff+1.0

        if self.staff == self.consultants:
            self.state = "fully_staffed"
        else:
            self.state = "started"

    def handle_joined_event(self, event):
        self.staff = self.staff+1.0
        if self.staff == self.consultants:
            self.state = "fully_staffed"


    def handle_progress_event(self, event):
        self.remaining_effort = max(self.remaining_effort-event.data["progress"], 0)
        
        self._effort_spent=self._effort_spent + event.data["progress"]

        if self.remaining_effort <= 0:
            self.state = "completed"

    def act(self, time, round_no, step_no):

        controlling = self.model.next_agent("controlling", "active")
        if controlling:
            controlling.receive_instantaneous_event(Event("revenue", self.id, controlling.id,{"revenue":self._effort_spent*self.billing_rate}))
        self._effort_spent=0
    
        if self.state=="acquired" and time*1.0==self.start_time:
            self.state="ready"
            if controlling:
                controlling.receive_instantaneous_event(Event("consultant_demand", self.id, controlling.id,{"consultant_demand":self.consultants-self.staff}))




