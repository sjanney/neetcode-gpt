import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        
        # Subtract max for numerical stability
        z = z - np.max(z)

        # Compute exponentials
        exp_vals = np.exp(z)

        # Divide by sum of exponentials
        softmax_vals = exp_vals / np.sum(exp_vals)

        return np.round(softmax_vals, 4)
