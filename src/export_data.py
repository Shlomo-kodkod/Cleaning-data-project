import pandas as pd
import json

class ExportData:
    
    # Export the DataFrame to a CSV file.
    @staticmethod
    def export_to_csv(df, file_path: str):
        if df is not None:
            try:
                df.to_csv(file_path, index=False)
                print(f"Data exported successfully to {file_path}")
            except Exception as e:
                print(f"Failed to export data: {e}")
        else:
            print("DataFrame is empty. No data to export.")

    # Export the result to an json file.
    @staticmethod
    def export_to_json(res_dict, file_path: str):
        if res_dict is not None:
            try:
                with open(file_path, 'w') as json_file:
                    json.dump(res_dict, json_file, indent=4)
                print(f"Data exported successfully to {file_path}")
            except Exception as e:
                print(f"Failed to export data: {e}")
        else:
            print("Data is empty. No data to export.")

