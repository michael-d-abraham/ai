# This defines the rules of the Wolf–Goat–Cabbage puzzle.

# It says:

# what the starting state is,

# what a “goal” looks like,

# what actions you can take from a state,

# how to apply an action to get a new state.

# It’s the “content” or “world” that the search algorithm explores.


def actions(state):
    F,W,G,C = state
    side = F
    acts = [("F",)]   # farmeralone
    if W == side: acts.append(("F", "W"))
    if G == side: acts.append(("F", "G"))
    if C == side: acts.append(("F", "C"))
    return acts

def flip(x):
    return 1 - x

def transition(state, acts):
    F, W, G, C = state
    if acts == ("F",):
        return (flip(F), W, G, C)
    if acts == ("F", "W"):
        return (flip(F), flip(W), G, C)
    if acts == ("F", "G"):
        return (flip(F), W, flip(G), C)
    if acts == ("F", "C"):
        return (flip(F), W, G, flip(C))

def valid(s):
    F,W,G,C = s

    # if wolf and golf are together and F side isn't on the same side
    if (W == G) and (F != W):
        return False
    
    # if goat and cabbage are together and farmer is on other staticmethod
    if (G == C) and (F !=G):
        return False
    
    # All others are true
    return True 
    


