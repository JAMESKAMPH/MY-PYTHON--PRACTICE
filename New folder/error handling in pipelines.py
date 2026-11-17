def process_data_safely(data_list):
    grouped={}
    for record in data_list:
        subj=record.get("subject")
        raw_score=record.get("score")
        #Try converting raw_score to a float safely
        try:
            clean_score=float(raw_score)
            if subj not in grouped:
                grouped[subj]=[]
            grouped[subj].append(clean_score)
        except (ValueError,TypeError):
        #Skip invalid values (None, "N/A","missing",etc.)
         continue
    #Compute averages for valid data
    return {subj: sum(scores)/len(scores)for subj, scores in grouped.items()}
# Dataset with messy types: None, strings, and valid numbers
messy_data=[
    {"name":"Alice","subject":"Math","score":"85"}, # String number
    {"name":"Bob","subject":"Physics","score":"90"}, # Int
    {"name":"Charlie","subject":"Math","score":"N/A"}, # Bad string
    {"name":"David","subject":"Physics","score":None}, # None type
    {"name":"Eva","subject":"Math","score":"95.5"} #Float
]
print("Clean Pipeline Output:", process_data_safely(messy_data))
