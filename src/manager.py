from data_loader import FileLoader
from data_investigation import DataInvestigation
from data_cleaner import DataCleaner
from export_data import ExportData
import pandas as pd

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
            print(f"Data loaded successfully from {self.__file_path}")
        else:
            print("Failed to load data.")
    
    # Investigate the data by calculating various statistics and exporting results to json file.
    def investigate_data(self):
        keys = ['antisemitic', 'non_antisemitic', 'total', 'unspecified']
        target_labels = (0, 1)
        investigation = DataInvestigation(self.__df, self.__target_column)
        result = {'total_tweets': dict(), "average_length": dict(), "common_words": dict(), "longest_3_tweets": dict(), "uppercase_words": dict()}
        result['total_tweets'][keys[0]] = investigation.tweet_sum_by_label(target_labels[1])
        result['total_tweets'][keys[1]] = investigation.tweet_sum_by_label(target_labels[0])
        result['total_tweets'][keys[2]] = investigation.total_tweet_sum()
        result['total_tweets'][keys[3]] = investigation.unspecified_tweet_sum_(target_labels)
        result['average_length'][keys[0]] = investigation.total_avg_text_length_by_label('Text', target_labels[1])
        result['average_length'][keys[1]] = investigation.total_avg_text_length_by_label('Text', target_labels[0])
        result['average_length'][keys[2]] = investigation.total_avg_text_length('Text')
        result['common_words'] = investigation.common_words('Text', 10)
        result['longest_3_tweets'][keys[0]] = investigation.longest_tweets_by_label('Text', target_labels[1], 3)
        result['longest_3_tweets'][keys[1]] = investigation.longest_tweets_by_label('Text', target_labels[0], 3)
        result['uppercase_words'][keys[0]] = investigation.sum_uppercase_words_by_label('Text', target_labels[1])
        result['uppercase_words'][keys[1]] = investigation.sum_uppercase_words_by_label('Text', target_labels[0])
        result['uppercase_words'][keys[2]] = investigation.total_uppercase_words('Text')
        return result
    
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
            print(cleaned_data.head())
            ExportData.export_to_csv(cleaned_data, 'results/cleaned_tweets.csv')
            ExportData.export_to_json(investigation_results, 'results/investigation_results.json')
        else:
            print("No data to process.")


