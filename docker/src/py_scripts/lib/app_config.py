# application configuration

# define the URL for the landing page for the local on-prem web application where the web actions will start from
local_web_url = "https://picmidd.nmfs.local/picd/f?p=DSIA"

# define the URL for the landing page for the remote web application where the web actions will start from
remote_web_url = "TBD"

# define the name of the .csv output file that contains the standard metrics/information from the web metrics
csv_output_file = "parr_tools_web_performance_metrics.csv"

# define the prefix for the log file that will be saved in the logs docker volume
log_file_prefix = "parr_tools_log_entries_"

# define the name of the web app that the web actions are being executed
app_name = "PARR Tools Data Set Info App"