files=($(find ./ -type f))
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        zip -j "${file}.zip" "$file"
    fi
done
