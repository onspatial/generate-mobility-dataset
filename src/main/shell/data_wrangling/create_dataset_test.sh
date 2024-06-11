echo -e "\n $big_dash Creating test dataset ... $big_dash"
mkdir -p $test_zip_dir

search_text=$test_start_time$date_postfix

echo $small_dash search_text: $search_text $small_dash
echo $small_dash trajectory_table_all: $trajectory_table_all $small_dash
trajectory_table_all_line_number=$(grep -n -m 1 "$search_text" "$trajectory_table_all" | cut -d : -f 1)

if [ -z "$trajectory_table_all_line_number" ]; then
    echo "Warning: trajectory_table_all_line_number is empty"
fi

echo $small_dash trajectory_table_all_line_number: $trajectory_table_all_line_number $small_dash
if [ -z "$trajectory_table_all_line_number" ]; then
    echo "There is no match for the test_start_time: $test_start_time"
    echo "Please check the test_start_time in variables.sh"
    echo "This will cause the test.tsv to be empty"

else
    echo $small_dash test.tsv $small_dash
    head -n 1 "$trajectory_table_cut" >"$test_file"
    sed -n "$trajectory_table_all_line_number,\$p" "$trajectory_table_cut" >>"$test_file"
fi

echo -e "$big_dash Creating test dataset...  done $big_dash \n"
