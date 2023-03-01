class SparseQTable:
    def __init__(self, dimension=3, default_value=0):
        self.dimension = dimension
        self.default_value = default_value
        self.elements = {} # this is the q-table
        self._max_action_value = {} # cache of max action values for faster access
        self._best_action = {} # cache of best actions for faster access

    def add_value(self, state, action, value):
        if len(state) != self.dimension:
            raise(Exception("Length of state expected to be {}".format(self.dimension)))
        key = state+(action,)
        self.elements[key] = value
        try:
            if self._max_action_value[state] < value:
                self._max_action_value[state] = value
        except KeyError:
            self._max_action_value[state] = value
        try:
            if self._best_action[state]["value"] < value:
                self._best_action[state] = {"action": action, "value": value}
        except KeyError:
            self._best_action[state] = {"action": action, "value": value} 

    def read_value(self, state, action):
        if len(state) != self.dimension:
            raise(Exception("Length of state expected to be {}".format(self.dimension)))
        try:
            key = state + (action, )
            value = self.elements[key]
        except KeyError:
            value = self.default_value
        return value

    def total(self):
        tensor_sum = 0
        for key, value in self.elements.items():
            tensor_sum += value
        return tensor_sum

    def max_action_value(self, state):
        if len(state) != self.dimension:
            raise(Exception("Num elements in state expected to be {}".format(self.dimension)))
        max_value = self.default_value
        try:
            max_value = max(self._max_action_value[state],max_value)
        except KeyError:
            pass
        return max_value

    def best_action(self, state):
        if len(state) != self.dimension:
            raise(Exception("Num elements in state expected to be {}".format(self.dimension)))
        max_value = None
        best_action = 0
        try:
            best_action=self._best_action[state]["action"]
        except KeyError:
            pass
        return best_action

    def count(self):
        return len(self.elements)
        
 
import json       
class SparseQTableEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SparseQTable):
            return {
                "type":"SparseQTable",
                "value":{
                    "dimension": obj.dimension,
                    "default_value": obj.default_value,
                    "elements": {json.dumps(k): v for k, v in obj.elements.items()},
                    "max_action_value": {json.dumps(k): v for k, v in obj._max_action_value.items()},
                    "best_action": {json.dumps(k): v for k, v in obj._best_action.items()}
                }
            }
        return super(SparseQTableEncoder, self).default(obj)
        
import json       
class SparseQTableDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if 'type' not in obj:
            return obj
        type = obj['type']
        if type == 'SparseQTable':
            qtable = SparseQTable(obj["value"]["dimension"],obj["value"]["default_value"])
            qtable.elements = {tuple(json.loads(k)): v for k, v in obj["value"]["elements"].items()}
            qtable._max_action_value = {tuple(json.loads(k)): v for k, v in obj["value"]["max_action_value"].items()}
            qtable._best_action = {tuple(json.loads(k)): v for k, v in obj["value"]["best_action"].items()}
            return qtable
        return obj

