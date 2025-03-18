# simulate-and-recover

# Simulate and Recover Assignment

## Overview
This repository implements a simulation exercise using the EZ diffusion model—a cognitive model for decision making. The goal is to assess whether the EZ diffusion model can recover its generating parameters from simulated data. The simulation involves generating model predictions based on randomly chosen parameters, and then “recovering” those parameters by adding a small perturbation. Over many iterations, one should observe that the bias is close to 0 and that the squared error decreases with larger sample sizes.

## Repository Structure
- **src/**  
  - **ez_diffusion.py**: Contains functions to compute EZ diffusion predictions and to “recover” parameters by adding noise.
  - **simulate.py**: Uses the EZ diffusion functions to perform the simulation-and-recovery exercise over 1000 iterations for each of three sample sizes (N = 10, 40, and 4000) and writes the results to CSV files.
  - **main.sh**: A bash script that runs the full simulation by calling the Python simulation script.
- **test/**  
  - **test_ez_diffusion.py**: Unit tests for the EZ diffusion functions.
  - **test.sh**: A bash script to run the test suite.

Assignment is written with assistance of ChatGPT, prompted to write a simulate and recover program for the EZ diffusion model using unit tests to define the EZ Diffusion model. 

## How to Run
- To run the complete simulation exercise, execute:
  ```bash
  ./src/main.sh
