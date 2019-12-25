import numpy as np 
import random 
import math

class Qubit:
    '''
    Implements a simple qubit with real probability amplitudes 
    Qubit initialized to |0> by default
    '''
    __epsilon = 1e-10    # used to ensure accurracy during computations

    def __init__(self):
        self.__state_vector = np.array([1, 0])
        assert abs(np.dot(np.transpose(self.__state_vector), self.__state_vector) - 1) < Qubit.__epsilon, \
                 'Failure to initialize Qubit state'

    def __get_probability(self, state):
        '''
        Derives the probability (from the probability amplitude) of measuring state |0> or |1>

        Parameters:
            state (int): if 0, will return probability for |0>; if 1, will return probability for |1>

        Returns:
            float: the desired probability
        '''
        return self.__state_vector[state] ** 2

    def view_state(self, num_hits=1000):
        '''
        Will return the state of the qubit when it's read

        Parameters:
            num_hits (int): increase num_hits to increase the algorithm's adherence to the probability amplitudes

        Returns:
            np.array: indicating whether electron is spin-up or spin-down
        '''
        proportion_spin_up = int((self.__get_probability(0)) ** 2 * num_hits)
        choices = [np.array([1, 0])] * proportion_spin_up \
                + [np.array([0, 1])] * (num_hits - proportion_spin_up)
        decision = random.choice(choices)
        self.__state_vector = decision
        return decision

    def pauli_x(self):
        '''
        Computes the equivalent of the classical NOT gate on the qubit

        Parameters:

        Returns:
        '''
        self.__state_vector = np.dot(np.array([[0, 1], [1, 0]]), self.__state_vector)

    def hadamard(self):
        '''
        Computes the equivalent of the classical NOT gate on the qubit

        Parameters:

        Returns:
        '''
        self.__state_vector = np.dot(math.sqrt(2) * np.array([[1, 1], [1, -1]]), self.__state_vector)

    

if __name__ == '__main__':
    q = Qubit()
