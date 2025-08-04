import pandas as pd

class DataInvestigation:

    def __init__(self, df: pd.DataFrame, target_column: str):
        self.__df = df
        self.__target_column = target_column
    
    #Get the total number of tweets in the DataFrame.
    def total_tweet_sum(self) -> int:
        if self.__df is None:
            return 0
        else:
            return self.__df[self.__target_column].count()
        
    # Get the total number of tweets for a specific label in the DataFrame.
    def tweet_sum_by_label(self, label: str | int) -> int:
        if self.__df is None:
            return 0
        else:
            return self.__df[self.__df[self.__target_column] == label][self.__target_column].count()
    
    # Get the total number of tweets that are not specified by the given labels.
    def unspecified_tweet_sum_(self, label: tuple[str | int]) -> int:
        if self.__df is None:
            print("DataFrame is empty.")
            return 0
        else:
            total_sum = self.total_tweet_sum()
            for i in label:
                total_sum -= self.tweet_sum_by_label(i)
            return total_sum
    
    # Get the average length of the text in the DataFrame.
    def total_avg_text_length(self, column: str) -> float:
        if self.__df is None:
            return 0.0
        else:
            return self.__df[column].str.len().mean()

    # Get the average length of the text for a specific label in the DataFrame.
    def total_avg_text_length_by_label(self, column: str, label: str | int) -> float:
        if self.__df is None:
            return 0.0
        else:
            return self.__df[self.__df[self.__target_column] == label][column].str.len().mean()
    
    # Get the longest tweets for a specific label in the DataFrame.
    def longest_tweets_by_label(self, column: str, label: str | int, n: int) -> list[str] | None:
        if self.__df is None:
            return None
        else:
            filtered_df = self.__df[self.__df[self.__target_column] == label].sort_values(by=column, key=lambda x: x.str.len(), ascending=False)
            if filtered_df.empty:
                return None
            longest_tweets = filtered_df[column].tolist()[:3]
            return longest_tweets
    
    # Get the most common words in the text for a specific label in the DataFrame.
    def common_words(self, column: str, n: int) -> list[str] | None:
        if self.__df is None:
            return None
        else:
            text_series = self.__df[column]
            all_words = ' '.join(text_series).split()
            word_counts = pd.Series(all_words).value_counts()
            common_words = word_counts.head(n).index.tolist()
            return common_words
    
    # Get the most common words in the text for a specific label in the DataFrame.
    def total_uppercase_words(self, column: str) -> int:
        if self.__df is None:
            return 0
        else:
            text_series = self.__df[column]
            all_words = ' '.join(text_series).split()
            total_uppercase = len([i for i in all_words if i.isupper()])
            return total_uppercase

    # Get the total number of uppercase words in the text for a specific label in the DataFrame.  
    def sum_uppercase_words_by_label(self, column: str, label: str | int) -> int:
        if self.__df is None:
            return 0
        else:
            filtered_df = self.__df[self.__df[self.__target_column] == label]
            text_series = filtered_df[column]
            all_words = ' '.join(text_series).split()
            total_uppercase = len([i for i in all_words if i.isupper()])
            return total_uppercase
    
df = pd.read_csv(r'C:\Users\user\VsCodeProjects\Python\Cleaning data project\data\tweets_dataset.csv')
investigation = DataInvestigation(df, 'Biased')
print(investigation.sum_uppercase_words_by_label('Text', 0))