# Description: This script is used to generate the results of the simulation.
echo -e "\n $big_dash Getting results of the dataset ... $big_dash"
sh $bash_dir/results_create.sh
tail $simulation_total_time_file | tee -a $results_txt
sh $bash_dir/results_of_input_file.sh $checkin_file
sh $bash_dir/results_of_input_file.sh $social_file
sh $bash_dir/results_of_input_file.sh $traj_file
sh $bash_dir/results_of_input_file.sh $test_file
echo -e "$big_dash Getting results of the dataset ... done $big_dash \n"
