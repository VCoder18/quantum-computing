from day5_vqe import h2_hamiltonian
from qiskit.circuit.library import efficient_su2, real_amplitudes
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import SLSQP
from qiskit.primitives import StatevectorEstimator


for ansatz_name, ansatz in [
    ("efficient_su2 reps=1", efficient_su2(h2_hamiltonian.num_qubits, reps=1)),
    ("efficient_su2 reps=2", efficient_su2(h2_hamiltonian.num_qubits, reps=2)),
    ("real_amplitudes reps=1", real_amplitudes(h2_hamiltonian.num_qubits, reps=1)),
]:
    vqe = VQE(
        ansatz=ansatz,
        optimizer=SLSQP(maxiter=500),
        estimator=StatevectorEstimator(),
    )
    result = vqe.compute_minimum_eigenvalue(h2_hamiltonian)
    print(f"{ansatz_name}: E = {result.eigenvalue.real:.6f} Hartree")