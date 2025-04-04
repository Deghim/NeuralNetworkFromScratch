
inputs = [1,2,3, 2.5]

weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    ]

biases = [
    2,
    3,
    0.5
]

layer_outputs = []

for neuron_weights, neuron_bias in zip(weights,biases):
    # Zeroed output of given layer
    neuron_output = 0
    # Iteramos por cada input y peso de la neurona
    for n_input, weight in zip(inputs,neuron_weights):
        # Multiplicamos el input por su peso asociado y lo agregamos al resultado que entrega
        neuron_output += n_input*weight
    # Despues del loop, le sumamos el bias
    neuron_output += neuron_bias
    
    # Al final lo agregamos a los resultados
    layer_outputs.append(neuron_output)

print(layer_outputs)