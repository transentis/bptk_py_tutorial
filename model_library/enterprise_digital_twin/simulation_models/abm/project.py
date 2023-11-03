from BPTK_Py import Agent
from BPTK_Py import Event

class Project(Agent):

    def initialize(self):
        self.agent_type = "project"
        self.state = "acquired"

        self.set_property("remaining_effort", {"type": "Double", "value": 0.0})
        self.set_property("effort", {"type": "Double", "value": 0.0})
        self.set_property("staff", {"type": "Double", "value": 0.0})
        self.set_property("effort_risk", {"type": "Double", "value": 0.0})

        self.register_event_handler(["ready"], "project_started", self.handle_started_event)
        self.register_event_handler(["started"], "project_joined", self.handle_joined_event)
        self.register_event_handler(["started"], "project_progress", self.handle_progress_event)
        self.register_event_handler(["fully_staffed"], "project_progress", self.handle_progress_event)

        self._effort_spent = 0.0
        self._generated_follow_on = False
        self._sent_count_info = False


    def reset_cache(self):
        self._effort_spent=0.0
        self._sent_count_info = False
        self._generated_follow_on=False
        self.state="acquired"
        self.remaining_effort=0.0
        self.staff=0.0
        self.effort=0.0
        self.effort_risk=0.0
    

    def handle_started_event(self, event):
        self.effort = self.contracted_effort
        self.remaining_effort = self.effort
        self.effort_risk = 1.0 - self.contracted_probability
            
        self.staff = self.staff + 1.0

        if self.staff == self.consultants:
            self.state = "fully_staffed"
        else:
            self.state = "started"

    def handle_joined_event(self, event):
        self.staff = self.staff+1.0
        if self.staff == self.consultants:
            self.state = "fully_staffed"


    def handle_progress_event(self, event):
        self.remaining_effort = max(self.remaining_effort-event.data["progress"], 0.0)
        
        self._effort_spent=self._effort_spent + event.data["progress"]

        

    def act(self, time, round_no, step_no):

        controlling = self.model.next_agent("controlling", "active")

        if controlling:         
            controlling.receive_instantaneous_event(Event("revenue", self.id, controlling.id,{"revenue":self._effort_spent*self.billing_rate, "revenue_risk": self.effort_risk}))

            controlling.receive_instantaneous_event(Event("consulting_effort",self.id,controlling.id,{"effort_delivered":self._effort_spent}))
            if not self._sent_count_info:
                controlling.receive_instantaneous_event(Event("count_project",self.id,controlling.id,{"count":1}))
                self._sent_count_info = True
            
        self._effort_spent=0.0
    
        if self.state=="acquired" and time*1.0==self.start_time:
            self.state="ready"

        if time*1.0 >= self.deadline and not self.state=="completed":
            self.state="completed"

        if time*1.0 < min(self.deadline,self.model.stoptime) and self.remaining_effort<=0.0 and  self.state in ['started','fully_staffed']:
            if self.extension_probability > (1.0-self.model.revenue_risk_level):
                self.remaining_effort = self.remaining_effort+self.extension_effort
                self.effort_risk = 1.0-self.extension_probability
            if self.remaining_effort<=0.0:
                self.state="completed"            
       
        if self.state in ['started','ready','fully_staffed']:
            controlling.receive_instantaneous_event(Event("consultant_demand", self.id, controlling.id,{"consultant_demand":self.consultants}))
            
        if time*1.0 == self.deadline and not self._generated_follow_on and self.follow_on_probability>(1.0-self.model.revenue_risk_level):
            self._generated_follow_on=True
            
            self.model.create_agent("project",

             {
                 "name":
                 {
                     "type":"String",
                     "value": self.name+" (Follow On)"
                 },
                    "contracted_effort":
                        {
                            "type": "Double",
                            "value": self.contracted_effort
                        },
                    "contracted_probability":
                    {
                        "type":"Double",
                        "value": self.follow_on_probability
                    },
		        "extension_probability":
		        {
		            "type": "Double",
		            "value": self.extension_probability
		        },
		        "extension_effort":
		        {
		            "type": "Double",
		            "value": self.extension_effort
		        },
		        "follow_on_probability":
		        {
		            "type": "Double",
		            "value": 0.0
		        },
                        "is_follow_on":
		        {
		             "type":"Boolean",
		             "value":True
		         },
                        "consultants":
                        {
                            "type": "Double",
                            "value":self.consultants
                        },
                        "start_time":
                        {
                            "type": "Double",
                            "value":time+1.0
                        },
		        "deadline":
		        {"type":"Double",
		         "value":min(self.model.stoptime ,time+self.deadline-self.start_time)},
                        "billing_rate":
                        {
                            "type": "Double",
                            "value":self.billing_rate
                        }
                })



