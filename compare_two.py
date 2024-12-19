import pandas as pd
import matplotlib.pyplot as plt

class CompareTwo:
    def __init__(self, coin_data_map):
        self.coin_data_map = coin_data_map

    def select_coins(self):
        coins_input = input("Enter the names of two coins (e.g., btc, btcg, bnb, xrp), separated by a space: ").lower()
        coins = coins_input.split()

        if len(coins) != 2:
            print("Please enter exactly two coins.")
            return None, None

        coin1, coin2 = coins

        if coin1 not in self.coin_data_map or coin2 not in self.coin_data_map:
            print("Invalid coin name(s).")
            return None, None

        return self.coin_data_map[coin1], self.coin_data_map[coin2]

    def display_comparison(self, coin1_data, coin2_data):
        coin1_high = coin1_data['High']
        coin2_high = coin2_data['High']

        comparison = pd.DataFrame({
            "Coin 1": coin1_high,
            "Coin 2": coin2_high
        })

        return comparison

    def plot_comparison(self):
        coin1_data, coin2_data = self.select_coins()
        if coin1_data is None or coin2_data is None:
            return

        comparison = self.display_comparison(coin1_data, coin2_data)
        comparison.plot(figsize=(12, 6))
        plt.title("Comparison of Coin 1 and Coin 2")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend(title="Cryptocurrencies")
        plt.grid(True)
        plt.show()
