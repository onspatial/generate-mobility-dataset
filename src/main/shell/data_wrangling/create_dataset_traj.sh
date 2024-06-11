echo -e "\n $big_dash Creating traj dataset ... $big_dash"
mkdir -p $traj_zip_dir

search_text=$test_start_time$date_postfix
echo $small_dash search_text: $search_text $small_dash

trajectory_table_all_line_number=$(grep -n -m 1 "$search_text" "$trajectory_table_all" | cut -d : -f 1)

if [ -z "$trajectory_table_all_line_number" ]; then
    echo "Warning: trajectory_table_all_line_number is empty"
fi

echo $small_dash trajectory_table_all_line_number: $trajectory_table_all_line_number $small_dash
if [ -z "$trajectory_table_all_line_number" ]; then
    echo "There is no match for the test_start_time: $test_start_time"
    echo "Please check the test_start_time in variables.sh"
    echo "This will cause the test.tsv to be empty"
    cat $trajectory_table_cut >$traj_file

else
    echo $small_dash traj.tsv $small_dash
    head -n $((trajectory_table_all_line_number - 1)) "$trajectory_table_cut" >"$traj_file"
    echo traj_file $traj_file

fi

echo -e "$big_dash Creating traj dataset...  done $big_dash \n"
