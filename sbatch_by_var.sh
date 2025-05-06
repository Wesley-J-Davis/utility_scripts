#!/bin/bash
while read -r item; do
    echo "Executing script for: $item"
    ./my_script.sh "$item"
done < list.txt
# Define a list of variables

#!/bin/bash
#var=$1
#sbatch --export=MYVAR=$var my_slurm_script.sh
