from typing import List,Dict

from model_utils import force_type

class State:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

class Transition:
	@force_type(State, str, State)
	def __init__(self, on_state, read_symbol, end_state):
		if len(read_symbol) != 1:
			raise ValueError("Symbol read must be of length 1")

		self.on_state = on_state
		self.read_symbol = read_symbol
		self.end_state = end_state

class DFA:
	@force_type(List[State], List[str], List[Transition], State, List[State], int)
	def __init__(self, states: List[State], input_alph: List[str], transitions: List[Transition], start_state: State, accept_states: List[State], max_depth: int = 100):
		if not all(map(lambda x: len(x) == 1, input_alph)):
			raise ValueError(input_alph)

		self.states = states

		transition_dict = {}
		for transition in transitions:
			if (transition.on_state, transition.read_symbol) in transition_dict:
				raise ValueError("Must have deterministic transitions.")
			else:
				transition_dict[(transition.on_state, transition.read_symbol)] = transition

		self.transitions = transition_dict

		self.input_alph = input_alph
		self.start_state = start_state
		self.accept_states = accept_states
		self.max_depth = max_depth

	def run(self, x):
		return self._run_thread(list(reversed(x)), self.start_state, [])

	def _run_thread(self, x, cur_state, history):
		if len(x) == 0:
			return cur_state in self.accept_states, history
		elif (cur_symbol:=x.pop()) == '':
			return cur_state in self.accept_states, history

		next_transition = self.transitions.get((cur_state, cur_symbol))

		if next_transition is None:
			return False, history
		elif next_transition.read_symbol == cur_symbol:
			return self._run_thread(x, next_transition.end_state, history + [next_transition])
		else:
			return False, history