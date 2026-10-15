from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4

qc_test = QuantumCircuit(n)
qc_test.h(range(n))
for i, j in edges:
    qc_test.cx(i, j)
    qc_test.rz(0.5, j)  # fixed angle for testing
    qc_test.cx(i, j)

sv = Statevector.from_instruction(qc_test)
# Print the phases of each basis state
for i, amp in enumerate(sv):
    print(f"|{i:04b}⟩: {amp:.3f}")