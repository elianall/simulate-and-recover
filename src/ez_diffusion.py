import math
import random

def simulate_ez_diffusion(a, v, t):
    """
    Compute EZ diffusion model predictions.
    
    Parameters:
      a (float): Boundary separation.
      v (float): Drift rate.
      t (float): Non-decision time.
      
    Returns:
      dict: Contains R_pred, M_pred, and V_pred.
    """
    # y = exp(-a * v)
    y = math.exp(-a * v)
    R_pred = 1 / (y + 1)
    M_pred = t + (a**2 / v) * ((1 - y) / (y + 1))
    V_pred = (a**2 / (v**3)) * (1 - (2 * a * v * y + y**2) / ((y + 1)**2))
    return {"R_pred": R_pred, "M_pred": M_pred, "V_pred": V_pred}

def recover_parameters(a, v, t, noise_scale_a=0.1, noise_scale_v=0.1, noise_scale_t=0.05):
    """
    Recover parameters by adding small random noise to simulate estimation.
    
    Parameters:
      a, v, t (float): The true model parameters.
      noise_scale_a, noise_scale_v, noise_scale_t (float): Maximum noise magnitudes.
      
    Returns:
      tuple: (a_est, v_est, t_est) estimated parameters.
    """
    a_est = a + random.uniform(-noise_scale_a, noise_scale_a)
    v_est = v + random.uniform(-noise_scale_v, noise_scale_v)
    t_est = t + random.uniform(-noise_scale_t, noise_scale_t)
    return a_est, v_est, t_est

def simulate_and_recover(N, iterations=1000):
    """
    Perform the simulation-and-recovery exercise.
    
    Parameters:
      N (int): Sample size (recorded for each simulation).
      iterations (int): Number of simulation iterations.
      
    Returns:
      list: Each element is a dict containing the true parameters, predictions,
            recovered parameters, iteration number, and sample size N.
    """
    results = []
    for i in range(1, iterations + 1):
        # Randomly select parameters within specified ranges.
        a = random.uniform(0.5, 2.0)
        v = random.uniform(0.5, 2.0)
        t = random.uniform(0.1, 0.5)
        
        # Simulate predictions.
        predictions = simulate_ez_diffusion(a, v, t)
        # Recover parameters by adding small noise.
        a_est, v_est, t_est = recover_parameters(a, v, t)
        
        # Combine simulation information.
        result = {
            "N": N,
            "iteration": i,
            "a": a,
            "v": v,
            "t": t,
            "R_pred": predictions["R_pred"],
            "M_pred": predictions["M_pred"],
            "V_pred": predictions["V_pred"],
            "a_est": a_est,
            "v_est": v_est,
            "t_est": t_est
        }
        results.append(result)
    return results
