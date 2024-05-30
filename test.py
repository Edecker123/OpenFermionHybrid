from src.openfermion.ops import BosonOperator, FermionOperator, QubitOperator


hamiltonian=BosonOperator(((1,1),(1,0)))
hamiltonian+=BosonOperator(((2,1),(2,0)))

print(hamiltonian)