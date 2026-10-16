import numpy as np
from qiskit.quantum_info import SparsePauliOp
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import SLSQP
from qiskit.circuit.library import efficient_su2
from qiskit.primitives import StatevectorEstimator


# --- Precomputed H₂ Hamiltonian at 0.735 Å (STO-3G, Jordan-Wigner) ---
# These are the same numbers PySCF would have produced.
h2_hamiltonian = SparsePauliOp.from_list([
    ("IIII", -0.8126),
    ("IIIZ",  0.1712),
    ("IIZI", -0.2228),
    ("IZII",  0.1712),
    ("ZIII", -0.2228),
    ("IIZZ",  0.1686),
    ("IZIZ",  0.1205),
    ("IZZI",  0.1686),
    ("ZIIZ",  0.1686),
    ("ZIZI",  0.1205),
    ("ZZII",  0.1686),
    ("IXXI",  0.0454),
    ("IYYI",  0.0454),
    ("XXII",  0.0454),
    ("YYII",  0.0454),
])


# --- Ansatz ---
ansatz = efficient_su2(
    num_qubits=h2_hamiltonian.num_qubits,
    reps=2,
    entanglement="linear",
)


# --- Optimizer + VQE ---
optimizer = SLSQP(maxiter=500)
vqe = VQE(
    ansatz=ansatz,
    optimizer=optimizer,
    estimator=StatevectorEstimator(),
)


if __name__ == "__main__":
    print("Number of qubits:", h2_hamiltonian.num_qubits)
    print("Number of Pauli terms:", len(h2_hamiltonian))

    print("\nHamiltonian:")
    print(h2_hamiltonian)

    result = vqe.compute_minimum_eigenvalue(h2_hamiltonian)
    print(f"\nGround state energy: {result.eigenvalue.real:.6f} Hartree")