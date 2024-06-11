echo "$big_dash Copying files... $big_dash"

if [ -z "$1" ]; then
   echo "Usage: sh rename_copy.sh input_prefix"
   exit 1
fi
input="$1"

current_directory=${PWD##*/}
echo "Current directory: $current_directory"
for oldname in $input-*.tsv.zip; do

   num=$(echo $oldname | awk -F '[.-]' '{printf "%04d", $2}')
   newname="${input}-${current_directory}-${num}.tsv.zip"

   if [ -e "$newname" ]; then
      echo "Error: $newname already exists."
   else
      cp -- "$oldname" "$full_data_dir/$newname"
      echo "Copying $oldname to    $full_data_dir/$newname"
   fi
done

echo "$big_dash Copying files...done $big_dash"
