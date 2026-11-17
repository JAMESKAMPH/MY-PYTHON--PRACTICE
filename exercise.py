raw_data=[
    {"id":101,"val":45.2,"status":"valid"},
    {"id":102,"val":None,"status":"error"},
    {"id":103,"val":88.0,"status":"valid"},{"id":104,"val":12.5,"status":"valid"}],
(function)  def_clean_dataset: (records):
valid_vals=[r["val"]for r in records if r["status"]=="valid"and r["val"]is not None],
return sum(valid_vals)/len(valid_vals) if valid_vals else 0, 
print("Avarage of valid values:",clean_dataset(raw_data))