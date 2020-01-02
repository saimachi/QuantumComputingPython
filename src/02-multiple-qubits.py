import numpy as np
import math
import random

def generate_basis_vector_from_string(binary_string):
    '''
    Generates a basis vector from a given binary string

    Parameters:
        binary_string

    Returns: an np.array basis vector
    '''
    if len(binary_string) == 1:
        if binary_string == '0':
            return np.array([1, 0])
        else:
            return np.array([0, 1]) 
    else:
        vectors = []
        for _, val in enumerate(binary_string):
            if val == '0':
                vectors.append(np.array([1, 0]))
            else:
                vectors.append(np.array([0, 1]))
        prod = np.kron(vectors[-2], vectors[-1])
        for i in range(len(vectors) - 3, -1, -1):    # by convention, tensor products are taken in reverse order
            prod = np.kron(vectors[i], prod)
        return prod

class QuantumRegister:
    '''
    This class serves two purposes: represent an entangled quantum register & a single initialized basis for computation

    Parameters:
        n: the size of the register (bits)
    '''
    def __init__(self, n):
        self.n = n
        self.__state_vector = math.sqrt(1 / 2 ** n) * np.ones((1, 2 ** n))    # vector of amplitudes (entangled register)
        self.__circuit_state = np.array([])    # a single later initialized basis state for computation

    # Register Methods

    def view_register_state(self, num_hits=1e6):
        '''
        Collapse and return the state stored in the register 

        Parameters:

        Returns: the collapsed state
        '''
        choices = []
        for amp_index in range(2 ** self.n):
            choice_probability = self.__state_vector[amp_index] ** 2 * num_hits
            choices.append(generate_basis_vector_from_string(bin(amp_index)[2:]))
        self.__state_vector = random.choice(choices)
        return self.__state_vector

    def view_single_qubit_state(self, qubit_index):
        '''
        View the state of an individual qubit without collapsing the entire register
        
        Parameters:
            qubit_index: the 0-indexed qubit position

        Returns:
        '''
        pass

    def initialize_qubit_register_state(self, state):
        '''
        Accepts a string as the state, and sets the internal state vector to the provided state (in basis vector form)

        Parameters:
            state: the binary string

        Returns:
        '''
        self.__state_vector = generate_basis_vector_from_string(state)    # just one state, with amplitude 1

    # Quantum Circuit Operations (will be made into a separate class in future versions)

    def initialize_quantum_circuit(self, starting_state):
        '''
        Accepts a single basis state string and represents it as the input to the circuit

        Parameters: 
            starting_state: basis string

        Returns:
        '''
        for idx, state in enumerate(starting_state):
            self.__circuit_state[idx] = int(state)

if __name__ == '__main__':
    q = QuantumRegister(2)
