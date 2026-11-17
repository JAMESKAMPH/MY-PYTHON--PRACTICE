import pandas as pd
import os
def run_merge_pipeline(salary_filename, details_filename, output_filename):
    """
    Robust, production-grade ETL pipeline with error handling.
    """
    try:
        script_dir=os.path.dirname(os.path.abspath(__file__)) 
        salary_path=os.path.join(script_dir,salary_filename)
        details_path=os.path.join(script_dir, details_filename)
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
    print("Transforming and merging data...")
    merged_df=pd.merge(salary_df, details_df,on="department", how="left",suffixes=('_salary_file','_details_file'))
    merged_df['region']= merged_df['region'].fillna("Unknown Region")
    print("\n✅ Pipeline execution complete successfully!")
    return merged_df
'if__name__'=="__main__" 
final_report=run_merge_pipeline(
        salary_filename="salary_report_pandas.csv",
        details_filename="department_details.csv",
        output_filename="final_merged_report.csv"
    )
if final_report is not None:
    print(final_report)