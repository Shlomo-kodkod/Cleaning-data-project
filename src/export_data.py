import pandas as pd
import json
import logging


logger = logging.getLogger(__name__)

class ExportData:
    
    # Export the DataFrame to a CSV file.
    @staticmethod
    def export_to_csv(df, file_path: str):
        try:
            df.to_csv(file_path, index=False)
            logger.info(f"Data exported successfully to {file_path}")
        except Exception as e:
            logger.error(f"Failed to export data: {e}")
       

    # Export the result to an json file.
    @staticmethod
    def export_to_json(res_dict, file_path: str):
        try:
            with open(file_path, 'w') as json_file:
                json.dump(res_dict, json_file, indent=4)
            logger.info(f"Data exported successfully to {file_path}")
        except Exception as e:
            logger.error(f"Failed to export data: {e}")
       
