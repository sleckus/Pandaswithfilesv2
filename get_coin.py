import pandas as pd

class GetCoin:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

        if 'Date' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')
            self.data = self.data.dropna(subset=['Date'])  # Drop rows with invalid dates
            self.data = self.data.set_index('Date')

    def get_data(self):
        return self.data
