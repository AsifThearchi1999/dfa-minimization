def hopcroft_minimize(accepting_states, input_alphabet, inverse_transition_func):
    """
    Minimize a DFA using Hopcroft's algorithm.
    
    Args:
        accepting_states: set of accepting states
        input_alphabet: set of input symbols
        inverse_transition_func: dict mapping (symbol, state) to set of predecessor states
        
    Returns:
        Set of frozensets representing the equivalence classes of states
    """
    # Step 1: Collect all states from both accepting states and transition function
    all_states = set(accepting_states)
    for (_, state), preds in inverse_transition_func.items():
        all_states.add(state)
        all_states.update(preds)
    
    # Step 2: Initialize partitions (accepting vs non-accepting)
    non_accepting = all_states - accepting_states
    P = []
    if accepting_states:
        P.append(frozenset(accepting_states))
    if non_accepting:
        P.append(frozenset(non_accepting))
    
    # Step 3: Initialize worklist with the smaller partition
    W = []
    if len(accepting_states) <= len(non_accepting):
        if accepting_states:
            W.append(frozenset(accepting_states))
    else:
        if non_accepting:
            W.append(frozenset(non_accepting))
    
    # Convert to mutable sets for processing
    P = [set(block) for block in P]
    W = [set(block) for block in W]
    
    # Step 4: Process worklist until empty
    while W:
        A = W.pop()
        
        for c in input_alphabet:
            # Find all predecessors of A on symbol c
            X = set()
            for s in A:
                X.update(inverse_transition_func.get((c, s), set()))
            if not X:
                continue
            
            # Check each block in P for splitting
            new_P = []
            for Y in P:
                intersect = Y & X
                difference = Y - X
                
                if intersect and difference:
                    # Split Y into two parts
                    new_P.append(intersect)
                    new_P.append(difference)
                    
                    # Update worklist
                    if Y in W:
                        W.remove(Y)
                        W.append(intersect)
                        W.append(difference)
                    else:
                        # Add the smaller split to worklist
                        if len(intersect) <= len(difference):
                            W.append(intersect)
                        else:
                            W.append(difference)
                else:
                    new_P.append(Y)
            
            P = new_P
    
    # Convert back to immutable frozensets
    return {frozenset(block) for block in P}
