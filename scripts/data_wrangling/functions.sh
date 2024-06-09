upload_file() {
    if [ -z "$drive" ]; then
        echo "drive is not set $drive"
        exit 1
    fi
    local file=$1
    extracted_path=$(echo $file | cut -d'/' -f4-6 | tr '/' '-')
    reverse_str=$(echo "$extracted_path" | tr '-' '\n' | tac | tr '\n' '-')
    file_dir=${reverse_str::-1}
    if [ -e "$file" ]; then
        echo "uploading $file to $drive:\"$upload_dir/$file_dir\""
        rclone copy $file $drive:"$upload_dir/$file_dir"
    else
        echo "Failed to upload! $file does not exist"
    fi
}

zip_and_remove() {
    local zip=$1
    local file=$2
    if [ -f "$file" ]; then
        echo $small_dash ziping $(basename $file) $small_dash
        zip $zip $file && rm $file
    fi
}

zip_and_keep() {
    local zip=$1
    local file=$2
    if [ -f "$file" ]; then
        echo $small_dash ziping $(basename $file) $small_dash
        zip $zip $file
    fi
}
