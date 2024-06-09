# Description: Prepare data for the missed results

direct_script_path="/home/script/pol/scripts/data_wrangling"

#for 15months 5k all maps checkin and social link data
cd /home/datapaper/15months/5k/gmu/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 450 | tee -a script.log.txt

cd /home/datapaper/15months/5k/nola/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 450 | tee -a script.log.txt

cd /home/datapaper/15months/5k/atl/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 450 | tee -a script.log.txt

cd /home/datapaper/15months/5k/sfco/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 450 | tee -a script.log.txt
