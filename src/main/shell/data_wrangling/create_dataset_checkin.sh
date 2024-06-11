echo -e "\n $big_dash Creating dataset ... $big_dash"
mkdir -p $checkin_zip_dir

search_text=$test_start_time$date_postfix
echo $small_dash search_text: $search_text $small_dash
checkin_all_line_number=$(grep -n -m 1 "$search_text" "$checkin_all" | cut -d : -f 1)

if [ -z "$checkin_all_line_number" ]; then
    echo "Warning: checkin_all_line_number is empty"
    echo "Trying to find the closest match..."

    test_start_day_temp=$test_start_day

    while [ -z "$checkin_all_line_number" ]; do

        test_start_day_temp=$(($test_start_day_temp + 1))
        if [ $test_start_day_temp -gt $total_simulation_days ]; then
            echo "Reached limit, exiting loop"
            break
        fi
        search_text=$(date -d "$simulation_start_time + $test_start_day_temp days" "+%Y-%m-%d")$date_postfix
        echo $small_dash search_text: $search_text $small_dash
        checkin_all_line_number=$(grep -n -m 1 "$search_text" "$checkin_all" | cut -d : -f 1)

    done

fi
echo $small_dash checkin_all_line_number: $checkin_all_line_number $small_dash
if [ -z "$checkin_all_line_number" ]; then
    echo "There is no match for the test_start_time: $test_start_time"
    echo "Please check the test_start_time in variables.sh"
    echo "This might cause the test.tsv to be empty"

    cat $checkin_all >$checkin_file
else
    head -n $((checkin_all_line_number - 1)) "$checkin_all" >"$checkin_file"
fi

echo -e "$big_dash Creating dataset...  done $big_dash \n"
