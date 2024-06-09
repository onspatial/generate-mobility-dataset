source $bash_dir/functions.sh
echo -e "\n $big_dash Uploading data to $drive... $big_dash"

upload_file $results_txt
upload_file $info_txt
upload_file $osf_info_txt
upload_file $manipulations_json
upload_file $checkin_zip_dir
upload_file $social_zip_dir
upload_file $traj_zip_dir
upload_file $test_zip_dir

# After all finished, upload all log.txt files
for file in *.log.txt; do
    rclone copy $file $drive:"$upload_dir/$file"
done

echo -e "$big_dash Uploading data to $drive... done $big_dash \n"
