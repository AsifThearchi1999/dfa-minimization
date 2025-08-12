def hopcroft_minimize(accepting_states, input_alphabet, inverse_transition_func):
    # Step 1: Collect all states
    all_states = set(accepting_states)
    for (_, state), preds in inverse_transition_func.items():
        all_states.add(state)
        all_states.update(preds)
    
    # Step 2: Initial partitions
    non_accepting = all_states - accepting_states
    P = []
    if accepting_states:
        P.append(frozenset(accepting_states))
    if non_accepting:
        P.append(frozenset(non_accepting))
    
    # Rest of the implementation...
    # [Include the full implementation I provided earlier]
    return {frozenset(block) for block in P}
