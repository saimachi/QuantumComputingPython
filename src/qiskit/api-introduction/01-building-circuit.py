from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from math import sqrt

# for now, let's execute our code locally
backend = Aer.get_backend('statevector_simulator')

def basic_qubit_initialization():
    # instantiate 1 qubit
    qc = QuantumCircuit(1)

    # by default, the execute method runs and polls the circuit 1,024 times
    result = execute(qc, backend).result()

    # the default state should be |0>, or [1, 0]
    plot_histogram(result.get_counts())
    # calling plt.show() is necessary for me 
    plt.show()

def assign_state():
    qc = QuantumCircuit(1)

    # Problem 1: Create a state vector that will give a  1/3  probability of measuring  |0> 
    q = [1j/sqrt(3), -sqrt(6)/3]
    qc.initialize(q, 0)
    result = execute(qc, backend).result()
    plot_histogram(result.get_counts())
    plt.show()

if __name__ == '__main__':
    # basic_qubit_initialization()
    assign_state()
