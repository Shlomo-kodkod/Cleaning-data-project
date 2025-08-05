import pandas as pd
import logging


logger = logging.getLogger(__name__)

class DataInvestigation:

    def __init__(self, df: pd.DataFrame, target_column: str):
        self.__df = df
        self.__target_column = target_column
    
    #Get the total number of tweets in the DataFrame.
    def total_tweet_sum(self) -> int:
        logger.info("Calculating total tweet sum.")
        if self.__df is None:
            logger.error("DataFrame is empty.")
            return 0
        else:
            res = int(self.__df[self.__target_column].count())
            logger.info("Successfully calculated total tweet sum.")
            return res
        
    # Get the total number of tweets for a specific label in the DataFrame.
    def tweet_sum_by_label(self, label: str | int) -> int:
        logger.info(f"Calculating tweet sum for label: {label}")
        if self.__df is None:
            logger.error("DataFrame is empty.")
            return 0
        else:
            res = int(self.__df[self.__df[self.__target_column] == label][self.__target_column].count())
            logger.info(f"Successfully calculated tweet sum for label: {label}")
            return res
    
    # Get the total number of tweets that are not specified by the given labels.
    def unspecified_tweet_sum_(self, label: tuple[str | int]) -> int:
        logger.info(f"Calculating unspecified tweet sum for labels: {label}")
        if self.__df is None:
            logger.error
            return 0
        else:
            total_sum = self.total_tweet_sum()
            for i in label:
                total_sum -= self.tweet_sum_by_label(i)
            res =  int(total_sum)
            logger.info(f"Successfully calculated unspecified tweet sum for labels: {label}")
            return res
    
    # Get the average length of the text in the DataFrame.
    def total_avg_text_length(self, column: str) -> float:
        logger.info(f"Calculating average text length for column: {column}")
        try:
            res = float(self.__df[column].str.split().str.len().mean())
            logger.info("Successfully calculated average text length.")
            return res
        except Exception as e:
            logger.error(f"Error calculating average text length: {e}")
            return 0.0
            
    # Get the average length of the text for a specific label in the DataFrame.
    def total_avg_text_length_by_label(self, column: str, label: str | int) -> float:
        logger.info(f"Calculating average text length for label: {label} in column: {column}")
        try:
            res = float(self.__df[self.__df[self.__target_column] == label][column].str.split().str.len().mean())
            logger.info(f"Successfully calculated average text length for label: {label}")
            return res
        except Exception as e:
            logger.error(f"Error calculating average text length for label {label}: {e}")
            return 0.0
    
    # Get the longest tweets for a specific label in the DataFrame.
    def longest_tweets_by_label(self, column: str, label: str | int, n: int) -> list[str] | None:
        logger.info(f"Retrieving longest tweets for label: {label} in column: {column}")
        try:
            filtered_df = self.__df[self.__df[self.__target_column] == label].sort_values(by=column, key=lambda x: x.str.len(), ascending=False)
            if filtered_df.empty:
                logger.warning(f"No tweets found for label: {label}")
                return None
            longest_tweets = filtered_df[column].tolist()[:3]
            logger.info(f"Successfully retrieved longest tweets for label: {label}")
            return longest_tweets
        except Exception as e:
            logger.error(f"Error retrieving longest tweets for label {label}: {e}")
            return None
    
    # Get the most common words in the text for a specific label in the DataFrame.
    def common_words(self, column: str, n: int) -> list[str] | None:
        logger.info(f"Retrieving {n} most common words from column: {column}")
        try:
            text_series = self.__df[column]
            all_words = ' '.join(text_series).split()
            word_counts = pd.Series(all_words).value_counts()
            common_words = word_counts.head(n).index.tolist()
            logger.info(f"Successfully retrieved {n} most common words.")
            return common_words
        except Exception as e:
            logger.error(f"Error retrieving common words: {e}")
            return None
    
    # Get the most common words in the text for a specific label in the DataFrame.
    def total_uppercase_words(self, column: str) -> int:
        logger.info(f"Calculating total uppercase words in column: {column}")
        try:
            text_series = self.__df[column]
            all_words = ' '.join(text_series).split()
            total_uppercase = len([i for i in all_words if i.isupper()])
            logger.info("Successfully calculated total uppercase words.")
            return int(total_uppercase)
        except Exception as e:
            logger.error(f"Error calculating total uppercase words: {e}")
            return 0

    # Get the total number of uppercase words in the text for a specific label in the DataFrame.  
    def sum_uppercase_words_by_label(self, column: str, label: str | int) -> int:
        logger.info(f"Calculating uppercase words for label: {label} in column: {column}")
        try:
            filtered_df = self.__df[self.__df[self.__target_column] == label]
            text_series = filtered_df[column]
            all_words = ' '.join(text_series).split()
            total_uppercase = len([i for i in all_words if i.isupper()])
            logger.info(f"Successfully calculated uppercase words for label: {label}")
            return int(total_uppercase)
        except Exception as e:
            logger.error(f"Error calculating uppercase words for label {label}: {e}")
            return 0
