#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""BosonOperator stores a sum of products of bosonic ladder operators."""

from src.openfermion.ops.operators.symbolic_operator import SymbolicOperator
from src.openfermion.ops.operators.fermion_operator import FermionOperator
from src.openfermion.ops.operators.qubit_operator import QubitOperator

import sympy
COEFFICIENT_TYPES = (int, float, complex, sympy.Expr)

class GeneralOperator(SymbolicOperator):
    @property
    def actions(self):
        """The allowed actions."""
        return (3 , 2 , 1, 0 , 'X', 'Y', 'Z')

    @property
    def action_strings(self):
        """The string representations of the allowed actions."""
        return ('^', '','^', '', 'X','Y','Z')

    @property
    def action_before_index(self):
        """Whether action comes before index in string representations."""
        return False

    @property
    def different_indices_commute(self): #TODO change that it remains true unless we compute on fermions 
        """Whether factors acting on different indices commute."""
        return False

    def is_normal_ordered(self):
        """Return whether or not term is in normal order.

        In our convention, ladder operators come first.
        Note that unlike the Fermion operator, due to the commutation
        of ladder operators with different indices, the BosonOperator
        sorts ladder operators by index.
        """
        for term in self.terms:
            for i in range(1, len(term)):
                for j in range(i, 0, -1):
                    right_operator = term[j]
                    left_operator = term[j - 1]
                    if (
                        right_operator[0] == left_operator[0]
                        and right_operator[1] > left_operator[1]
                    ):
                        return False
        return True


    