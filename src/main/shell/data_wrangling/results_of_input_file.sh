# Example: sh results_of_input_file.sh AgentStateTable.all.tsv
if [ -z "$1" ]; then
    echo "Error: sh results_of_input_file.sh input_file_name"
    exit 1
fi

input_file_name=$1

echo "$small_dash  Counting for the $(basename $input_file_name) $small_dash " | tee -a $results_txt
wc $input_file_name | tee -a $results_txt
ls -lh $input_file_name | tee -a $results_txt
echo -e "$small_dash Counting for the $(basename $input_file_name) done $samll_dash\n" | tee -a $results_txt
