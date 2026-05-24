class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        # We also do our original calculation, so we can update it
        curr = init 

        
        # We first create our loop with the number of steps tht we need to take
        for i in range(iterations):
            # After that, we then take our inital value, then iterate again
            curr = curr - learning_rate * (2 * curr)
        
        # After completing all of the iterations, we then return our result
        return round(curr, 5)