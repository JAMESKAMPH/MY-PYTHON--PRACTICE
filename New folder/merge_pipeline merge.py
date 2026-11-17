import pandas as pd
import os
def run__pipeline(salary_filename, details_filename, output_filename):
    """
    Reusable ETL pipeline to  salary summarises with department details.
    """
    script_dir=os.path.dirname(os.path.abspath(__file__))
    salary_path=os.path.join(script_dir,salary_filename)
    details_path=os.path.join(script_dir,details_filename)
    output_path=os.path.join(script_dir, output_filename)
    print("Extracting data...")
    salary_df=pd.read_csv(salary_path)
    details_df=pd.read_csv(details_path)
    print("Transforming and merging data...")
    d_df=pd.(salary_df,details_df, on="department", how="left")
    d_df['region']=d_df["region"].fillna("Unknown Region")
    print(f"Loading data to {output_filename}...")
    d_df.to_csv(output_path, index=False)
    print("\nPipeline execution complete!")
    return d_df
if __name__=="__main__":
    final_report= run__pipeline(
        salary_filename= "salary_report_pandas.csv",
        details_filename= "department_details.csv",
        output_filename="final_d_report.csv" 
    )
    print(final_report)