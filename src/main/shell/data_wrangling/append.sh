#!/bin/bash
# Usage: sh append.sh file_name_prefix
dirs=()
file_name_prefix=$1
echo -e "\n$big_dash Appending $file_name_prefix ... $big_dash"
mkdir -p $data_set_dir

file_out_all=$data_set_dir/$file_name_prefix$file_postfix_all
full_data_zip_files="${file_name_prefix}-*.tsv.zip"
unziped_log="${logs_dir}/${file_name_prefix}.tsv"
echo file_name_prefix: $file_name_prefix
echo logs_dir: $logs_dir
echo unziped_log: $unziped_log

echo $file_out_all
>$file_out_all

for dir in */; do
  dir=${dir%*/}
  dirs+=("$dir")
done
echo ${dirs[@]}
for dir in "${dirs[@]}"; do
  cd $dir
  # first copy and rename the files to make sure they are in order and safe
  sh $bash_dir/rename_copy.sh $file_name_prefix
  cd ..
done

# remove the old files
echo removing the old files
rm $full_data_dir/*.tsv
echo "ls $full_data_dir/:"
ls $full_data_dir/
echo you should not see any tsv file

echo "$small_dash changing directory to $full_data_dir ... $small_dash"
cd $full_data_dir
pwd

file_processed_counter=0

echo $small_dash Working on archived folders... $small_dash
>$file_out_all
echo $small_dash HEADER MIGHT NOT BE WRITTEN PROPERLY $small_dash
for zip_file in ${file_name_prefix}*.zip; do
  echo $small_dash $file_name_prefix $small_dash
  unzip "$zip_file" "$file_name_prefix-*.tsv" -d $full_data_dir/
  echo unzipping $zip_file ... done
  file=$(ls ${file_name_prefix}-*.tsv 2>/dev/null)
  echo $file is unzipped
  echo "$small_dash appending original.log.txt $small_dash"
  head -n 1 "$file" | tee -a $file_out_all.original.log.txt
  tail -n 1 "$file" | tee -a $file_out_all.original.log.txt
  echo integrating the $file ...
  sed -n '1,$p' "$file" >>$file_out_all
  #   echo "$small_dash appending append.log.txt $small_dash"
  # head -n 1 <(sed -n '1,$p' "$file") | tee -a $file_out_all.append.log.txt
  # tail -n 1 <(sed -n '1,$p' "$file") | tee -a $file_out_all.append.log.txt

  echo removing $file ...
  rm $file
  file_processed_counter=$((file_processed_counter + 1))
done

echo $small_dash archive done $small_dash

echo unziped_log: $unziped_log
echo file_out_all: $file_out_all

head -n 1 "$unziped_log" | tee -a $file_out_all.original.log.txt
tail -n 1 "$unziped_log" | tee -a $file_out_all.original.log.txt

echo integrating the $unziped_log ...
sed -n '1,$p' $unziped_log >>$file_out_all
# head -n 1 <(sed -n '1,$p' $unziped_log) | tee -a $file_out_all.append.log.txt
# tail -n 1 <(sed -n '1,$p' $unziped_log) | tee -a $file_out_all.append.log.txt

file_processed_counter=$((file_processed_counter + 1))
echo $small_dash $file_processed_counter files processed $small_dash
echo -e "$big_dash appending $file_name_prefix ... done $big_dash\n"
