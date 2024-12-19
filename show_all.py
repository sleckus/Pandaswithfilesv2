import pandas as pd
from matplotlib import pyplot as plt


class ShowAll:
    def __init__(self, main_coin_data, second_coin_data, third_coin_data, fourth_coin_data):
        self.main_coin_data = main_coin_data
        self.second_coin_data = second_coin_data
        self.third_coin_data = third_coin_data
        self.fourth_coin_data = fourth_coin_data

    def display_prices(self, second_name, third_name, fourth_name):
        main_high = self.main_coin_data['High']
        second_high = self.second_coin_data['High']
        third_high = self.third_coin_data['High']
        fourth_high = self.fourth_coin_data['High']

        prices = pd.DataFrame({
            "Bitcoin": main_high,
            second_name: second_high,
            third_name: third_high,
            fourth_name: fourth_high
        })

        return prices

    def plot_prices(self, second_name, third_name, fourth_name):
        prices = self.display_prices(second_name, third_name, fourth_name)
        prices.plot(figsize=(12, 6))
        plt.title("Crypto Prices")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend(title="Cryptocurrencies")
        plt.grid(True)
        plt.show()
