export big_dash="------------------------------------------------------"
export small_dash="---------------------"
echo "$big_dash Exporting variables... $big_dash"
# path to directories:
export bash_dir=$(dirname "$0")
export logs_dir=$PWD
export parent_dir=$(dirname "$PWD")
export data_wrangling_dir="$parent_dir/data_wrangling"
export full_data_dir="$data_wrangling_dir/full_data"
export data_set_dir="$data_wrangling_dir/data_set"

# path to files
export manipulations_json="$(dirname "$parent_dir")/manipulations.json"
export results_txt="$data_set_dir/results.txt"
export info_txt="$data_set_dir/info.txt"
export osf_info_txt="$data_set_dir/osf_info.txt"
export simulation_total_time_file="$logs_dir/pattenrs_of_life.log"

# upload path
export upload_dir="hopper/datapaper/data_set"

# prefix and postfix for files
export file_postfix_all=".all.tsv"
export drive="onedrive"
export zip_size_limit=4500000000 # 5GB in bytes

# creating dates for searching in the dataset
export traj_start_day=0
export test_start_day=$1
export number_of_test_days=14
export total_simulation_days=${2:-$(($1 + $number_of_test_days))}
export simulation_start_time="2019-07-01"
export date_postfix="T00:00:00"
export traj_start_time=$(date -d "$simulation_start_time + $traj_start_day days" "+%Y-%m-%d")
export test_start_time=$(date -d "$simulation_start_time + $test_start_day days" "+%Y-%m-%d")

# Social links
export social_zip_dir="$data_set_dir/social"
export social_links_all="$data_set_dir/SocialNetwork.all.tsv"
export social_file="$data_set_dir/SocialLinks.tsv"
export social_zip="$social_zip_dir/SocialLinks.tsv.zip"
export social_links_prefix="SocialNetwork"

# Trajectory
export traj_zip_dir="$data_set_dir/traj"
export trajectory_table_all="$data_set_dir/AgentStateTable.all.tsv"
export trajectory_table_cut="$data_set_dir/AgentStateTable.cut.tsv"
export traj_file="$data_set_dir/traj.tsv"
export traj_zip="$traj_zip_dir/traj.tsv.zip"
export trajectory_table_prefix="AgentStateTable"

# Checkins
export checkin_zip_dir="$data_set_dir/checkin"
export checkin_all="$data_set_dir/Checkin.all.tsv"
export checkin_file="$data_set_dir/CheckIns.tsv"
export checkin_zip="$checkin_zip_dir/CheckIns.tsv.zip"
export checkin_prefix="Checkin"

# Test
export test_zip_dir="$data_set_dir/test"
export test_file="$data_set_dir/test.tsv"
export test_zip="$test_zip_dir/test.tsv.zip"

echo "$big_dash Exporting variables... done $big_dash"
