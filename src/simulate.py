#!/usr/bin/env python3
import csv
from ez_diffusion import simulate_and_recover

def write_csv(filename, results):
    """
    Write simulation results to a CSV file.
    """
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        # Write header.
        writer.writerow(["N", "Iteration", "a", "v", "t", "R_pred", "M_pred", "V_pred", "a_est", "v_est", "t_est"])
        for res in results:
            writer.writerow([
                res["N"], res["iteration"], res["a"], res["v"], res["t"],
                res["R_pred"], res["M_pred"], res["V_pred"],
                res["a_est"], res["v_est"], res["t_est"]
            ])

def main():
    # For each sample size, run 1000 iterations.
    for N in [10, 40, 4000]:
        results = simulate_and_recover(N, iterations=1000)
        filename = f"simulation_results_N{N}.csv"
        write_csv(filename, results)
        print(f"Results for N = {N} saved to {filename}")

if __name__ == "__main__":
    main()

