from manager import Manager


if __name__ == "__main__":
    manager = Manager(r"C:\Users\user\VsCodeProjects\Python\Cleaning data project\data\tweets_dataset.csv", 'Biased')
    manager.main()