from BPTK_Py import Model
from .brewery import Brewery
from .distributor import Distributor
from .wholesaler import Wholesaler
from .retailer import Retailer
from .consumer import Consumer
from .controlling import Controlling
from .orderStrategy import TypicalOrderStrategy

class Beergame(Model):

    def instantiate_model(self):
        self.register_agent_factory("brewery", lambda agent_id, model, properties: Brewery(agent_id, model, properties,TypicalOrderStrategy()))
        self.register_agent_factory("distributor", lambda agent_id, model, properties: Distributor(agent_id, model, properties, TypicalOrderStrategy()))
        self.register_agent_factory("wholesaler", lambda agent_id, model, properties: Wholesaler(agent_id, model, properties, TypicalOrderStrategy()))
        self.register_agent_factory("retailer", lambda agent_id, model, properties: Retailer(agent_id, model, properties, TypicalOrderStrategy()))
        self.register_agent_factory("consumer", lambda agent_id, model, properties: Consumer(agent_id, model, properties))
        self.register_agent_factory("controlling", lambda agent_id, model, properties: Controlling(agent_id, model, properties))



