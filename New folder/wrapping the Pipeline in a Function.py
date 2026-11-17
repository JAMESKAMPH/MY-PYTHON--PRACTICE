def analyze_subjects(data_list):
    grouped={}
    for record in data_list:
        subj=record["subject"]
        score=record["score"]
        if score is not None:
            if subj not in grouped:
               grouped[subj]=[]
            grouped[subj].append(score)
    return{subj:sum(scores)/len(scores)for subj,scores in grouped.items()} 
term1 =[
    {"name":"Alice","subject":"Maths","score":85},
    {"name":"Bob","subject":"Physics","score":90},
    {"name":"Charlie","subject":"Maths","score":None},
    {"name":"David","subject":"Physics","score":70}
] 
term2 =[
    {"name":"Alice","subject":"Maths","score":92},
    {"name":"Bob","subject":"Physics","score":88},
    {"name":"Charlie","subject":"Physics","score":95}
]
print("Term1 Results:",analyze_subjects(term1))
print("Term2 Results:",analyze_subjects(term2))