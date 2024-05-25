import unittest

import sys
sys.path.append('../models')

from pda import State, Transition, PDA

class TestPDA(unittest.TestCase):
	global start_state, end_state
	start_state = State("start")
	end_state = start_state

	def test_empty(self):
		empty_transition = Transition(start_state, '', '', '', end_state)

		empty_pda = PDA(
						states = [start_state],
						transitions = [empty_transition],
						input_alph = [''], stack_alph = [''],
						start_state = start_state,
						accept_states = [start_state]
					)

		self.assertTrue(empty_pda.run(x=[''])[0])

	def test_one_transition(self):
		only_transition = Transition(start_state, 'a', '', '', end_state)

		one_transition_pda = PDA(
								states = [start_state],
								transitions = [only_transition],
								input_alph = ['a', 'b'], stack_alph = [''],
								start_state = start_state,
								accept_states = [start_state]
							)

		self.assertTrue(one_transition_pda.run(x=[''])[0])

		self.assertTrue(one_transition_pda.run(x=['a'])[0])

		self.assertFalse(one_transition_pda.run(x=['b'])[0])

		self.assertFalse(one_transition_pda.run(x=['a', 'b'])[0])

	def test_an_bn(self):
		"""
		PDA that decides {a^nb^n | n >= 0}
		"""
		state_a = State("read a")
		state_b = State("read b")
		state_accept = State("accept")

		mark_beginning = Transition(start_state, '', '', '$', state_a)
		read_a = Transition(state_a, 'a', '', 'a', state_a)
		switch = Transition(state_a, 'b', 'a', '', state_b)
		only_b = Transition(state_b, 'b', 'a', '', state_b)
		end = Transition(state_b, '', '$', '', state_accept)

		an_bn_pda = PDA(
						states = [start_state, state_a, state_b, state_accept],
						transitions = [mark_beginning, read_a, switch, only_b, end],
						input_alph = ['a', 'b'],
						stack_alph = ['a', 'b', '$'],
						start_state = start_state,
						accept_states = [start_state,state_accept]
					)

		self.assertTrue(an_bn_pda.run(x=[''])[0])

		self.assertTrue(an_bn_pda.run(x=['a', 'b'])[0])

		self.assertFalse(an_bn_pda.run(x=['a', 'b', 'b'])[0])

	def test_palindromes(self):
		"""
		PDA that decides {wcw^R | w in {a,b}*}
		"""

		state_add = State("add symbol")
		state_remove = State("remove symbol")
		state_accept = State('accept')

		mark_beginning = Transition(start_state, '', '', '$', state_add)
		add_a = Transition(state_add, 'a', '', 'a', state_add)
		add_b = Transition(state_add, 'b', '', 'b', state_add)
		switch = Transition(state_add, 'c', '', '', state_remove)
		remove_a = Transition(state_remove, 'a', 'a', '', state_remove)
		remove_b = Transition(state_remove, 'b', 'b', '', state_remove)
		end = Transition(state_remove, '', '$', '', state_accept)

		palindrome_pda = PDA(
							states = [start_state, state_add, state_remove, state_accept],
							transitions = [mark_beginning, add_a, add_b, switch, remove_a, remove_b, end],
							input_alph = ['a','b','c'],
							stack_alph = ['a','b','c','$'],
							start_state = start_state,
							accept_states = [start_state, state_accept]
						)

		self.assertTrue(palindrome_pda.run(x=[''])[0])

		self.assertTrue(palindrome_pda.run(x=['c'])[0])

		self.assertTrue(palindrome_pda.run(x=['a','c','a'])[0])

		self.assertFalse(palindrome_pda.run(x=['a'])[0])

		self.assertFalse(palindrome_pda.run(x=['a','a'])[0])

		self.assertFalse(palindrome_pda.run(x=['c','a'])[0])

		self.assertFalse(palindrome_pda.run(x=['b','c'])[0])

		self.assertFalse(palindrome_pda.run(x=['a','c','a','c','a'])[0])

	def test_loop(self):
		"""
		PDA which infinitely loops
		"""

		infinite = Transition(start_state, '', '', '', start_state)

		infinite_pda = PDA(
						states = [start_state],
						transitions = [infinite],
						input_alph = [''],
						stack_alph = [''],
						start_state = start_state,
						accept_states = [],
						max_depth = 50
					)

		self.assertFalse(infinite_pda.run(x=[''])[0])

if __name__ == '__main__':
	unittest.main()