import pandas as pd
import os
script_dir= os.path. dirname(os.path.abspath(__file__))
salary_path=os.path.join(script_dir,"salary_report_pandas.csv")
details_path=os.path.join(script_dir,"department_details.csv")
output_path=os.path.join(script_dir,"final_merged_report.csv")
salary_df=pd.read_csv(salary_path)
details_df=pd.read_csv(details_path)
merged_df=pd.merge(salary_df, details_df, on="department", how="left")
merged_df['region']= merged_df['region'].fillna("Unknown Region")
merged_df.to_csv(output_path, index=False)
print("\n---Left Join Master Report---")
print(merged_df)