from manager import Manager
import logging


base_config = logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()])


if __name__ == "__main__":
    manager = Manager(r"C:\Users\user\VsCodeProjects\Python\Cleaning data project\data\tweets_dataset.csv", 'Biased')
    manager.main()