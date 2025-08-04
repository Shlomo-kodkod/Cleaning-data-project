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
    def total_avg_text_length(self) -> float:
        if self.__df is None:
            return 0.0
        else:
            return self.__df['Text'].str.len().mean()

    # Get the average length of the text for a specific label in the DataFrame.
    def total_avg_text_length_by_label(self, label: str | int) -> float:
        if self.__df is None:
            return 0.0
        else:
            return self.__df[self.__df[self.__target_column] == label]['Text'].str.len().mean()
        
df = pd.read_csv(r'C:\Users\user\VsCodeProjects\Python\Cleaning data project\data\tweets_dataset.csv')
investigation = DataInvestigation(df, 'Biased')
print(investigation.total_avg_text_length())