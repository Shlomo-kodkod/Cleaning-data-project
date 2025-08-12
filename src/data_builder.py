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

    # Calculates how many tweets there are from each category (by category, undefined, and total).
    def tweets_sum(self) -> None:
        for key, label in self.__target_labels.items():
            self.__result['total_tweets'][key] = self.__investigation.tweet_sum(label)
        self.__result['total_tweets']['total'] = self.__investigation.tweet_sum()
        self.__result['total_tweets']['unspecified'] = self.__investigation.unspecified_tweet_sum_(tuple(self.__target_labels.values()))

    # Calculate the average length (in words) of tweets (by category and total).
    def average_length(self) -> None:
        for key, label in self.__target_labels.items():
            self.__result['average_length'][key] = self.__investigation.avg_text_length('Text', label)
        self.__result['average_length']['total'] = self.__investigation.avg_text_length('Text')

    # Find the 3 tweets with the largest amount of text (by category).
    def common_words(self) -> None:
        self.__result['common_words'] = self.__investigation.common_words('Text', 10)

    # Find the 10 most common words in all tweets (from all categories).
    def longest_tweets(self) -> None:
        for key, label in self.__target_labels.items():
            self.__result['longest_3_tweets'][key] = self.__investigation.longest_tweets('Text', label, 3)

    # Calculate a few words in large letters (by category and total).
    def uppercase_words(self) -> None:
        for key, label in self.__target_labels.items():
            self.__result['uppercase_words'][key] = self.__investigation.sum_uppercase_words('Text', label)
        self.__result['uppercase_words']['total'] = self.__investigation.sum_uppercase_words('Text')
        return self.__result
    
    # return the result in dictenary.
    @property
    def result(self) -> dict:
        return self.__result
