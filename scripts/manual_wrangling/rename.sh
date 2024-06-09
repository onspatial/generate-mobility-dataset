for oldname in AgentStateTable-*.tsv.zip
do
     num=$(echo $oldname | awk -F '[.-]' '{printf "%03d", $2}')
    newname="AgentStateTable-${num}.tsv.zip"

    if [ -e "$newname" ]; then
       echo "Error: $newname already exists."
    else
       mv -- "$oldname" "$newname"
    fi
done
