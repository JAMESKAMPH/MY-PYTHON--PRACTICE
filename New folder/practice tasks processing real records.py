students=[
       {"name": "Alice", "score":45},
       {"name": "Bob", "score":82},
       {"name": "Charlie", "score":91},
       {"name": "David", "score":38}  
]
for student in students:
    if student ["score"] >=50:
        status= "Pass"
    else:
        status="Fail"
    print(student["name"],"scored", student["score"],"->",status)