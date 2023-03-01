import numpy as np

# this is an implementation of a fixed size, non-sparse q-table - not currently used
class qTable:
    def __init__(self, size=(0, 0, 0), default_value=0):
        self._size = size
        self._default_value = default_value
        self._elements = np.full(size, default_value)

    def _within_bounds(self, key):
        if len(key) > len(self._size):
            raise(Exception("Length of key expected to be less or equal to {}".format(len(self._size))))
        within_bounds = True
        for idx, value in enumerate(key):
            within_bounds &= ((0 <= value) and (value < self._size[idx]))
        return within_bounds

    def add_value(self, state, action, value):
        if len(state) != len(self._size)-1:
            raise(Exception("Length of state expected to be {}".format(len(self._size)-1)))
        key = state + (action,)
        if self._within_bounds(key):
            self._elements[key] = value

    def read_value(self, state, action):
        if len(state) != len(self._size)-1:
            raise(Exception("Length of state expected to be {}".format(len(self._size)-1)))
        key = state + (action,)
        return self._elements[key] if self._within_bounds(key) else self._default_value

    def total(self):
        return np.sum(self._elements)

    def max_action_value(self, state):
        if len(state) != len(self._size) - 1:
            raise(Exception("Length of state expected to be {}".format(len(self._size)-1)))
        return np.max(self._elements[state]) if self._within_bounds(state) else self._default_value

    def best_action(self, state):
        if len(state) != len(self._size) - 1:
            raise(Exception("Length of state expected to be {}".format(len(self._size)-1)))
        return np.argmax(self._elements[state]) if self._within_bounds(state) else 0

