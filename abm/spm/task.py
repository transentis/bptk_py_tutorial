from BPTK_Py import Agent
from .events import Events
from BPTK_Py import log


class Task(Agent):

    TYPE = "task"

    STATES = {"OPEN": "open", "IN_PROGRESS": "inProgress", "CLOSED": "closed"}

    def __init__(self, agent_id, sim):
        super().__init__(agent_id, sim)

        self.task_remaining_effort = self.sim.effort_per_task()
        self.state = Task.STATES["OPEN"]

    def remaining_effort(self):

        return self.task_remaining_effort

    def handle_started_event(self, event):

        self.state = Task.STATES["IN_PROGRESS"]

    def handle_progress_event(self, event):

        self.task_remaining_effort = max(self.task_remaining_effort-event.data["progress"], 0)

        log("TASK - remaining effort: {}".format(self.task_remaining_effort))

        if self.task_remaining_effort == 0:
            self.state = Task.STATES["CLOSED"]

    def act(self, time, sim_round, step):

        super().act(time, sim_round, step)

    def initialize(self):

        self.agent_type = Task.TYPE
        self.state = Task.STATES["OPEN"]
        self.register_event_handler([Task.STATES["OPEN"]], Events.TASK_STARTED, self.handle_started_event)
        self.register_event_handler([Task.STATES["IN_PROGRESS"]], Events.TASK_PROGRESS, self.handle_progress_event)
