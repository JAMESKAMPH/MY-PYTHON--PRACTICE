students=[
    {"name": "Alice","score":45},
    {"name":"Bob","score":None},
    {"name":"Charlie","score":91},
    {"name":"David","score":None},
    {"name":"Eva","score":67}
]
valid_scores=[]
for student in students:
    if student["score"] is not None:
        valid_scores.append(student["score"])
total=sum(valid_scores)
count=len(valid_scores)
avarage= total/count
print("Valid scores extracted:",valid_scores)
print("Clean avarage score:",avarage)