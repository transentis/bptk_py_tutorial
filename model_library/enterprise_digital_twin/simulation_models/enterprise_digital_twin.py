from BPTK_Py import Model
from .abm.consultant import Consultant
from .abm.project import Project
from .abm.controlling import Controlling
from .abm.marketing_campaign import MarketingCampaign

from .sd.enterprise_digital_twin_sd import EnterpriseDigitalTwinSD

class EnterpriseDigitalTwin(Model):

    def instantiate_model(self):
        super().instantiate_model()
        # register the agent factories

        self.register_agent_factory("consultant", lambda agent_id, model, properties: Consultant(agent_id, model, properties))
        self.register_agent_factory("project", lambda agent_id, model, properties: Project(agent_id, model, properties))
        self.register_agent_factory("controlling", lambda agent_id, model, properties: Controlling(agent_id, model, properties))
        self.register_agent_factory("marketing_campaign", lambda agent_id, model, properties: MarketingCampaign(agent_id, model, properties))

        self.sd_model = None
        self._exchange={}
        self._exchange["revenue"]={}
        self._exchange["revenue_risk"]={}
        self._exchange["salaries"]={}
        self._exchange["consulting_effort"]={}
        self._exchange["consultant_capacity"]={}
        self._exchange["workplace_cost"]={}
        self._exchange["fixed_cost"]={}

    def configure(self,config):
        super().configure(config)
        self.sd_model = EnterpriseDigitalTwinSD(self)
        
        

    def sd_time(self,time):
        # convert abm model time to sd time, because sd model runs at the granularity of abm dt
        return ((time-self.starttime)/self.dt+self.starttime)
        
    def run(self,show_progress_widget=False, collect_data=True):
        #this is called at the beginning of every simulation run - use for tidying up
        super().run()



    def reset_cache(self):
        super().reset_cache()

        self.sd_model.reset_cache()
        
        delete_agent_ids=[]
      
        for agent in self.agents:
            if agent.agent_type=="project" and agent.is_follow_on:
                delete_agent_ids.append(agent.id)

        self.delete_agents(delete_agent_ids)

       

      

        
                
    
