
# A single neuron
"""
    Los inputs son la informacion la cual se entrega a las neuronas para su evaluacion
"""
"""
inputs = [1,2,3, 2.5] # Building block of a neural network

weights = [0.2, 0.8, -0.5, 1.0] # Los pesos son los parametros que hacen que la red funcione (o no) 
bias = 2 

output  = (inputs[0]*weights[0]+
           inputs[1]*weights[1]+
           inputs[2]*weights[2]+
           inputs[3]*weights[3]+bias)

print(output)
"""

"""
    La neurona utiliza los inputs para calcular el output, el resultado depende del peso de ese valor y el bias que se le tiene al mismo
"""

# Asi mismo se es posible utilzar la libreria de numpy para simplificar la sintaxis de las operaciones
import numpy as np

inputs = [1,2,3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2 

output = np.dot(inputs, weights) + bias
# output = np.dot([1,2,3, 2.5], [0.2, 0.8, -0.5, 1.0]) + bias

print(output)