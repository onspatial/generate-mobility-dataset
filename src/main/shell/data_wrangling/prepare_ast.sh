echo -e "\n $big_dash Preparing data started a $(date)... $big_dash"
if [ -z "$1" ]; then
    echo "Usage: sh prepare_ast.sh <nth day needed>"
    exit 1
fi

days_of_data=$1
source $(dirname "$0")/variables.sh $days_of_data
rm -rf $data_wrangling_dir
ls -lh $data_wrangling_dir
# to make sure the directory exists
mkdir -p $full_data_dir
mkdir -p $data_set_dir
mkdir -p $traj_zip_dir
mkdir -p $test_zip_dir

sh $bash_dir/print_variables.sh
echo "$small_dash AgentStateTable table $small_dash"
sh $bash_dir/append.sh $trajectory_table_prefix
sh $bash_dir/create_dataset_traj.sh
sh $bash_dir/zip_dataset.sh
sh $bash_dir/upload.sh
sh $bash_dir/clean_all.sh
