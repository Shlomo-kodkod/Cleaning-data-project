from manager import Manager


if __name__ == "__main__":
    manager = Manager(r"data\tweets_dataset.csv", 'Biased')
    manager.main()