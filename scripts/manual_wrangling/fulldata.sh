# it integrate all the tsv files into one file

# RENAME FILES TO MAKE THE RIGHT ORDER:
# use rename.sh 

# Usage: bash cut.sh
output_file=full.data.tsv
echo $output_file
> $output_file
rm *.tsv # remove the old files
ls
echo you should not see any tsv file 
for file in AgentStateTable-*.tsv.zip; do
  unzip "$file"

first_file=1
for file in *.tsv; do
if [ $file != $output_file ]; then
        echo integrating the $file ...
        if [ $first_file -eq 1 ]; then
            cat "$file" >> $output_file
            first_file=0
        else
            tail -n +2 "$file" >> $output_file
        fi
        rm $file
    fi
done

done

tail -n +2 ../AgentStateTable.tsv >> $output_file
