import pandas as pd
from data_investigation import DataInvestigation

class DataBuilder:
    def __init__(self, target_column: str, df: pd.DataFrame):
        self.__target_column = target_column
        self.__df = df
        self.__investigation = DataInvestigation(self.__df, self.__target_column)
        self.__target_labels = { 'antisemitic': 1, 'non_antisemitic': 0 }
        self.__result = {
            'total_tweets': {},
            'average_length': {},
            'common_words': {},
            'longest_3_tweets': {},
            'uppercase_words': {}
        }


    def total_tweets(self) -> None:
        for key, label in self.__target_labels.items():
            self.__result['total_tweets'][key] = self.__investigation.tweet_sum_by_label(label)
        self.__result['total_tweets']['total'] = self.__investigation.total_tweet_sum()
        self.__result['total_tweets']['unspecified'] = self.__investigation.unspecified_tweet_sum_(tuple(self.__target_labels.values()))

    def average_length(self) -> None:
        for key, label in self.__target_labels.items():
            self.__result['average_length'][key] = self.__investigation.total_avg_text_length_by_label('Text', label)
        self.__result['average_length']['total'] = self.__investigation.total_avg_text_length('Text')

    def common_words(self) -> None:
        self.__result['common_words'] = self.__investigation.common_words('Text', 10)

    def longest_tweets(self) -> None:
        for key, label in self.__target_labels.items():
            self.__result['longest_3_tweets'][key] = self.__investigation.longest_tweets_by_label('Text', label, 3)

    def uppercase_words(self) -> None:
        for key, label in self.__target_labels.items():
            self.__result['uppercase_words'][key] = self.__investigation.sum_uppercase_words_by_label('Text', label)
        self.__result['uppercase_words']['total'] = self.__investigation.total_uppercase_words('Text')
        return self.__result
    
    @property
    def result(self) -> dict:
        return self.__result
