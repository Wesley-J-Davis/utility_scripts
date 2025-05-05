#!/bin/bash

# Define a list of variables
variables=("param1" "param2" "param3" "param4")

# Iterate through each variable and submit a job
for var in "${variables[@]}"; do
    echo "Submitting job with variable: $var"
    
    sbatch --export=MYVAR=$var my_slurm_script.sh
done

echo "All jobs submitted!"
