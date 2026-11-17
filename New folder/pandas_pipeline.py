import pandas as pd
import os
script_dir=os.path.dirname(os.path.abspath(__file__))
input_path=os.path.join(script_dir,"sales_data.csv")
output_path=os.path.join(script_dir,"salary_report_pandas.csv")
df = pd.read_csv(input_path)
df['salary']=pd.to_numeric(df['salary'],errors='coerce')
clean_df=df.dropna(subset=['department', 'salary'])
summary= clean_df.groupby('department')['salary'].mean().reset_index()
summary.rename(columns={'salary': 'average_salary'}, inplace=True)
summary['average_salary']=summary['average_salary'].round(2)
summary.to_csv(output_path, index=False)
print("Success! Pandas pipeline ran perfectly.")
print(summary)