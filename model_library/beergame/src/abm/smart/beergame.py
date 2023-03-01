from BPTK_Py import Model
from ..base.brewery import Brewery
from ..base.distributor import Distributor
from ..base.wholesaler import Wholesaler
from ..base.retailer import Retailer
from ..base.consumer import Consumer
from ..base.controlling import Controlling
from .orderStrategy import SmartOrderStrategy

class Beergame(Model):

    def instantiate_model(self):
        self.register_agent_factory("brewery", lambda agent_id, model, properties: Brewery(agent_id, model, properties,SmartOrderStrategy()))
        self.register_agent_factory("distributor", lambda agent_id, model, properties: Distributor(agent_id, model, properties, SmartOrderStrategy()))
        self.register_agent_factory("wholesaler", lambda agent_id, model, properties: Wholesaler(agent_id, model, properties, SmartOrderStrategy()))
        self.register_agent_factory("retailer", lambda agent_id, model, properties: Retailer(agent_id, model, properties, SmartOrderStrategy()))
        self.register_agent_factory("consumer", lambda agent_id, model, properties: Consumer(agent_id, model, properties))
        self.register_agent_factory("controlling", lambda agent_id, model, properties: Controlling(agent_id, model, properties))



