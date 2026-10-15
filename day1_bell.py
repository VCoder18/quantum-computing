from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# 1. Create a circuit with 2 qubits
qc = QuantumCircuit(2)

# 2. Put qubit 0 into superposition
qc.h(0)

# 3. Entangle qubit 0 and qubit 1
qc.cx(0, 1)

# 4. Measure both qubits
qc.measure_all()

# 5. Draw the circuit
print(qc.draw("text"))

# 6. Run it on the local simulator
sampler = StatevectorSampler()
result = sampler.run([qc], shots=1024).result()

# 7. Get the counts
counts = result[0].data.meas.get_counts()

print("\nMeasurement counts:", counts)