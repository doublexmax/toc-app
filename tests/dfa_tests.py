import unittest

import sys
sys.path.append('../models')

from dfa import State, Transition, DFA

class TestDFA(unittest.TestCase):
	global start_state, end_state
	start_state = State("start")
	end_state = State("end")

	def test_empty(self):
		transition_a = Transition(start_state, 'a', start_state)
		transition_b = Transition(start_state, 'b', start_state)

		empty_dfa = DFA(
								states = [start_state, end_state],
								transitions = [],
								input_alph = ['a','b'],
								start_state = start_state,
								accept_states = [start_state]
							)

		#print(empty_dfa.run(x=['']))
		self.assertTrue(empty_dfa.run(x=[''])[0])

	def test_one_transition(self):
		transition_a = Transition(start_state, 'a', end_state)
		transition_b = Transition(start_state, 'b', end_state)

		one_transition_dfa = DFA(
						states = [start_state, end_state],
						transitions = [transition_a, transition_b],
						input_alph = ['a','b'],
						start_state = start_state,
						accept_states = [end_state]
					)
		#print(one_transition_dfa.run(x=['a']))
		self.assertTrue(one_transition_dfa.run(x=['a'])[0])

	def test_a_b(self):
		only_a = State("only a")
		only_b = State("only b")
		
		transition_a = Transition(start_state, 'a', only_a)
		transition_b = Transition(start_state, 'b', only_b)
		transition_read_a = Transition(only_a, 'a', only_a)
		transition_switch = Transition(only_a, 'b', only_b)
		transition_stay_b = Transition(only_b, 'b', only_b)

		a_b_dfa = DFA(
				states = [start_state, only_a, only_b],
				transitions = [transition_a, transition_b, transition_read_a, transition_switch, transition_stay_b],
				input_alph = ['a','b'],
				start_state = start_state,
				accept_states = [start_state, only_a, only_b]
			)

		self.assertTrue(a_b_dfa.run(x=[''])[0])

		self.assertTrue(a_b_dfa.run(x=['a'])[0])

		self.assertTrue(a_b_dfa.run(x=['a','b'])[0])

		self.assertTrue(a_b_dfa.run(x=['a','a'])[0])

		self.assertTrue(a_b_dfa.run(x=['a','a','b'])[0])

		self.assertTrue(a_b_dfa.run(x=['b','b'])[0])

		self.assertFalse(a_b_dfa.run(x=['b','a'])[0])

		self.assertFalse(a_b_dfa.run(x=['a','b','a'])[0])


if __name__ == '__main__':
	unittest.main()