import pickle
import json
from BPTK_Py import Model
from BPTK_Py import Event
from ..base.distributor import Distributor
from ..base.wholesaler import Wholesaler
from ..base.retailer import Retailer
from ..base.brewery import Brewery
from ..base.consumer import Consumer
from .controlling import ControllingQlOB
from .orderBalanceStrategy import OrderBalanceStrategy
from ..q_learning_base.sparseQTable import SparseQTable
from ..q_learning_base.sparseQTable import SparseQTableEncoder
from ..q_learning_base.sparseQTable import SparseQTableDecoder


class BeergameQlOB(Model):
    # the q-tables are set up as static methods
    brewery_q_table = SparseQTable(dimension=1)
    distributor_q_table = SparseQTable(dimension=1)
    wholesaler_q_table = SparseQTable(dimension=1)
    retailer_q_table = SparseQTable(dimension=1)
    
    @staticmethod
    def dump_q_tables(path,format="PICKLE"):
        
        if(format=="PICKLE"):
            file = open(path,"wb")
            pickle.dump(BeergameQlOB.brewery_q_table, file)
            pickle.dump(BeergameQlOB.distributor_q_table, file)
            pickle.dump(BeergameQlOB.wholesaler_q_table, file)
            pickle.dump(BeergameQlOB.retailer_q_table, file)
            file.close()
        elif(format=="JSON"):
            # the JSON dump format isn't a framed protocoll, so we cannot dump multiple objects into one file
            # hence we create our own frame using a dict
            qtable_json = {}
            qtable_json["brewery"] = json.dumps(BeergameQlOB.brewery_q_table,cls=SparseQTableEncoder)
            qtable_json["distributor"] = json.dumps(BeergameQlOB.distributor_q_table,cls=SparseQTableEncoder)
            qtable_json["wholesaler"] = json.dumps(BeergameQlOB.wholesaler_q_table,cls=SparseQTableEncoder)
            qtable_json["retailer"] = json.dumps(BeergameQlOB.retailer_q_table,cls=SparseQTableEncoder)
            file = open(path,"w")
            json.dump(qtable_json,file)
            file.close()
        
    
    @staticmethod
    def load_q_tables(path,format="PICKLE"):
        
        if(format=="PICKLE"):
            file = open(path,"rb")
            BeergameQlOB.brewery_q_table = pickle.load(file)
            BeergameQlOB.distributor_q_table = pickle.load(file)
            BeergameQlOB.wholesaler_q_table = pickle.load(file)
            BeergameQlOB.retailer_q_table = pickle.load(file)
            file.close()
        elif(format=="JSON"):
            file = open(path,"r")
            qtable_json=json.load(file)
            file.close()
            BeergameQlOB.brewery_q_table = json.loads(qtable_json["brewery"], cls=SparseQTableDecoder)
            BeergameQlOB.distributor_q_table = json.loads(qtable_json["distributor"], cls=SparseQTableDecoder)
            BeergameQlOB.wholesaler_q_table = json.loads(qtable_json["wholesaler"], cls=SparseQTableDecoder)
            BeergameQlOB.retailer_q_table = json.loads(qtable_json["retailer"], cls=SparseQTableDecoder)
        

    def instantiate_model(self):
        self.register_agent_factory(
            "brewery",
            lambda agent_id, model, properties:
                Brewery(
                    agent_id,
                    model,
                    properties,
                    OrderBalanceStrategy(BeergameQlOB.brewery_q_table)
                )
        )

        self.register_agent_factory(
            "distributor",
            lambda agent_id, model, properties: 
                Distributor(
                    agent_id,
                    model,
                    properties,
                    OrderBalanceStrategy(BeergameQlOB.distributor_q_table)
                )
        )
        self.register_agent_factory(
            "wholesaler",
            lambda agent_id, model, properties:
                Wholesaler(
                    agent_id,
                    model,
                    properties,
                    OrderBalanceStrategy(BeergameQlOB.wholesaler_q_table)
                )
        )
        self.register_agent_factory(
            "retailer",
            lambda agent_id, model, properties:
                Retailer(
                    agent_id,
                    model,
                    properties,
                    OrderBalanceStrategy(BeergameQlOB.retailer_q_table)
                )
        )
        self.register_agent_factory(
            "consumer",
            lambda agent_id, model, properties:
                Consumer(
                    agent_id,
                    model,
                    properties
                 )
        )
        self.register_agent_factory(
            "controlling",
            lambda agent_id, model, properties:
                ControllingQlOB(
                    agent_id,
                    model,
                    properties
                )
        )

        # q-learning parameters
        self.set_property("alpha", {"type": "Double", "value": 0.2})
        self.set_property("gamma", {"type": "Double", "value": 1.0})
        self.set_property("epsilon", {"type": "Double", "value": 0.1})
        self.set_property("game_over", {"type": "Boolean", "value": False})
        self.set_property("game_over_round", {"type": "Integer","value":24})

    def begin_episode(self, epsiode_no):
        super().begin_episode(epsiode_no)
        self.game_over=False
        self.game_over_round=24
        
    def end_round(self, time, sim_round, step):
        supply_chain_agents = {"brewery", "distributor", "wholesaler", "retailer"}
        controlling_agent = None
        total_reward = 0
        
        for agent in self.agents:
            if agent.agent_type == "controlling":
                controlling_agent = agent

        for agent in self.agents:
            reward = 0
            if agent.agent_type in supply_chain_agents and not self.game_over:
                if (agent.order_balance < 0  or agent.order_balance > 1400):
                    self.game_over = True
                    self.game_over_round = time + 1 # run one more round to pickup the rewards, then stop
                    reward = -10000
                elif agent.outgoing_order < agent.incoming_order:
                    reward = -10000
                else:
                    if time == 3:
                        if 750 >= agent.order_balance >= 600:
                            reward += 2000
                    if time == 5:
                        if 900 >= agent.order_balance >= 700:
                            reward += 2000      
                    if time == 10:
                        if 1150 >= agent.order_balance >= 1000:
                            reward += 2000      
                    if time == 15:
                        if 1250 >= agent.order_balance >= 1100:
                            reward += 2000
                    if time == 20:
                        if 1250 >= agent.order_balance >= 1150:
                            reward += 2000
                    if time == self.stoptime - 1: # penultimate round, to ensure rewards are handled in final round
                        if agent.total_cost < 10000:
                            reward += 10000
                        if controlling_agent.supply_chain_cost < 40000:
                            reward += 20000
                total_reward += reward
                agent.receive_instantaneous_event(Event("reward", None, agent.id, {"reward": reward}))
        controlling_agent.receive_instantaneous_event(Event("supply_chain_reward", None, None, {"supply_chain_reward": total_reward}))


