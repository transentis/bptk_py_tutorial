from BPTK_Py import Agent
from BPTK_Py import Event


class StaffMember(Agent):


    def initialize(self):

        self.agent_type = "staf_member"
        self.state = "available"
        self.set_property("task", {"type": "Agent", "value": None})

    def act(self, time, round_no, step_no):

       work_capacity = self.model.dt * self.model.productivity

       while work_capacity > 0:
            if self.state == "available":

                self.task = self.model.next_agent("task", "open")

                if self.task is not None:

                    self.state = "busy"
                    self.task.receive_instantaneous_event(Event("task_started", self.id, self.task.id))
                else:
                    # no more open tasks
                    work_capacity = 0

            if self.state == "busy":

                # the actual progress we make on a task depends on the remaining effort

                work_done = min(work_capacity, self.task.remaining_effort)
                work_capacity -= work_done

                self.task.receive_instantaneous_event(
                    Event(
                         "task_progress",
                        self.id,
                        self.task.id,
                        {"progress": work_done}
                     )
                )

                if self.task.state == "closed":
                    self.state = "available"
                    self.task = None




