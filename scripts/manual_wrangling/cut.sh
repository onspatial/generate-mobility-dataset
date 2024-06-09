# It cuts the tsv file to "Tick, Time, Location, Agent ID." 
# It also removes the header line.

# RENAME FILES TO MAKE THE RIGHT ORDER:
mv AgentStateTable-1.tsv.zip AgentStateTable-01.tsv.zip
mv AgentStateTable-2.tsv.zip AgentStateTable-02.tsv.zip
mv AgentStateTable-3.tsv.zip AgentStateTable-03.tsv.zip
mv AgentStateTable-4.tsv.zip AgentStateTable-04.tsv.zip
mv AgentStateTable-5.tsv.zip AgentStateTable-05.tsv.zip
mv AgentStateTable-6.tsv.zip AgentStateTable-06.tsv.zip
mv AgentStateTable-7.tsv.zip AgentStateTable-07.tsv.zip
mv AgentStateTable-8.tsv.zip AgentStateTable-08.tsv.zip
mv AgentStateTable-9.tsv.zip AgentStateTable-09.tsv.zip

# Usage: bash cut.sh
output_file=data.tsv
echo $output_file
> $output_file
rm *.tsv # remove the old files
for file in *.tsv.zip; do
  unzip "$file"

first_file=1
for file in *.tsv; do
if [ $file != $output_file ]; then
  echo cuttting the $file ...
  if [ $first_file -eq 1 ]; then
    cut -f 1-4 "$file" >> $output_file
    first_file=0
  else
    tail -n +2 "$file" | cut -f 1-4 >> $output_file
  fi
  rm $file
  fi
done

done