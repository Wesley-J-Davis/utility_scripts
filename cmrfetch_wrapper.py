# CMR Fetch Wrapper
import pandas as pd
import os
import sys
beg_date = sys.argv[1]
end_date = sys.argv[2]
date_range = beg_date + '_' + end_date
def cmr_fetch_wrapper(date_range):
  script_path = "/path/to/cmrfetch"
  command = f"/what/runs/cmrfetch/?/ ${script_path} ${date_range}"
  system_response = os.system(command)
  return system_response

query_answer = cmr_fetch_wrapper(date_range) 

if empty(query_answer)
  date_sequence = pd.date_range("2020-01-06", "2020-04-03", freq="m")
  for dtg in date_sequence
    cmr_fetch_wrapper(dtg)
