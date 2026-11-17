students=[
    {"name": "Alice","score":45},
    {"name":"Bob","score":None},
    {"name":"Charlie","score":91},
    {"name":"David","score":None},
    {"name":"Eva","score":67}
]
results ={
    s["name"]:("Pass" if s["score"]>= 50 else "Fail")
    for s in students
    if s["score"] is  not None
}
print("Processed Results:", results)
print("Charlie's Result:",results["Charlie"])
print("Alice's Result:",results["Alice"])
print("Eva's Result:",results["Eva"])