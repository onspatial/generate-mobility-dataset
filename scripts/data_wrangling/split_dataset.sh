echo -e "\n $big_dash Spliting dataset ... $big_dash"

for file in $traj_zip $test_zip $social_zip $checkin_zip; do
    size=$(du -b "$file" | cut -f1)
    if [ $size -gt $zip_size_limit ]; then
        dir=$(dirname "$file")
        base=$(basename "$file")
        echo $small_dash $base is larger than $(($zip_size_limit / (1024 * 1024 * 1024))) GB $small_dash
        echo "Make sure to use lowe than the limits, becuse GB is 1000^3, not 1024^3"
        split -b "$zip_size_limit" "$file" "$dir/$base.part-" && rm "$file"
    else
        echo $small_dash $base is smaller than $(($zip_size_limit / (1024 * 1024 * 1024))) GB $small_dash
        echo "No need to split"
    fi

done

echo -e "$big_dash Spliting dataset...  done $big_dash \n"
