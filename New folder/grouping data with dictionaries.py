dataset = [
    {"name": "Alice","subject":"Math","score":85},
    {"name": "Bob","subject":"Physics","score":90},
    {"name": "Charlie","subject":"Math","score":None},
    {"name": "David","subject":"Physics","score":70},
    {"name": "Eva","subject":"Math","score":95}
]
grouped={}
for record in dataset:
    subj=record["subject"]
    score=record["score"]
    if score is not None:
        if subj not in grouped:
            grouped[subj]=[]
        grouped[subj]. append(score)
subject_averages={}
for subj, scores in grouped.items():
    subject_averages[subj]= sum(scores)/len(scores)
print("Grouped Scores:", grouped)
print("Subject Avarages:",subject_averages)
