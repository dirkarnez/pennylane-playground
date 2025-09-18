import pennylane as qml
import numpy as np

def my_quantum_function(x, y):
    qml.RZ(x, wires=0)
    qml.CNOT(wires=[0,1])
    qml.RY(y, wires=1)
    return qml.expval(qml.Z(wires=1))

dev_unique_wires = qml.device('default.qubit', wires=['aux', 'q1', 'q2'])
circuit = qml.QNode(my_quantum_function, dev_unique_wires)
print(qml.draw(circuit)(np.pi/4, 0.7))