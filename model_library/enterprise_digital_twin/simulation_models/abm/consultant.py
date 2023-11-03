from BPTK_Py import Agent
from BPTK_Py import Event


class Consultant(Agent):

    def __init__(self, agent_id, model, properties,agent_type="agent"):
        super().__init__(agent_id,model,properties,agent_type)
        self._effort_spent = 0

    def initialize(self):

        self._effort_spent = 0
        self.agent_type = "consultant"
        self.state = "available"
        self.set_property("project", {"type": "Agent", "value": None})

    def reset_cache(self):
        self.state="available"
        self.project = None
        self._effort_spent = 0

    def act(self, time, round_no, step_no):

        controlling = self.model.next_agent("controlling", "active")
        
        if controlling:
            controlling.receive_instantaneous_event(Event("consultant_cost", self.id, controlling.id,{"salary":self.salary*self.model.dt,"workplace_cost":self.workplace_cost*self.model.dt}))
            controlling.receive_instantaneous_event(Event("consultant_capacity", self.id, controlling.id,{"capacity":self.model.dt}))

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
                        self.project = self.model.next_agent("marketing_campaign","ready")

                        if self.project is not None:
                            self.state = "busy"
                            self.project.receive_instantaneous_event(Event("project_started",self.id,self.project.id))
                        else:
                            self.project = self.model.next_agent("marketing_campaign", "started")

                            if self.project is not None:
                                self.state = "busy"
                                self.project.receive_instantaneous_event(Event("project_joined",self.id,self.project.id))
                            else:
                                # no available projects and no marketing campaign
                                work_capacity = 0

            if self.state == "busy":
                if self.project.state == "completed":
                    self.state = "available"
                    self.project = None
                    return


                # the actual progress made on the project depends on the remaining effort

                work_done = min(work_capacity, self.project.remaining_effort)

                if work_done > 0:
                    work_capacity -= work_done

                    self.project.receive_instantaneous_event(
                        Event(
                            "project_progress",
                            self.id,
                            self.project.id,
                            {"progress": work_done}
                        )
                    )
                else:
                    # the project has no budget the consultant stays on the project for now
                    work_capacity = 0
                

   

              



