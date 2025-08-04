import pandas as pd


class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.__df = df

    # Remove unrelevant columns from the DataFrame.
    def keep_relevant_columns(self, columns: list[str]) -> pd.DataFrame:
        if self.__df is not None:
            self.__df = self.__df[columns]

    # Remove punctuation values in the specified column
    def remove_punctuation_marks(self, column: str):
        if self.__df is not None:
            self.__df.loc[:, column] = self.__df[column].str.replace(r'[^\w\s]', ' ', regex=True)
            
    
    # Replace all uppercase values in the DataFrame with a lowercase values.
    def to_lowercase(self, column: str):
        if self.__df is not None:
            self.__df.loc[:, column] = self.__df[column].str.lower()

    # Remove rows that contain unspecified values in the target column.
    def remove_unspecified(self, column: str, labels: list[str | int]):
        self.__df = self.__df[self.__df[column].isin(labels)]

    #Return the cleaned DataFrame.
    def get_cleaned_data(self) -> pd.DataFrame:
        return self.__df

    