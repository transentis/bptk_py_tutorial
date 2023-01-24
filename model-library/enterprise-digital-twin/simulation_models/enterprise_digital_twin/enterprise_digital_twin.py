from BPTK_Py import Model
from .consultant import Consultant
from .project import Project
from .controlling import Controlling
from .enterprise_digital_twin_sd import EnterpriseDigitalTwinSD
class EnterpriseDigitalTwin(Model):

    def instantiate_model(self):
        super().instantiate_model()
        # register the agent factories

        self.register_agent_factory("consultant", lambda agent_id, model, properties: Consultant(agent_id, model, properties))
        self.register_agent_factory("project", lambda agent_id, model, properties: Project(agent_id, model, properties))
        self.register_agent_factory("controlling", lambda agent_id, model, properties: Controlling(agent_id, model, properties))

        self.sd_model = EnterpriseDigitalTwinSD(self)
