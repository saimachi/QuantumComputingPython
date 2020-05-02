import argparse
from qiskit import IBMQ

parser = argparse.ArgumentParser()
parser.add_argument('--key', '-k', required=True, 
                    help='key from IBM Quantum Experience')
args = parser.parse_args()

IBMQ.save_account(args.key)
