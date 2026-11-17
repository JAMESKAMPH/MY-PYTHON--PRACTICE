def process_data_safely(data_list):
    grouped={}
    for record in data_list:
        subj=record.get("subject")
        raw_score=record.get("score")
        try:
            clean_score=float(raw_score)
            if subj not in grouped:
                grouped[subj]=[]
            grouped[subj].append(clean_score)
        except (ValueError,TypeError):
          continue
    return {subj: sum(scores)/len(scores)for subj, scores in grouped.items()}
messy_data=[
    {"name":"Alice","subject":"Math","score":"85"}, 
    {"name":"Bob","subject":"Physics","score":"90"}, 
    {"name":"Charlie","subject":"Math","score":"N/A"}, 
    {"name":"David","subject":"Physics","score":None}, 
    {"name":"Eva","subject":"Math","score":"95.5"}
]
results = process_data_safely(messy_data)
print("="*35)
print("      SUMMARY REPORT")
print("=*35")
for subject, avg in results.items():
    print(f"Subject:{subject:<10}|Average:{avg:.2f}")
print("="*35)

