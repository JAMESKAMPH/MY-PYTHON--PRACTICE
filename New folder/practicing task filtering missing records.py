students=[
    {"name": "Alice","score":45},
    {"name": "Bob","score":None},
    {"name": "Charlie","score":91},
    {"name": "David","score":None},
    {"name": "Eva","score":67}
]
for student in students:
    score=student["score"]
    if score is None:
        status="Missing Record"
    elif score  >= 50:
        status="Pass"
    else:
        status="Fail"
    print(student["name"],"->",status)