import numpy as np
import math

class ComputationalBasis:
    '''
    A vector that represents a given binary string

    Parameters:
        binary_string: the binary string to be represented
    '''
    def __init__(self, binary_string):
        self.__compute_basis_vector(binary_string)

    def __compute_basis_vector(self, binary_string):
        '''
        Convert a binary string to the equivalent basis vector
        E.g. "10" to [0 0 1 0]

        Parameters:
            binary_string

        Returns:
        '''
        if len(binary_string) == 1:
            if binary_string == '0':
                self.vector_representation = np.array([1, 0])
            else:
                self.vector_representation = np.array([0, 1]) 
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
            self.vector_representation = prod

class QuantumRegister:
    '''
    Represents an n qubit quantum register
    Default state is Hadamard transform

    Parameters:
        n: the size of the register (bits)
    '''
    def __init__(self, n):
        self.n = n
        self.__state_vector = math.sqrt(1 / 2 ** n) * np.ones((1, 2 ** n))

    def view_register_state(self):
        '''
        Collapse and view the state stored in the register 

        Parameters:

        Returns: 
        '''
        pass

    def view_single_qubit_state(self, qubit_index):
        '''
        View the state of an individual qubit without collapsing the entire register

        Parameters:
            qubit_index: the 0-indexed qubit position

        Returns:
        '''
        pass
    
    def general_unitary_transform(self, transform):
        '''
        Applies a unitary transformation matrix of length 2^n by 2^n to the state vector
        This transformation matrix can be the product of multiple unitary gates

        Parameters:
            transform: the transformation matrix

        Returns: 
        '''
        pass

if __name__ == '__main__':
    q = QuantumRegister(2)
