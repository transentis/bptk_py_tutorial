from BPTK_Py import Agent
from BPTK_Py import log


class Task(Agent):


    def __init__(self, agent_id, sim):
        super().__init__(agent_id, sim)

        self._remaining_effort = self.sim.effort_per_task
        self.state = "open"

    @property
    def remaining_effort(self):

        return self._remaining_effort

    def handle_started_event(self, event):

        self.state = "inProgress"

    def handle_progress_event(self, event):

        self._remaining_effort = max(self._remaining_effort-event.data["progress"], 0)

        log("TASK - remaining effort: {}".format(self.remaining_effort))

        if self.remaining_effort == 0:
            self.state = "closed"

    def act(self, time, sim_round, step):

        super().act(time, sim_round, step)

    def initialize(self):

        self.agent_type = "task"
        self.state = "open"
        self.register_event_handler(["open"], "taskStarted", self.handle_started_event)
        self.register_event_handler(["inProgress"], "taskProgress", self.handle_progress_event)
