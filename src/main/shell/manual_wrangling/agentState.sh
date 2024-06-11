#!/bin/bash
dirs=()
root_dir=$(pwd)
output_file=$root_dir/full.data.tsv
prefix=$1
echo $output_file
>$output_file

for dir in */; do
  dir=${dir%*/}
  dirs+=("$dir")
done

for dir in "${dirs[@]}"; do

  cd $dir
  # frist rename all the zip files
  for oldname in $prefix-*.tsv.zip; do
    num=$(echo $oldname | awk -F '[.-]' '{printf "%03d", $2}')
    newname="${prefix}-${num}.tsv.zip"

    if [ -e "$newname" ]; then
      echo "Error: $newname already exists."
    else
      mv -- "$oldname" "$newname"
    fi
  done

  rm *.tsv # remove the old files
  ls
  echo you should not see any tsv file

  for file in $prefix-*.tsv.zip; do
    unzip "$file"

    first_file=1
    for file in *.tsv; do
      if [ $file != $output_file ]; then
        echo integrating the $file ...
        if [ $first_file -eq 1 ]; then
          cat "$file" >>$output_file
          first_file=0
        else
          tail -n +2 "$file" >>$output_file
        fi
        rm $file
      fi
    done

  done

  cd ..
done

tail -n +2 $prefix.tsv >>$output_file
