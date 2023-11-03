from BPTK_Py import Agent
from BPTK_Py import Event

class MarketingCampaign(Agent):

    def initialize(self):
        self.agent_type = "marketing_campaign"
        self.state = "initialized"

        self.set_property("remaining_effort", {"type": "Double", "value": 0.0})
        self.set_property("effort", {"type": "Double", "value": 0.0})
        self.set_property("staff", {"type": "Double", "value": 0.0})
       
        
        self.register_event_handler(["ready"], "project_started", self.handle_started_event)
        self.register_event_handler(["started"], "project_joined", self.handle_joined_event)
        self.register_event_handler(["started"], "project_progress", self.handle_progress_event)
        self.register_event_handler(["fully_staffed"], "project_progress", self.handle_progress_event)

        self._generated_projects = False
        

    def reset_cache(self):
        self.set_property("remaining_effort", {"type": "Double", "value": 0.0})
        self.set_property("effort", {"type": "Double", "value": 0.0})
        self.staff = 0.0
        self._generated_projects = False
        self.state = "initialized"

    def handle_started_event(self, event):
        self.effort = self.campaign_effort
        self.remaining_effort = self.effort

        self.staff = self.staff+1.0

        self.state = "started"

    def handle_joined_event(self, event):
        self.staff = self.staff+1.0
        if self.staff == self.consultants:
            self.state = "fully_staffed"


    def handle_progress_event(self, event):
        self.remaining_effort = max(self.remaining_effort-event.data["progress"], 0)
              

    def act(self, time, round_no, step_no):
            
        self._effort_spent=0
    
        if self.state=="initialized" and time*1.0==self.start_time:
            self.state="ready"

        if self.remaining_effort<=0.0 and (self.state == "started" or self.state=="fully_staffed"):
            self.state="completed" 
     
        if self.state=="completed" and not self._generated_projects:
            self._generated_projects=True
            
            self.model.create_agents({
                "name":"project",
                "count":2,
                "properties":
                {
                    
                    "contracted_effort":
                        {
                            "type": "Double",
                            "value": 12.0
                        },
                    "contracted_probability":
                    {
                        "type":"Double",
                        "value": 1.0
                    },
		        "extension_probability":
		        {
		            "type": "Double",
		            "value": 0.8
		        },
		        "extension_effort":
		        {
		            "type": "Double",
		            "value": 6.0
		        },
		        "follow_on_probability":
		        {
		            "type": "Double",
		            "value": 0.0
		        },
                        "consultants":
                        {
                            "type": "Double",
                            "value": 2.0
                        },
                        "start_time":
                        {
                            "type": "Double",
                            "value":time+3.0
                        },
		        "deadline":
		        {
                            "type":"Double",
		            "value":time+3.0+12.0
                         },
                        "billing_rate":
                        {
                            "type": "Double",
                            "value": 5000.0
                        }
                                   
                }})

            
       
