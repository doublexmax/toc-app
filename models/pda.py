from typing import List, Dict
import asyncio

from utils import force_type

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
	@force_type(List[State], Dict[State, List[Transition]], List[str], List[str], State, List[State])
	def __init__(self, states: List[State], transitions: Dict[State, List[Transition]], input_alph: List[str], stack_alph: List[str], start_state: State, accept_states: List[State]):
		if not all(map(lambda x: len(x) == 1 or x == '', input_alph)):
			raise ValueError(input_alph)

		if not all(map(lambda x: len(x) == 1 or x == '', stack_alph)):
			raise ValueError(stack_alph)

		self.states = states
		self.transitions = transitions
		self.input_alph = input_alph
		self.stack_alph = stack_alph
		self.start_state = start_state
		self.accept_states = accept_states

	def run(self, x):
		return asyncio.run(self.gather_threads(x, [''], []))

	async def gather_threads(self, x, stack, history):
		if len(x) == 0:
			return True, history

		tasks = []

		cur_state = self.start_state

		cur_symbol = x.pop()

		if cur_symbol == '':
			return True, history

		if cur_symbol not in self.input_alph:
			raise ValueError(f"Invalid symbol: {cur_symbol}")

		cur_stack = stack.pop()

		for transition in self.transitions[cur_state]:
			if transition.read_symbol == cur_symbol and cur_stack == transition.pop_from_stack:				
				tasks.append(asyncio.create_task(self.gather_threads(x, [s for s in stack] + [transition.add_to_stack], history + [str(transition)])))


		if any(tasks):
			return await asyncio.gather(*tasks)
		else:
			return False