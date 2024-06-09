for file in *; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo $filename >>$file
    fi
done
