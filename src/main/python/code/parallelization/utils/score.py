def get_score_from_stat (stat1, stat2, normalize=None):

    print("Calculating score...")
    score = 0.0
    diff = {}
    for key in stat1:
        if key in stat2:
            
            try:
                
                if type(stat1[key]) in [int, float]:
                    diff[key] = (abs(stat1[key] - stat2[key]))
               
            except:
                print("Error: ", key, stat1[key], stat2[key])
                diff[key] = 0
           
    if normalize:
        for key in diff:
            diff[key] = diff[key] / normalize[key]
        normalization = 1
            
    else:
        normalization = 100
    # print("Diff: ", diff)
    score = float(sum(diff.values()) / len(diff))
    scaled_score =  normalization - score/normalization
    return score, scaled_score
    