import pandas as pd

class GetCoin:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path, parse_dates=['Date'], index_col='Date')
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at {self.file_path} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")

    def get_data(self):
        if self.data is None:
            raise ValueError("Data has not been loaded. Call 'load_data' first.")
        return self.data