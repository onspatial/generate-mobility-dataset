build=$1
agents=1000
while true; do
    if [ "$build" == "build" ]; then
        bash sh.mvn.sh
    fi
    rm -rf life/logs

    cd life
    echo $(date)

    echo "numOfAgents = $agents
seed = 1
maps = maps/atl/map" >modified.properties
    bash sh.live.sh | tee emory_exit_off_$agents.log 2>&1
    echo $(date)
    cd ..
    echo "sleeping 10 seconds"
    agents=$((agents + 5000))
    sleep 10
    if [ $? -eq 130 ]; then
        continue
    fi

done
