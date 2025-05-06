#sbatch -J MyJob -o output.log -e error.log -N 2 -n 8 -t 02:00:00 my_script.sh

Basic Options
-J jobname → Set the job name.

-o output_file → Specify the output file for job logs.

-e error_file → Specify the error file for job logs.

-N num_nodes → Request a specific number of nodes.

-n num_tasks → Specify the number of tasks (processes).

-c num_cores → Request a certain number of CPU cores per task.

-t time → Set the time limit (e.g., -t 02:00:00 for 2 hours).

-p partition → Specify the partition (queue) for the job.

--mail-type=type → Set email notifications (BEGIN, END, FAIL, ALL).

--mail-user=email → Email address for notifications.

Resource Allocation Options
--mem=MB → Request memory in megabytes.

--mem-per-cpu=MB → Set memory per allocated CPU.

--gres=gpu:N → Request N GPUs per node.

--constraint=features → Specify hardware constraints (e.g., --constraint=skylake).

--exclusive → Request exclusive node use.

Job Dependencies & Arrays
--dependency=afterok:jobid → Start after a job completes successfully.

--dependency=afternotok:jobid → Start after a job fails.

--array=start-end → Run a job array (e.g., --array=1-10 for 10 tasks).

Environment & Execution
--export=VAR=value → Pass environment variables.

--chdir=dir → Change to a specific directory before executing the script.

--test-only → Validate the job script without submitting.

--account=account → Specify the Slurm account for billing purposes.
