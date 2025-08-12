import pandas as pd
import logging
from data_loader import FileLoader
from data_investigation import DataInvestigation
from data_cleaner import DataCleaner
from export_data import ExportData
from data_builder import DataBuilder


logger = logging.getLogger(__name__)

class Manager:
    def __init__(self, file_path: str, target_column: str):
        self.__file_path = file_path
        self.__target_column = target_column
        self.__df = None

    # Load data from the specified file path
    # and store it in a DataFrame.
    def load_data(self):
        self.__df = FileLoader.load_data(self.__file_path)
        if self.__df is not None:
            logger.info(f"Data loaded successfully from {self.__file_path}")
        else:
            logger.error("Failed to load data.")
    
    # Investigate the data by calculating various statistics and exporting results to json file.
    def investigate_data(self):
        data_builder = DataBuilder(self.__target_column, self.__df)
        data_builder.total_tweets()
        data_builder.average_length()
        data_builder.common_words()
        data_builder.longest_tweets()
        data_builder.uppercase_words()
        return data_builder.result
    
    # Cleaning the data and exporting the cleaned data to csv file.
    def clean_data(self, columns: list[str]):
        cleaner = DataCleaner(self.__df)
        cleaner.keep_relevant_columns(columns)
        cleaner.remove_punctuation_marks('Text')
        cleaner.to_lowercase('Text')
        cleaner.remove_unspecified('Biased', [0, 1])
        return cleaner.get_cleaned_data()
    
    # Main function to loading, investigating, cleaning, and exporting the data.
    def main(self):
        self.load_data()
        if self.__df is not None:
            investigation_results = self.investigate_data()
            cleaned_data = self.clean_data(['Text', 'Biased'])
            ExportData.export_to_csv(cleaned_data, 'results/cleaned_tweets.csv')
            ExportData.export_to_json(investigation_results, 'results/investigation_results.json')
            logger.info("Data processing completed successfully.")
        else:
            logger.error("Data processing failed due to loading error.")


