import pandas as pd
import logging



logger = logging.getLogger(__name__)


class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.__df = df

    # Remove non relevant columns from the DataFrame.
    def keep_relevant_columns(self, columns: list[str]):
        logger.info(f"Keeping relevant columns: {columns}")
        try:
            self.__df = self.__df[columns]
            logger.info("Relevant columns kept successfully.")
        except Exception as e:
            logger.error(f"Failed to keep relevant columns: {e}")
        
    # Remove punctuation values in the specified column
    def remove_punctuation_marks(self, column: str):
        logger.info(f"Removing punctuation marks from column: {column}")
        try:
            self.__df.loc[:, column] = self.__df[column].str.replace(r'[^\w\s]', ' ', regex=True)
            logger.info("Punctuation marks removed successfully.")
        except Exception as e:
            logger.error(f"Failed to remove punctuation marks from column {column}: {e}")
    
    # Replace all uppercase values in the DataFrame with a lowercase values.
    def to_lowercase(self, column: str):
        logger.info(f"Converting column {column} to lowercase.")
        try:
            self.__df.loc[:, column] = self.__df[column].str.lower()
            logger.info("Column converted to lowercase successfully.")
        except Exception as e:
            logger.error(f"Failed to convert column {column} to lowercase: {e}")

    # Remove rows that contain unspecified values in the target column.
    def remove_unspecified(self, column: str, labels: list[str | int]):
        logger.info(f"Removing rows with unspecified values in column {column}.")
        try:
            self.__df = self.__df[self.__df[column].isin(labels)]
            logger.info("Unspecified values removed successfully.")
        except Exception as e:
            logger.error(f"Failed to remove unspecified values in column {column}: {e}")

    #Return the cleaned DataFrame.
    def get_cleaned_data(self) -> pd.DataFrame:
        return self.__df

    