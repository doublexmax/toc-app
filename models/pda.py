from typing import List, Dict
import asyncio

from model_utils import force_type, uncover

class State:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

class Transition:
	@force_type(State, str, str, str, State)
	def __init__(self, on_state: State, read_symbol: str, pop_from_stack: str, add_to_stack: str, end_state: State):
		if len(read_symbol) != 1 and len(read_symbol):
			raise ValueError(read_symbol)

		if len(pop_from_stack) != 1 and len(pop_from_stack):
			raise ValueError(pop_from_stack)

		if len(add_to_stack) != 1 and len(add_to_stack):
			raise ValueError(add_to_stack)

		self.on_state = on_state
		self.read_symbol = read_symbol
		self.pop_from_stack = pop_from_stack
		self.add_to_stack = add_to_stack
		self.end_state = end_state

	def __str__(self):
		return f"({str(self.on_state)}, {self.read_symbol}, {self.pop_from_stack}, {self.add_to_stack}, {str(self.end_state)})"

class PDA:
	@force_type(List[State], List[Transition], List[str], List[str], State, List[State], int)
	def __init__(self, states: List[State], transitions: List[Transition], input_alph: List[str], stack_alph: List[str], start_state: State, accept_states: List[State], max_depth: int = 200):
		if not all(map(lambda x: len(x) == 1 or x == '', input_alph)):
			raise ValueError(input_alph)

		if not all(map(lambda x: len(x) == 1 or x == '', stack_alph)):
			raise ValueError(stack_alph)

		if '' not in input_alph:
			input_alph += ['']

		self.states = states

		transition_dict = {}
		for transition in transitions:
			transition_dict[transition.on_state] = transition_dict.get(transition.on_state, []) + [transition]

		self.transitions = transition_dict

		self.input_alph = input_alph
		self.stack_alph = stack_alph
		self.start_state = start_state
		self.accept_states = accept_states
		self.max_depth = max_depth

	def run(self, x):
		response = asyncio.run(self._gather_threads(self.start_state, list(reversed(x)), [''], []))
		#print(uncover(response))
		return uncover(response)

	async def _gather_threads(self, cur_state, x, stack, history, depth = 0):
		if len(x) == 0:
			if cur_state in self.accept_states:
				return True, history
			else:
				x = ['']

		if depth == self.max_depth:
			return False, history + ["max depth reached"]

		tasks = []

		cur_symbol = x.pop()

		#print(cur_symbol,stack,x,cur_state, 'start')

		if cur_symbol == '' and cur_state in self.accept_states:
			return True, history

		if cur_symbol not in self.input_alph:
			raise ValueError(f"Invalid symbol: {cur_symbol}")

		cur_stack = (stack.pop() if len(stack) > 0 else '')

		for transition in self.transitions.get(cur_state, []):
			if transition.read_symbol == '':
				new_x = x + [cur_symbol]
			elif transition.read_symbol == cur_symbol:
				new_x = x
			else:
				continue
			if transition.pop_from_stack == '':
				#print('2')
				if cur_stack == '':
					if transition.add_to_stack == '':
						new_stack = stack
					else:
						new_stack = stack + [transition.add_to_stack]
				else:
					if transition.add_to_stack == '':
						new_stack = stack + [cur_stack]
					else:
						new_stack = stack + [cur_stack, transition.add_to_stack]
			elif cur_stack == transition.pop_from_stack:
				if transition.add_to_stack == '':
					new_stack = stack
				else:
					new_stack = stack + [transition.add_to_stack]
			else:
				continue
			tasks.append(asyncio.create_task(self._gather_threads(transition.end_state, new_x, new_stack, history + [str(transition)], depth + 1)))
	
		if any(tasks):
			return await asyncio.gather(*tasks)
		else:
			return False, history