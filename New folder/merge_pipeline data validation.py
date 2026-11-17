import pandas as pd
import os
def run_merge_pipeline(salary_filename, details_filename, output_filename):
    """
    Robust, production-grade ETL pipeline with robust error handling and data validation.
    """
    try:
        script_dir=os.path.dirname(os.path.abspath(__file__)) 
        salary_path=os.path.join(script_dir,salary_filename)
        details_path=os.path.join(script_dir, details_filename)
        output_path=os.path.join(script_dir,output_filename)
        print("Extracting data...")
        salary_df=pd.read_csv(salary_path)
        details_df=pd.read_csv(details_path)
    except FileNotFoundError as e:
        print(f"\n ❌ ERROR: File not found. Please check your file names!")
        print(f"Technical details:{e}")
        return None
    except Exception as e:
        print(f"\n ❌ An unexpected error occured during extraction:{e}")
        return None
    print("Validating data structure and integrity...")
    required_salary_cols={"department","average_salary"}
    required_details_cols={"department","region"}
    if not required_salary_cols.issubset(salary_df.columns):
        print(f"\n❌ DATA ERROR: Missing required columns in details file.Expected:{required_salary_cols}")
        return None
    if  not required_details_cols.issubset(details_df.columns):
        print(f"\n❌ DATA ERROR:Missing required columns in details file. Expected :{required_details_cols}")
        return None
    if (salary_df["average_salary"]<0).any():
        print(f"\n❌ DATA ERROR:Negative salary values detected! Pipeline halted for safety.")
        return None
    print(f"Loading data to {output_filename}...")
    merged_df=pd.merge(salary_df,details_df,on="department",how="left")
    merged_df['region']=merged_df['region'].fillna("Unknown Region")
    print(f"Loading data to{output_filename}...")
    merged_df.to_csv(output_path, index=False)
    print("\n✅ Pipeline execution complete successfully!")
    return merged_df
if __name__ == "__main__" :
 final_report=run_merge_pipeline(
        salary_filename="salary_report_pandas.csv",
        details_filename="department_details.csv",
        output_filename="final_merged_report.csv"
    )
if final_report is not None:
    print(final_report)    