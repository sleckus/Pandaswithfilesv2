import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from get_coin import GetCoin
from show_all import ShowAll
from cmenu import ShowMenu, SelectMenu


btc = GetCoin('files/bitcoin.csv')
btc.load_data()
btc_data = btc.get_data()

btcg = GetCoin('files/Bitcoin Gold.csv')
btcg.load_data()
btcg_data = btcg.get_data()

bnb = GetCoin('files/BNB.csv')
bnb.load_data()
bnb_data = bnb.get_data()

xrp = GetCoin('files/xrp.csv')
xrp.load_data()
xrp_data = xrp.get_data()

ShowMenu()  # Show the menu
SelectMenu(btc_data, btcg_data, bnb_data, xrp_data)
