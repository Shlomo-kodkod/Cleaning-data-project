# Preparatory project for analyzing anti-Semitism classification data on Twitter

# Data exploration:
- How many tweets are there from each category (by category, unspecified, and total)
- What is the average length (in words) of tweets (by category and total)
- What are the 3 tweets with the most text (by category)
- What are the 10 most common words in all tweets (from all categories)
- How many words are capitalized (by category and total) 


# Basic text cleaning
- Keeping the relevant columns from the data file 
- Removing punctuation marks
- Converting to lowercase
- Removing uncategorized tweets

# Exporting the results of the investigation and cleaning:
- Saved the cleaned dataset as a CSV file named csv.cleaned_dataset_tweets.
- Saved the results of the data exploration  to a JSON file named json.results.

# Project Structure
data/:
    tweets_dataset.csv - original data set
src/:
    data_loader.py - loading the data
    data_investigation.py - investigate the data
    data_cleaner.py - cleaning the data
    export_data.py - save the cleaned data to csv and save the results to json file
    manager.py - load, investigate, cleaning, and export the data
    main.py - program entry point
results/:
        The results of the clean information and the investigation of the information


# Technologies Used
Python 3
Standard Python libraries

