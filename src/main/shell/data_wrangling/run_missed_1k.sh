# Description: Prepare data for the missed results

direct_script_path="/home/script/pol/scripts/data_wrangling"

# for 15month 1k all maps all data
cd /home/datapaper/15months/1k/gmu/pol/examples/logs/logs
sh $direct_script_path/prepare.sh 450 | tee -a script.log.txt

cd /home/datapaper/15months/1k/nola/pol/examples/logs/logs
sh $direct_script_path/prepare.sh 450 | tee -a script.log.txt

cd /home/datapaper/15months/1k/atl/pol/examples/logs/logs
sh $direct_script_path/prepare.sh 450 | tee -a script.log.txt

cd /home/datapaper/15months/1k/sfco/pol/examples/logs/logs
sh $direct_script_path/prepare.sh 450 | tee -a script.log.txt
