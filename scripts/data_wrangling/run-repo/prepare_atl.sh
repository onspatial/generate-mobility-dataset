# Description: Prepare data for ATL
# sh $direct_script_path/prepare_atl.sh
# for 15 months
direct_script_path="/home/script/pol/scripts/data_wrangling"
cd /home/datapaper/15months/10k/atl/pol/examples/logs/logs
sh $direct_script_path/prepare.sh 450 | tee -a script.log.txt

# for 121 months
cd /home/datapaper/121months/atl/pol/examples/logs/logs
sh $direct_script_path/prepare.sh 3630 | tee -a script.log.txt

# for 241 month
cd /home/datapaper/241months/atl/pol/examples/logs/logs
sh $direct_script_path/prepare.sh 7230 | tee -a script.log.txt
