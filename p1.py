# A single neuron
"""
    Los inputs son la informacion la cual se entrega a las neuronas para su evaluacion
"""
inputs = [1,2,3] # Building block of a neural network

weights = [0.2, 0.8, -0.5] # Los pesos son los parametros que hacen que la red funcione (o no) 
bias = 2 

output  = (inputs[0]*weights[0]+
           inputs[1]*weights[1]+
           inputs[2]*weights[2]+bias)

print(output)