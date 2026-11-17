import csv
import os
def process_and_export_pipeline(input_filename, output_filename):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    input_path=os.path.join(script_dir, input_filename)
    output_path=os.path.join(script_dir, output_filename)
    grouped={}
    try:
        with open(input_path, mode="r",encoding="utf-8") as file:
            reader=csv.DictReader(file)
            for record in reader:
                subj=record.get("subject")
                raw_score=record.get("score")
                if not subj:
                    continue
                try:
                    clean_score= float(raw_score)
                    if subj not in grouped:
                        grouped[subj]=[]
                    grouped[subj].append(clean_score)
                except (ValueError, TypeError):
                    continue
    except FileNotFoundError:
        print(f"Error:The file '{input_path}' could not be found.")
        return{}
    summary = {subj:sum(scores)/len(scores) for subj, scores in grouped.items()}
    try:
        with open(output_path, mode="w", newline="", encoding="utf-8") as outfile:
            fieldnames=["subject", "average_score"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for subj, avg in summary.items():
                writer.writerow({"subject":subj, "average_score": round(avg,2)})
        print(f"Success! Summary report exported to '{output_path}'.")
    except IOError:
        print(f"Error: Could not write to file'{output_path}'.")
    return summary
process_and_export_pipeline("scores.csv", "summary_report.csv")             