import numpy as np

def entropy_node(y):
    if len(y) == 0:
        return 0.0  # ✅ handle edge case

    values, counts = np.unique(y, return_counts=True)
    probs = counts / counts.sum()
    return float(-np.sum(probs * np.log2(probs)))