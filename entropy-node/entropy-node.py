import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if len(y) == 0:
        return 0.0
    else:
        values, counts = np.unique(y, return_counts=True)
        H=0
        entropy=0
        sum=0
        for i in range(len(counts)):
           sum+=counts[i]
        for i in range(len(counts)):
            p=counts[i]/sum
            entropy+=-p*np.log2(p)
        return entropy
            
            
        
        
    
    