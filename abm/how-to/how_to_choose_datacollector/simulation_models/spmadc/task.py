from BPTK_Py import Agent
from BPTK_Py import log


class Task(Agent):

    def initialize(self):
        self.agent_type = "task"
        self.state = "open"

        self.set_property("remaining_effort", {"type": "Double", "value": 0})

        self.register_event_handler(["open"], "task_started", self.handle_started_event)
        self.register_event_handler(["in_progress"], "task_progress", self.handle_progress_event)

    def handle_started_event(self, event):

        self.remaining_effort = self.effort
        self.state = "in_progress"

    def handle_progress_event(self, event):

        self.remaining_effort = max(self.remaining_effort-event.data["progress"], 0)

        if self.remaining_effort == 0:
            self.state = "closed"



