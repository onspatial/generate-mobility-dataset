echo -e "\n $big_dash Preparing data started a $(date)... $big_dash"
if [ -z "$1" ]; then
    echo "Usage: sh prepare.sh <nth day that manipulation starts>"
    exit 1
fi

manipulation_start_day=$1
source $(dirname "$0")/variables.sh $manipulation_start_day
rm -rf $data_wrangling_dir
ls -lh $data_wrangling_dir
# to make sure the directory exists
mkdir -p $full_data_dir
mkdir -p $data_set_dir
mkdir -p $traj_zip_dir
mkdir -p $test_zip_dir

sh $bash_dir/print_variables.sh

sh $bash_dir/append.sh $checkin_prefix
sh $bash_dir/create_dataset_checkin.sh

# sh $bash_dir/append.sh $social_links_prefix
# sh $bash_dir/create_dataset_social.sh

# echo "$small_dash Trajectory table $small_dash"
# sh $bash_dir/append.sh $trajectory_table_prefix
# echo "$small_dash Cutting trajectory table $small_dash"
# cut -f 2-4 $trajectory_table_all >$trajectory_table_cut
# echo -e "$samll_dash Cutting trajectory table... done $small_dash\n"
# sh $bash_dir/create_dataset_traj.sh
# sh $bash_dir/create_dataset_test.sh

sh $bash_dir/zip_dataset.sh
sh $bash_dir/split_dataset.sh

sh $bash_dir/create_info.sh
sh $bash_dir/create_osf_info.sh
sh $bash_dir/results.sh

sh $bash_dir/print_variables.sh
sh $bash_dir/upload.sh
sh $bash_dir/clean_all.sh

echo -e "$big_dash Preparing data... done at $(date) $big_dash \n"
