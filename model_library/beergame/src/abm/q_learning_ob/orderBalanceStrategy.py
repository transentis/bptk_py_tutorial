from ..base.orderStrategy import OrderStrategy
import random

class OrderBalanceStrategy(OrderStrategy):
    def __init__(self, q_table):
        super().__init__()
        self.q_table = q_table
        self.last_state = None
        self.last_action = None

    def initialize(self, agent):
        super().initialize(agent)
        self.agent.set_property("reward", {"type": "Double", "value": 0})  # steady state reward
        def handle_reward_event(event):
            self.agent.reward = event.data["reward"]
        self.agent.register_event_handler(["active"], "reward", handle_reward_event)
        self.last_state = (600,)  # steady state order_balance
        self.last_action = 100

    def calculate_order(self, time):
        amount = 0
        if self.agent.model.learning_on == 1:
            amount = self.q_learning_training(time)
        elif self.agent.model.use_training_results == 1:
            amount = self.q_learning_order(time)
        return amount

    def q_learning_order(self, time):
        return self.q_table.best_action((self.agent.order_balance-self.agent.incoming_order,))

    def q_learning_training(self,time):
        
        # no more learning if game is over
        if self.agent.model.game_over and time > self.agent.model.game_over_round:
            return 0
        
        # update the q_table with the reward from last round
        last_action_value = self.q_table.read_value(
                self.last_state,
                self.last_action
        )
        max_next_action_value = self.q_table.max_action_value((self.agent.order_balance-self.agent.incoming_order,))
        new_action_value = (
            last_action_value +
            self.agent.model.alpha*(
                self.agent.reward + 
                self.agent.model.gamma * max_next_action_value -
                last_action_value
            )
        )
        self.q_table.add_value(self.last_state, self.last_action, new_action_value)
        # now choose the next amount using the q-table
        if random.uniform(0, 1) < self.agent.model.epsilon:
            amount =  random.randint(0, round(1.5*self.agent.incoming_order)) 
        else:
            amount = self.q_learning_order(time)
            
        # update q-learning data
        self.last_state = (self.agent.order_balance-self.agent.incoming_order,)
        self.last_action = amount
        return amount
