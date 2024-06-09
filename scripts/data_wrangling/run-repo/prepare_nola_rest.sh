# Description: Prepare data for NOLA
# sh $direct_script_path/prepare_nola.sh
# for 15 months
direct_script_path="/home/script/pol/scripts/data_wrangling"
cd /home/datapaper/15months/10k/nola/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 450 | tee -a script.log.txt

# for 121 months
cd /home/datapaper/121months/nola/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 3630 | tee -a script.log.txt

# for 241 month
cd /home/datapaper/241months/nola/pol/examples/logs/logs
sh $direct_script_path/prepare_rest.sh 7230 | tee -a script.log.txt
