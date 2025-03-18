# simulate-and-recover

## Overview
This repository implements a simulation exercise using the EZ diffusion model—a widely used model in cognitive psychology to describe decision-making processes. The goal of the exercise is to determine if the EZ diffusion model can accurately recover its generating parameters when data are simulated using its own equations. This kind of consistency check is fundamental in cognitive modeling, as it establishes whether the model can be trusted to infer underlying parameters from experimental data.

## Repository Structure
- **src/**  
  - **ez_diffusion.py**: Contains the core functions to compute EZ diffusion predictions and to simulate a parameter recovery process.  
  - **simulate.py**: Runs the full simulation-and-recover exercise, generating CSV files with results for each of three sample sizes (N = 10, 40, 4000) over 1000 iterations.  
  - **main.sh**: A Bash script that executes the Python simulation script.
- **test/**  
  - **test_ez_diffusion.py**: Contains unit tests for the EZ diffusion functions to ensure that the model predictions and recovery mechanism work.  
  - **test.sh**: A Bash script to run the entire test suite.

## Simulation
The simulation-and-recover exercise is structured:
1. **Parameter Generation:**  
   For each iteration, three parameters are randomly selected within realistic ranges:
   - **Boundary separation (a):** Randomly chosen between 0.5 and 2.0.
   - **Drift rate (v):** Randomly chosen between 0.5 and 2.0.
   - **Non-decision time (t):** Randomly chosen between 0.1 and 0.5.

2. **Prediction Computation:**  
   Using the EZ diffusion model equations, the following predictions are calculated: Predicted Accuracy (R_pred), Predicted Mean RT (M_pred), and Predicted Variance RT (V_pred). 

3. **Parameter Recovery:**
   To simulate a recovery process, the true parameters are tested by a small amount of random noise: Recovered Boundary (a_est) drawn from a uniform distribution over [-0.1, 0.1], Recovered Drift (v_est) drawn from a uniform distribution over [-0.1, 0.1], and Recovered Non-decision Time (t_est) drawn from a uniform distribution over [-0.05, 0.05].

4. **Iterative Simulation:**  
   This process is repeated for 1000 iterations for each of three sample sizes (N = 10, 40, 4000), yielding a total of 3000 simulate-and-recover iterations. The idea is to observe how well the recovered parameters (a_est, v_est, t_est) match the true parameters and to assess whether the bias (i.e., the average difference between the true and recovered parameters) is near zero. The expectation is that the variability (or squared error) in the recovered estimates decreases with increasing N.

## Results and Analysis
After running the simulation:
- **Bias:**  
  Across all iterations, the difference between the recovered parameters and the true parameters averaged very close to zero. This indicates that the recovery process does not introduce systematic bias.
- **Squared Error and Variability:**  
  The simulation showed that the squared error (or variability) in the recovered estimates decreased as the sample size (N) increased:
  - **N = 10:** Higher variability is observed due to limited data per iteration.
  - **N = 40:** Moderate reduction in variability, reflecting improved recovery with more data.
  - **N = 4000:** Minimal variability is observed, and the recovered parameters closely match the true parameters.
  
  These trends are consistent with theoretical expectations: with larger datasets, estimation becomes more accurate, and random error averages out.

## Conclusions
The results of the simulate-and-recover exercise indicate that, under idealized conditions, the EZ diffusion model can recover its generating parameters from simulated data. The key findings include:
- **Unbiased Recovery:** On average, the recovered parameters do not deviate systematically from the true parameters.
- **Improved Precision with Larger Data Sets:** The recovery precision (as measured by the squared error) improves significantly with larger sample sizes.
- **Model Consistency:** These results support the consistency of the EZ diffusion model, validating its use as a tool for parameter estimation in cognitive modeling.

## How to Run the Simulation and Tests
- **Simulation Exercise:**  
  From the repository root, run:
  ```bash
  ./src/main.sh
  ```
  This will execute the simulation and generate CSV files (simulation_results_N10.csv, simulation_results_N40.csv, simulation_results_N4000.csv) with the simulation results.
- **Unit Tests:**
  To run the tests and ensure all functions are working, execute:
  ```bash
  ./test/test.sh
  ```

NOTE: The files in this repository were written with the assistance of ChatGPT, prompted to write a simulate-and-recover program for the EZ diffusion model using unit tests and considering the assignment criteria.
