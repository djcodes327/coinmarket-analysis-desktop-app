# COIN_MARKET_API Project
from tkinter import *
import requests
import json
import sqlite3

conn = sqlite3.connect('coin.db')
cObj = conn.cursor()

cObj.execute("CREATE TABLE IF NOT EXISTS coins (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, symbol TEXT, amount INTEGER, Price REAL )")
conn.commit()


'''

# GUI
crypto = Tk()
crypto.title("Crypto-Currency Portfolio")
crypto.iconbitmap('Favicon.ico')

def coin_status(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


def my_portfolio():
    # Calling API
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD""&CMC_PRO_API_KEY=")

    # Loading Stored Data
    api = json.loads(api_request.content)

    # "Bitcoin","Ethereum","Bitcoin Cash","Binance Coin","Bitcoin SV"
    coins = [
        {
            "name": "Bitcoin",
            "symbol": "BTC",
            "amount_owned": 2,
            "price_per_coin": 3200
        },

        {
            "name": "Ethereum",
            "symbol": "ETH",
            "amount_owned": 5,
            "price_per_coin": 3.700
        },

        {
            "name": "Bitcoin Cash",
            "symbol": "BCH",
            "amount_owned": 10,
            "price_per_coin": 300
        },

        {
            "name": "Binance Coin",
            "symbol": "BNB",
            "amount_owned": 6,
            "price_per_coin": 200
        },

    ]

    total_pl = 0
    coin_rows = 1
    total_cv = 0

    for i in range(10):
        for coin in coins:
            if coin["name"] == api["data"][i]["name"]:
                # Total Amount Paid
                total_paid = coin["amount_owned"] * coin["price_per_coin"]

                # Current Value of Coin
                current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]

                # Profit/Loss for Coin
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]

                # Total Profit/Loss Per-coin
                total_pl_percoin = pl_percoin * coin["amount_owned"]

                # Total P/L
                total_pl = total_pl + total_pl_percoin

                # Total Current Value
                total_cv += current_value

                name = Label(crypto, text=api["data"][i]["name"], bg="white", fg="black", font="Roboto 12", padx="7",
                             pady="7", borderwidth=2, relief="groove")
                name.grid(row=coin_rows, column=0, sticky=N + S + E + W)

                price = Label(crypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white",
                              fg="black", font="Roboto 12", padx="7", pady="7", borderwidth=2, relief="groove")
                price.grid(row=coin_rows, column=1, sticky=N + S + E + W)

                no_of_coins = Label(crypto, text="${0:.2f}".format(coin["amount_owned"]), bg="white", fg="black",
                                    font="Roboto 12", padx="7", pady="7", borderwidth=2, relief="groove")
                no_of_coins.grid(row=coin_rows, column=2, sticky=N + S + E + W)

                amount_paid = Label(crypto, text="${0:.2f}".format(total_paid), bg="white", fg="black",
                                    font="Roboto 12", padx="7", pady="7", borderwidth=2, relief="groove")
                amount_paid.grid(row=coin_rows, column=3, sticky=N + S + E + W)

                current_val = Label(crypto, text="${0:.2f}".format(current_value), bg="white",
                                    fg=coin_status(float("{0:.2f}".format(current_value))), font="Roboto 12", padx="7",
                                    pady="7", borderwidth=2, relief="groove")
                current_val.grid(row=coin_rows, column=4, sticky=N + S + E + W)

                pl_per_coin = Label(crypto, text="${0:.2f}".format(pl_percoin), bg="white",
                                    fg=coin_status(float("{0:.2f}".format(pl_percoin))), font="Roboto 12", padx="7",
                                    pady="7", borderwidth=2, relief="groove")
                pl_per_coin.grid(row=coin_rows, column=5, sticky=N + S + E + W)

                total_profitandloss_per_coin = Label(crypto, text="${0:.2f}".format(total_pl_percoin), bg="white",
                                                     fg=coin_status(float("{0:.2f}".format(total_pl_percoin))),
                                                     font="Roboto 12", padx="7", pady="7", borderwidth=2,
                                                     relief="groove")
                total_profitandloss_per_coin.grid(row=coin_rows, column=6, sticky=N + S + E + W)

                coin_rows += 1

    api = ""

    total_profitandloss = Label(crypto, text="${0:.2f}".format(total_pl), bg="white",
                                fg=coin_status(float("{0:.2f}".format(total_pl))), font="Roboto 12", padx="7", pady="7",
                                borderwidth=2, relief="groove")
    total_profitandloss.grid(row=coin_rows, column=6, sticky=N + S + E + W)

    total_currentvalue = Label(crypto, text="${0:.2f}".format(total_cv), bg="white", fg="black", font="Roboto 12",
                               padx="7", pady="7", borderwidth=2, relief="groove")
    total_currentvalue.grid(row=coin_rows, column=4, sticky=N + S + E + W)

    update = Button(crypto, text="Update", bg="skyblue", fg="white", font="Roboto 12", command=my_portfolio,
                    padx="7", pady="7", borderwidth=2, relief="groove")
    update.grid(row=coin_rows+1, column=6, sticky=N + S + E + W)

    print("Total Profit/Loss for Portfolio : ", total_pl)


name = Label(crypto, text="Coin Name", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7", pady="7",
             borderwidth=2, relief="groove")

name.grid(row=0, column=0, sticky=N + S + E + W)

price = Label(crypto, text="Price", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7", pady="7", borderwidth=2,
              relief="groove")
price.grid(row=0, column=1, sticky=N + S + E + W)

no_of_coins = Label(crypto, text="Number of Coins", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7", pady="7",
                    borderwidth=2, relief="groove")
no_of_coins.grid(row=0, column=2, sticky=N + S + E + W)

amount_paid = Label(crypto, text="Total Amount Paid", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7",
                    pady="7", borderwidth=2, relief="groove")
amount_paid.grid(row=0, column=3, sticky=N + S + E + W)

current_val = Label(crypto, text="Current Value", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7", pady="7",
                    borderwidth=2, relief="groove")
current_val.grid(row=0, column=4, sticky=N + S + E + W)

pl_per_coin = Label(crypto, text="Profit/Loss Per Coin", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7",
                    pady="7", borderwidth=2, relief="groove")
pl_per_coin.grid(row=0, column=5, sticky=N + S + E + W)

total_profitandloss = Label(crypto, text="Total Profit/Loss", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7",
                            pady="7", borderwidth=2, relief="groove")
total_profitandloss.grid(row=0, column=6, sticky=N + S + E + W)

my_portfolio()
crypto.mainloop()'''


conn.close()

print("-----Program Completed-----")
