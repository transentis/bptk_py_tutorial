from BPTK_Py import Model
from .abm.consultant import Consultant
from .abm.project import Project
from .abm.controlling import Controlling
from .sd.enterprise_digital_twin_sd import EnterpriseDigitalTwinSD

class EnterpriseDigitalTwin(Model):

    def instantiate_model(self):
        super().instantiate_model()
        # register the agent factories

        self.register_agent_factory("consultant", lambda agent_id, model, properties: Consultant(agent_id, model, properties))
        self.register_agent_factory("project", lambda agent_id, model, properties: Project(agent_id, model, properties))
        self.register_agent_factory("controlling", lambda agent_id, model, properties: Controlling(agent_id, model, properties))

        self.sd_model = EnterpriseDigitalTwinSD(self)
        self._exchange={}
        self._exchange["revenue"]={}
        self._exchange["salaries"]={}

    def run(self,show_progress_widget=False, collect_data=True):
        #this is called at the beginning of every simulation run - use for tidying up
        super().run()