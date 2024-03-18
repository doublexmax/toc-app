import unittest

import sys
sys.path.append('../models')

from pda import State, Transition, PDA

class TestPDA(unittest.TestCase):
	global start_state, end_state, empty_transition
	start_state = State("start")
	end_state = start_state

	empty_transition = Transition(start_state, '', '', '', end_state)

	def test_empty(self):
		empty_pda = PDA(
						states = [start_state],
						transitions = {start_state: [empty_transition]},
						input_alph = [''], stack_alph = [''],
						start_state = start_state,
						accept_states = [start_state]
					)

		self.assertTrue(empty_pda.run(x=['']))

	def test_one_transition(self):
		only_transition = Transition(start_state, 'a', '', '', end_state)

		one_transition_pda = PDA(
								states = [start_state],
								transitions = {start_state: [only_transition]},
								input_alph = ['a', 'b'], stack_alph = [''],
								start_state = start_state,
								accept_states = [start_state]
							)

		self.assertTrue(one_transition_pda.run(x=['']))

		self.assertTrue(one_transition_pda.run(x=['a']))

		self.assertFalse(one_transition_pda.run(x=['b']))

		self.assertFalse(one_transition_pda.run(x=['a', 'b']))

if __name__ == '__main__':
	unittest.main()