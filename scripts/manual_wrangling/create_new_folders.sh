part1=("ATL" "GMU" "NOLA" "SFCO")
part2=("1K" "3K" "5K" "10K")
part3="15mo"
file_name="README.txt"
folder_init="Created on $(date +%Y-%m-%d) by Hossein Amiri
Each folder contains a file called traj.tsv.zip, which is the compressed version of the traj.tsv file. If the file is split into multiple parts, these parts are named traj.tsv.zip.part-aa, traj.tsv.zip.part-ab, etc.
To concatenate these parts, you can use the cat command in Linux or utilize the concat_unzip.sh script available in the repository.
info.txt contains the first four lines of the traj.tsv file, and last four lines of the traj.tsv file.
"

for i in "${part1[@]}"; do
    for j in "${part2[@]}"; do
        dir_name="$i-$j-$part3"
        mkdir "$dir_name"
        cat <<EOF >"$dir_name/$file_name"
$folder_init
EOF
    done
done

part1=("ATL" "GMU" "NOLA" "SFCO")
part2="1K"
part3=("121mo" "241mo")

for i in "${part1[@]}"; do
    for j in "${part3[@]}"; do
        dir_name="$i-$part2"-$j
        mkdir "$dir_name"
        cat <<EOF >"$dir_name/$file_name"
$folder_init 
EOF
    done
done
