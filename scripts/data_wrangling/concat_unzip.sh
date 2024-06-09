# run the script in the folder containis all traj.tsv.zip.part-*
# the script will concat all the files into one file, traj.tsv.zip.date
# and then unzip the file
file_name=traj.tsv.zip.$(date +%Y%m%d%H%M%S)
for i in $(ls *.part-*); do
    echo concating $i ... to $file_name
    cat $i >>$file_name
done

unzip $file_name
