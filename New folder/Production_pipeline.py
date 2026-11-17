def process_pipeline(dataset):
    grouped={}
    for record in dataset:
        subj=record.get("subject")
        raw_score= record.get("score")
        if not subj:
            continue
        try:
            clean_score= float(raw_score)
            if subj not in grouped:
                grouped[subj]=[]
            grouped[subj].append(clean_score)
        except (ValueError,TypeError):
            continue
        return {subj: sum(scores)/len(scores)for subj, scores in grouped. items()}
raw_records = [
        {"name": "Alice", "subject": "Math", "score":"88"},
        {"name": "Bob","subject": "Physics", "score":"92.5"},
        {"name": "Charlie", "score":"88"},
        {"name": "David", "subject": "Math", "score":"corrupt"},
        {"name": "Eva", "subject": "Physics", "score":"None"},
        {"name": "Frank", "subject": "Math", "score":"94"},
        {"name": "Grace", "subject": "Chemistry", "score":"81"}
    ]
summary= process_pipeline(raw_records)
print("="*40)
print(f"{'SUBJECT':<15} | {'AVERAGE SCORE':<15}")
print("="*40)
for subject, avg in summary. items():
        print(f"{subject:<15} | {avg:<15.2f}")
print("="*40)
    