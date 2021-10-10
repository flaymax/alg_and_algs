n = int(input())


def gate(operation: str, n_gate: int, input_1: int, input_2=None) -> str:
    
    return {
        
        operation == 'not': 'GATE {} NOT {}'.format(n_gate, input_1),
        operation == 'and': 'GATE {} AND {} {}'.format(n_gate, input_1, input_2),
        operation == 'or': 'GATE {} OR {} {}'.format(n_gate, input_1, input_2),
        operation == 'out': 'OUTPUT {} {}'.format(n_gate, input_1),
    
    }[1]


out = [gate('out', i, i) for i in range(2 ** (2 ** n))]
scheme_dict = {i:{} for i in range(2 ** n + 1)}

for i in range(n):
    elements = set()
    for k in range(2 ** n):
        tmp_bit = k
        for _ in range(i):
            tmp_bit //= 2
        if (tmp_bit % 2) == 1:
            elements.add(k)
    scheme_dict[2 ** (n - 1)][frozenset(elements)] = i

n_gate = n
for i in range(n):
    elements = set()
    for k in range(2 ** n):
        tmp_bit = k
        #tmp_bit = 999
        for _ in range(i):
            tmp_bit //= 2
        if (tmp_bit % 2) == 0:
            elements.add(k)
    scheme_dict[2 ** (n - 1)][frozenset(elements)] = n_gate
    print(gate('not', n_gate, i))
    n_gate += 1

    
    
        
for i in range(2 ** (n - 1) - 1, -1, -1):
    for left_key, input_1 in zip(scheme_dict[2 ** (n - 1)].keys(), 
                                  scheme_dict[2 ** (n - 1)].values()):
        for right_key, input_2 in zip(scheme_dict[i+1].keys(), 
                                  scheme_dict[i+1].values()):
            intersec = left_key & right_key   
            if intersec not in scheme_dict[len(intersec)]:
                scheme_dict[len(intersec)][intersec] = n_gate
                print(gate('and', n_gate, input_1, input_2))
                n_gate += 1

                

for i in range(2, 2 ** n + 1):
    for left_key, input_1 in zip(scheme_dict[1].keys(), 
                                  scheme_dict[1].values()):
        for right_key, input_2 in zip(scheme_dict[i-1].keys(), 
                                  scheme_dict[i-1].values()):            
            union = left_key | right_key # a | b == union
            if union not in scheme_dict[len(union)]:
                scheme_dict[len(union)][union] = n_gate
                print(gate('or', n_gate, input_1, input_2))
                n_gate += 1

    ## OUT ##
for i in out:
    print(i)