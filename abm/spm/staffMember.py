from BPTK_Py import Agent
from BPTK_Py import Event
from .events import Events
from .task import Task


class StaffMember(Agent):

    TYPE = "staffMember"

    STATES = {"BUSY": "busy", "AVAILABLE": "available"}

    def __init__(self, sim_id, sim):
        super().__init__(sim_id, sim)

        self.task = None
        self.task_progress_in_this_step = 0

    def current_task(self):
        return self.task

    def act(self, time, round_no, step_no):

        if self.state == StaffMember.STATES["BUSY"]:

            progress_made = min(self.task.remaining_effort(), self.task_progress_in_this_step)

            self.task_progress_in_this_step -= progress_made

            self.task.receive_instantaneous_event(
                Event(
                    Events.TASK_PROGRESS,
                    self.id,
                    self.task.id,
                    {"progress": progress_made}
                )
            )

            if self.task.state == Task.STATES["CLOSED"]:

                self.state = StaffMember.STATES["AVAILABLE"]

                self.task = None
            else:
                self.task_progress_in_this_step += self.sim.productivity()/self.sim.effort_per_task()

        if self.state == StaffMember.STATES["AVAILABLE"]:

            self.task = self.sim.next_agent(Task.TYPE, Task.STATES["OPEN"])

            if self.task is not None:

                self.task.receive_instantaneous_event(Event(Events.TASK_STARTED, self.id, self.task.id))

                self.state = StaffMember.STATES["BUSY"]

                self.task_progress_in_this_step += self.sim.productivity() * self.sim.effort_per_task()

    def initialize(self):

        self.agent_type = StaffMember.TYPE
        self.state = StaffMember.STATES["AVAILABLE"]
