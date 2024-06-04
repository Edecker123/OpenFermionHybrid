from src.openfermion.ops import FermionOperator, BosonOperator, QubitOperator, SymbolicOperator

# Define theta
theta = 1  # Define the value of theta here

# Displacement
displacement =QubitOperator('Z0', -1j * theta) 
if isinstance(displacement, SymbolicOperator):
    print(True)
displacement+=(BosonOperator('0^') + BosonOperator('0'))

# Doubly-controlled rotation
doubly_controlled_rotation = QubitOperator('Z0 Z1', -1j * theta) * BosonOperator('0^ 0')

# Spin-Holstein dynamics
spin_holstein_dynamics = -1j * theta
for i, n in [(10, 10)]:  # Define the indices for i and n
    spin_holstein_dynamics *= BosonOperator(f'{n}^') + BosonOperator(f'{n}') * QubitOperator(f'Z{i}', 1)

# Fermionic string
fermionic_string = QubitOperator('Z0 Z1 Z2', -1j * theta) * (QubitOperator('X3') - 1j * QubitOperator('Y3'))

# Hubbard-Holstein dynamics
hubbard_holstein_dynamics =-1j * theta
t = 1
g = 1

for i, j in [(1,1),(2,3),(4,5)]:  # Define the indices for i and j
    hubbard_holstein_dynamics += FermionOperator(f'{i}^ {j}', -1j * t) + FermionOperator(f'{j}^ {i}', 1j * t)
    
for i in range(1,3):  # Define the indices for i
    hubbard_holstein_dynamics += BosonOperator(f'{i}^') + BosonOperator(f'{i}', -1j * g)

for q in range(1,3):  # Define the indices for q
    hubbard_holstein_dynamics += BosonOperator(f'{q}^ {q}', -1j * theta)

# Schwinger-boson plaquette term
schwinger_boson_plaquette_term = QubitOperator('', -1j * theta)
schwinger_boson_plaquette_term += BosonOperator('1^ 2 3^ 4 5 6^ 7 8^') + BosonOperator('1 2^ 3 4^ 5^ 6 7^ 8')

# Print the Hamiltonians
print("Displacement:", displacement)
print("Doubly-controlled rotation:", doubly_controlled_rotation)
print("Spin-Holstein dynamics:", spin_holstein_dynamics)
print("Fermionic string:", fermionic_string)
print("Hubbard-Holstein dynamics:", hubbard_holstein_dynamics)
print("Schwinger-boson plaquette term:", schwinger_boson_plaquette_term)