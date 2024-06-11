# Description: Prepare data for GMU not traj and test but the rest
# sh $direct_script_path/prepare_gmu_rest.sh
# for 15 months
direct_script_path="/home/script/pol/scripts/data_wrangling"
cd /home/datapaper/15months/10k/gmu/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 450 | tee -a script.log.txt

# for 121 months
cd /home/datapaper/121months/gmu/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 3630 | tee -a script.log.txt

# for 241 month
cd /home/datapaper/241months/gmu/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 7230 | tee -a script.log.txt
