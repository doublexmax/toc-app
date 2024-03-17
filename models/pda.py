from typing import List, Dict
import asyncio

from utils import force_type


class State:
	def __init__(self, name):
		self.name = name

class Transition:
	@force_type(State, str, str, str, State)
	def __init__(self, on_state: State, read_symbol: str, pop_from_stack: str, add_to_stack: str, end_state: State):
		if len(read_symbol) != 1:
			raise ValueError(read_symbol)

		if len(pop_from_stack) != 1:
			raise ValueError(pop_from_stack)

		if len(add_to_stack) != 1:
			raise ValueError(add_to_stack)

		self.on_state = on_state
		self.read_symbol = read_symbol
		self.pop_from_stack = pop_from_stack
		self.add_to_stack = add_to_stack
		self.end_state = end_state

class PDA:
	@force_type(List[State], Dict[State, Transition], List[str], List[str], State, List[State])
	def __init__(self, states: List[State], transitions: Dict[State, Transition], input_alph: List[str], stack_alph: List[str], start_state: State, accept_states: List[State]):
		if not all(map(lambda x: len(x) == 1, input_alph)):
			raise ValueError(input_alph)

		if not all(map(lambda x: len(x) == 1, stack_alph)):
			raise ValueError(stack_alph)

		self.states = states
		self.transitions = transitions
		self.input_alph = input_alph
		self.stack_alph = stack_alph
		self.start_state = start_state
		self.accept_states = accept_states

	def run(self, x):
		return asyncio.run(self.gather_threads(x, ['']))

	async def gather_threads(self, x, stack):
		if len(x) == 0:
			return True

		tasks = []

		cur_state = self.start_state

		cur_symbol = x.pop()

		cur_stack = stack.pop()

		for transition in transitions[cur_state]:
			if transition.read_symbol == cur_symbol and cur_stack == transition.pop_from_stack:				
				tasks.append(asyncio.create_task(self.run(x, [s for s in stack] + [transition.add_to_stack])))


		if any(tasks):
			return await asyncio.gather(*tasks)
		else:
			return False