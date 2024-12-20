import pandas as pd
import matplotlib.pyplot as plt

class CompareTwo:
    def __init__(self, coin_data_map):
        self.coin_data_map = coin_data_map

    def select_coins(self):
        coins_input = input("Enter the names of two coins ( btc, btcg, bnb, xrp), separated by a space: ").lower()
        coins = coins_input.split()

        if len(coins) != 2:
            print("Please enter the coins like this example: (xrp bnb).")
            return None, None

        coin1, coin2 = coins

        if coin1 not in self.coin_data_map or coin2 not in self.coin_data_map:
            print("Invalid coin names.")
            return None, None

        return self.coin_data_map[coin1], self.coin_data_map[coin2]

    def choose_graph_type(self):
        print("\nAvailable graph types:")
        print("1. Line graph")
        print("2. Bar chart")
        print("3. Scatter plot")
        print("4. Area chart")
        print("5. Histogram")
        graph_choice = input("Choose a graph type (1-5): ")

        graph_map = {
            "1": "line",
            "2": "bar",
            "3": "scatter",
            "4": "area",
            "5": "hist"
        }

        return graph_map.get(graph_choice, None)

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

        graph_type = self.choose_graph_type()
        if graph_type is None:
            print("Invalid graph type selection. Please try again.")
            return

        comparison = self.display_comparison(coin1_data, coin2_data)

        if graph_type == "scatter":
            plt.figure(figsize=(12, 6))
            plt.scatter(comparison.index, comparison["Coin 1"], label="Coin 1", alpha=0.6)
            plt.scatter(comparison.index, comparison["Coin 2"], label="Coin 2", alpha=0.6)
            plt.title("Comparison of Coin 1 and Coin 2")
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.legend(title="Cryptocurrencies")
            plt.grid(True)
            plt.show()
        else:
            comparison.plot(kind=graph_type, figsize=(12, 6))
            plt.title(f"Comparison of Coin 1 and Coin 2 ({graph_type.capitalize()})")
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.legend(title="Cryptocurrencies")
            plt.grid(True)
            plt.show()
