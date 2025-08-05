import pandas as pd
import logging

logger = logging.getLogger(__name__)

# FileLoader load CSV files from disk
class FileLoader():

    # Load a CSV file into a DataFrame
    @staticmethod
    def load_data(file_path: str) -> pd.DataFrame | None:
        try:
            file_path = file_path
            logger.info(f"Loading data from {file_path}")
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            logger.error(f"Failed to load data from {file_path}: {e}")
            return None
