from BPTK_Py import Agent
from BPTK_Py import Event


class StaffMember(Agent):


    def __init__(self, sim_id, sim):
        super().__init__(sim_id, sim)

        self.task = None
        self.task_progress_in_this_step = 0

    def current_task(self):
        return self.task

    def act(self, time, round_no, step_no):

        if self.state == "busy":

            progress_made = min(self.task.remaining_effort, self.task_progress_in_this_step)

            self.task_progress_in_this_step -= progress_made

            self.task.receive_instantaneous_event(
                Event(
                    "taskProgress",
                    self.id,
                    self.task.id,
                    {"progress": progress_made}
                )
            )

            if self.task.state == "closed":

                self.state = "available"

                self.task = None
            else:
                self.task_progress_in_this_step += self.sim.productivity/self.sim.effort_per_task

        if self.state == "available":

            self.task = self.sim.next_agent("task", "open")

            if self.task is not None:

                self.task.receive_instantaneous_event(Event("taskStarted", self.id, self.task.id))

                self.state = "busy"

                self.task_progress_in_this_step += self.sim.productivity * self.sim.effort_per_task

    def initialize(self):

        self.agent_type = "staffMember"
        self.state = "available"
