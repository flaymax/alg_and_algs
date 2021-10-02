n= int(input())

def gate(operation: str, n_gate: int, input_1: int, input_2=None) -> str:
    
    return {
        
        operation == 'not': 'GATE {} NOT {}'.format(n_gate, input_1),
        operation == 'and': 'GATE {} AND {} {}'.format(n_gate, input_1, input_2),
        operation == 'or': 'GATE {} OR {} {}'.format(n_gate, input_1, input_2),
    
    }[1]

step = 3*n
gates_count = 0
outputs = [i for i in range(2 * n + 2)]

# gates

for i in range(n):
    print(gate('not', step, i))
    
    print(gate('and', step + 1, n + i, 2*n + i))
    print(gate('not', step + 2, step + 1))
    print(gate('or', step + 3, n + i, 2*n + i))
    
    print(gate('and', step + 4, step + 2, step + 3))
    print(gate('and', step + 5, step, step + 4))
    print(gate('not', step + 6, step + 3))
    
    print(gate('or', step + 7, step + 1, step + 6))
    print(gate('and', step + 8, i, step + 7))
    print(gate('or', step + 9, step + 5, step + 8))
    print(gate('and', step + 10, i, step + 4))
    
    print(gate('or', step + 11, step + 1, step + 10))
    gates_count += 12
    step += 12
    
print(gate('and', step, 0, 3 * n))
gates_count += 1
assert gates_count <= 12*n + 1

step = 3*n

# outputs
for i in range(n):
    outputs[i] = step + 9
    outputs[i + n + 2] = step + 9 + 2
    step += 12
outputs[n] = step
outputs[n + 1] = step

a = ['OUTPUT {} {}'.format(i, outputs[i]) for i in range(len(outputs))]

assert len(a) == 2*n +2
for i in a: 
    print(i)
