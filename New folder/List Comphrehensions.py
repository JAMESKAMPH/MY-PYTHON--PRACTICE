students=[
    {"name": "Alice","score":45},
    {"name":"Bob","score":None},
    {"name":"Charlie","score":91},
    {"name":"David","score":None},
    {"name":"Eva","score":67}
]
valid_scores=[s["score"] for s in students  if s["score"] is not None]
clean_avg=sum(valid_scores)/ len(valid_scores)
print("Valid scores:", valid_scores)
print("Avarage:",clean_avg)