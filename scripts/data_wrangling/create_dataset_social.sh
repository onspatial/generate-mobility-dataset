echo -e "\n $big_dash Creating social links ... $big_dash"
mkdir -p $social_zip_dir

search_text=$test_start_time$date_postfix
echo $small_dash search_text: $search_text $small_dash
social_links_all_line_number=$(grep -n -m 1 "$search_text" "$social_links_all" | cut -d : -f 1)

if [ -z "$social_links_all_line_number" ]; then
    echo "Warning: social_links_all_line_number is empty"
    echo "Trying to find the closest match..."

    test_start_day_temp=$test_start_day

    while [ -z "$social_links_all_line_number" ]; do

        test_start_day_temp=$(($test_start_day_temp + 1))
        if [ $test_start_day_temp -gt $total_simulation_days ]; then
            echo "Reached limit, exiting loop"
            break
        fi
        search_text=$(date -d "$simulation_start_time + $test_start_day_temp days" "+%Y-%m-%d")$date_postfix
        echo $small_dash search_text: $search_text $small_dash
        social_links_all_line_number=$(grep -n -m 1 "$search_text" "$social_links_all" | cut -d : -f 1)

    done

fi

if [ -z "$social_links_all_line_number" ]; then
    echo "There is no match for the test_start_time: $test_start_time"
    echo "Please check the test_start_time in variables.sh"
    echo "This might cause the test.tsv to be empty"
    cat $social_links_all >$social_file
else
    head -n $((social_links_all_line_number - 1)) "$social_links_all" >"$social_file"
fi

echo -e "$big_dash Creating social links...  done $big_dash \n"
