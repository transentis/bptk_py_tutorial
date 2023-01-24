from BPTK_Py import Agent
from BPTK_Py import Event


class Consultant(Agent):


    def initialize(self):

        self.agent_type = "consultant"
        self.state = "available"
        self.set_property("project", {"type": "Agent", "value": None})

    def act(self, time, round_no, step_no):

        controlling = self.model.next_agent("controlling", "active")
        
        if controlling:
            controlling.receive_instantaneous_event(Event("salary", self.id, controlling.id,{"salary":self.salary}))

        self._effort_spent=0
  
        work_capacity = self.model.dt # the amount of work a consultant could do in this time step

        while work_capacity > 0:
            if self.state == "available":

                self.project = self.model.next_agent("project", "ready")

                if self.project is not None:

                    self.state = "busy"
                    self.project.receive_instantaneous_event(Event("project_started", self.id, self.project.id))
                else:
                    self.project = self.model.next_agent("project","started")

                    if self.project is not None:
                        self.state = "busy"
                        self.project.receive_instantaneous_event(Event("project_joined",self.id, self.project.id))
                    else:
                        # no available projects
                        work_capacity = 0

            if self.state == "busy":
                if self.project.state == "completed":
                    self.state = "available"
                    self.project = None
                    return

                # the actual progress we make on a project depends on the remaining effort

                work_done = min(work_capacity, self.project.remaining_effort)
                work_capacity -= work_done

                self.project.receive_instantaneous_event(
                    Event(
                         "project_progress",
                        self.id,
                        self.project.id,
                        {"progress": work_done}
                     )
                )

   

              



