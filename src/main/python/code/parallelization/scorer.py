
import utils.geolife as geolife
import utils.pol as pol
import utils.stat as stat
import utils.file as file
from utils.stat import save_stat_to_file, get_stat_from_file
from utils.score import get_score_from_stat


import sys
import os

def run(checkin_path, dataset_type):
    data = None
    stat_path = file.get_stat_path(checkin_path)
    statistics = get_stat_from_file(stat_path)
    if statistics:
        return statistics
    
    if dataset_type == "geolife":
        data = geolife.read(checkin_path)
    elif dataset_type == "pol":
        data = pol.read(checkin_path)
    else:
        print("Dataset type not supported")
        return
    
    statistics = stat.get_stat(data)
    print(statistics)
    if not file.exists(stat_path):
        save_stat_to_file(statistics, stat_path)

    return statistics


def get_score(pol_path):
    log_file = "results_score.log.txt"
    try:
        geolife_stat = run(file.get_geolife_path(), "geolife")
        pol_stat = run(pol_path, "pol")
        score, scaled_score = get_score_from_stat(geolife_stat, pol_stat, normalize=geolife_stat)
        file.log_print(f"{pol_path} : {(score, scaled_score)}", log_file)
        
        if scaled_score > 0 and scaled_score <= 1:
            return scaled_score
        else:
            return -1
        
    except Exception as e:
        print(f"Error getting score: {e}")
        file.log_print(f"{pol_path} : 0", log_file)
        return 0
    

if __name__ == "__main__":
    pol_path = sys.argv[1]
    get_score(pol_path)
    