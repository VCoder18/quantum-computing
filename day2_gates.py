from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run(qc, shots=1024, label=""):
    qc.measure_all()
    sampler = StatevectorSampler()
    counts = sampler.run([qc], shots=shots).result()[0].data.meas.get_counts()
    print(f"{label}: {counts}")
    return counts

qc = QuantumCircuit(1)
qc.x(0)
run(qc, label="X on 0")

qc = QuantumCircuit(1)
qc.h(0)
run(qc, label="H on 0")

qc = QuantumCircuit(1)
qc.h(0)
qc.z(0)
qc.h(0)
run(qc, label="HZH on 0")

qc = QuantumCircuit(1)
qc.h(0)
qc.s(0)
qc.h(0)
run(qc, label="HSH on 0")

qc = QuantumCircuit(1)
qc.h(0)
qc.t(0)
qc.h(0)
run(qc, label="HTH on 0")

import numpy as np

qc = QuantumCircuit(1)
qc.ry(np.pi/3, 0)
run(qc, label="Ry(pi/3) on 0")

qc = QuantumCircuit(1)
qc.rx(np.pi/3, 0)
run(qc, label="Rx(pi/3) on 0")

qc = QuantumCircuit(1)
qc.rz(np.pi/3, 0)
qc.h(0)
run(qc, label="Rz(pi/3) then H on 0")