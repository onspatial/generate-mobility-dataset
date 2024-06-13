from utils.score import get_score_from_stat
from utils.stat import  get_stat_from_file
import os
geo_stat= {"distance_per_trip": 3692.136322125363, "average_distance": 4474.59242875467, "max_distance": 30262.0, "median_distance": 3349.75}

# city/results.old/id_results_6/calculation.log.txt
pl_stat_200 ={'distance_per_trip': 4271.24709118128, 'average_distance': 4237.819534070307, 'max_distance': 32808.0, 'median_distance': 3689.0}

# city/results.old/id_results_8/calculation.log.txt
pl_stat_1k = {'distance_per_trip': 3002.256256942419, 'average_distance': 2998.3476042247935, 'max_distance': 31907.0, 'median_distance': 2650.0}

print(f'pol_200: {get_score_from_stat(geo_stat, pl_stat_200, normalize=geo_stat)}')
print(f'pol_1k: {get_score_from_stat(geo_stat, pl_stat_1k, normalize=geo_stat)}')

city_dir= '/home/hosseinamiri/Research/geopol-dev/city'
results=''
for root, dirs, files in os.walk(city_dir):
    for file in files:
        if file == 'stat.json':
            stat_file= os.path.join(root, file)
            pol_stat= get_stat_from_file(stat_file)
            results+= f'file:{stat_file}, score: {get_score_from_stat(geo_stat, pol_stat, normalize=geo_stat)}\n'

with open('results_all.txt', 'w') as f:
    f.write(results)
            