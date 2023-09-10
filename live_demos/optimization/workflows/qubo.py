# This code is part of Qiskit.
#
# (C) Copyright IBM 2023
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
QUBO workflow
"""
from optimization.passes import (InequalityToEquality,
                                 IntegerToBinary,
                                 LinearEqualityToPenalty,
                                 LinearInequalityToPenalty,
                                 MaximizeToMinimize,
                                 EvaluateProgramSolution,
                                 UnrollQUBOVariables
                                 )
from optimization.fulqrum import Workflow


def QuadraticConverter():
    return Workflow([InequalityToEquality(), # Transformation
                     IntegerToBinary(), # Transformation
                     LinearEqualityToPenalty(), # Transformation
                     LinearInequalityToPenalty(), # Transformation
                     MaximizeToMinimize(), # Transformation
                    ], name='quadratic-converter')


def QuadraticPostprocess(qubo, quadratic_transformer):
    return Workflow([EvaluateProgramSolution(qubo),
                     UnrollQUBOVariables(quadratic_transformer),
                    ], name='quadratic-postprocess')