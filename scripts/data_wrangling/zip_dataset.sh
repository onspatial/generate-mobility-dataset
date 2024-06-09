source $bash_dir/functions.sh
echo -e "\n $big_dash Zipping dataset ... $big_dash"
mkdir -p $traj_zip_dir
mkdir -p $test_zip_dir
mkdir -p $social_zip_dir
mkdir -p $checkin_zip_dir

zip_and_keep $traj_zip $traj_file
zip_and_keep $test_zip $test_file
zip_and_keep $social_zip $social_file
zip_and_keep $checkin_zip $checkin_file

echo -e "$big_dash Zipping dataset...  done $big_dash \n"
