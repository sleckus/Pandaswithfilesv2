from compare_two import CompareTwo
from show_all import ShowAll  # Import ShowAll class from show_all.py

def ShowMenu():
    print(f'Choose what you want to do with the following data:')
    print('btc, btcg, bnb, xrp.')
    print(f'1. Show all of the data in a graph.')
    print('2. Compare 2 coins')
    print('3. exit')

def SelectMenu(btc_data, btcg_data, bnb_data, xrp_data):
    choice = input(f'Choose a number: ')
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            return ShowAll(btc_data, btcg_data, bnb_data, xrp_data).plot_prices('Bitcoin Gold', 'BNB', 'XRP')
        elif choice == 2:
            coin_data_map = {
                'btc': btc_data,
                'btcg': btcg_data,
                'bnb': bnb_data,
                'xrp': xrp_data
            }
            comparer = CompareTwo(coin_data_map)
            comparer.plot_comparison()


        elif choice == 3:
            return None
        else:
            print("Invalid choice.")
    else:
        print("Invalid input.")
    return None