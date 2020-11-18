# COIN_MARKET_API Project
from tkinter import *
import requests
import json
import sqlite3

conn = sqlite3.connect('coin.db')
cObj = conn.cursor()

cObj.execute("CREATE TABLE IF NOT EXISTS coins (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, symbol TEXT, amount INTEGER, Price REAL )")
conn.commit()

# GUI
crypto = Tk()
crypto.title("Crypto-Currency Portfolio")
crypto.iconbitmap('Favicon.ico')



def my_portfolio():
    # Calling API
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD""&CMC_PRO_API_KEY")

    # Loading Stored Data
    api = json.loads(api_request.content)

    cObj.execute("SELECT * FROM coins")
    coins = cObj.fetchall()

    #Coin Color
    def coin_status(amount):
        if amount >= 0:
            return "green"
        else:
            return "red"

    total_pl = 0 #Total Profit/Loss
    coin_rows = 1
    total_cv = 0 #Total Coin Value
    total_ap = 0 #Total Amount Paid

    for i in range(10):
        for coin in coins:
            if coin[2] == api["data"][i]["symbol"]:
                # Total Amount Paid
                total_paid = coin[3] * coin[4]

                # Current Value of Coin
                current_value = coin[3] * api["data"][i]["quote"]["USD"]["price"]

                # Profit/Loss for Coin
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin[4]

                # Total Profit/Loss Per-coin
                total_pl_percoin = pl_percoin * coin[3]

                # Total P/L
                total_pl = total_pl + total_pl_percoin

                # Total Current Value
                total_cv += current_value

                #Total Amount Paid
                total_ap += total_paid

                port_id = Label(crypto, text=coin[0], bg="white", fg="black",
                             font="Roboto 12", padx="7",
                             pady="7", borderwidth=2, relief="groove")
                port_id.grid(row=coin_rows, column=0, sticky=N + S + E + W)

                symbol = Label(crypto, text=coin[2], bg="white", fg="black",
                             font="Roboto 12", padx="7",
                             pady="7", borderwidth=2, relief="groove")
                symbol.grid(row=coin_rows, column=2, sticky=N + S + E + W)

                price = Label(crypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white",
                              fg="black", font="Roboto 12", padx="7", pady="7", borderwidth=2, relief="groove")
                price.grid(row=coin_rows, column=3, sticky=N + S + E + W)

                no_of_coins = Label(crypto, text="${0:.2f}".format(coin[3]), bg="white", fg="black",
                                    font="Roboto 12", padx="7", pady="7", borderwidth=2, relief="groove")
                no_of_coins.grid(row=coin_rows, column=4, sticky=N + S + E + W)

                amount_paid = Label(crypto, text="${0:.2f}".format(total_paid), bg="white", fg="black",
                                    font="Roboto 12", padx="7", pady="7", borderwidth=2, relief="groove")
                amount_paid.grid(row=coin_rows, column=5, sticky=N + S + E + W)

                current_val = Label(crypto, text="${0:.2f}".format(current_value), bg="white",
                                    fg=coin_status(float("{0:.2f}".format(current_value))), font="Roboto 12", padx="7",
                                    pady="7", borderwidth=2, relief="groove")
                current_val.grid(row=coin_rows, column=6, sticky=N + S + E + W)

                pl_per_coin = Label(crypto, text="${0:.2f}".format(pl_percoin), bg="white",
                                    fg=coin_status(float("{0:.2f}".format(pl_percoin))), font="Roboto 12", padx="7",
                                    pady="7", borderwidth=2, relief="groove")
                pl_per_coin.grid(row=coin_rows, column=7, sticky=N + S + E + W)

                total_profitandloss_per_coin = Label(crypto, text="${0:.2f}".format(total_pl_percoin), bg="white",
                                                     fg=coin_status(float("{0:.2f}".format(total_pl_percoin))),
                                                     font="Roboto 12", padx="7", pady="7", borderwidth=2,
                                                     relief="groove")
                total_profitandloss_per_coin.grid(row=coin_rows, column=8, sticky=N + S + E + W)

                coin_rows += 1

    api = ""

    #Total Amount Paid
    total_amountpaid = Label(crypto, text="${0:.2f}".format(total_ap), bg="white", fg="black", font="Roboto 12",
                               padx="7", pady="7", borderwidth=2, relief="groove")
    total_amountpaid.grid(row=coin_rows, column=5, sticky=N + S + E + W)

    #Total Current Value
    total_currentvalue = Label(crypto, text="${0:.2f}".format(total_cv), bg="white",
                               fg=coin_status(float("{0:.2f}".format(total_cv))), font="Roboto 12",
                               padx="7", pady="7", borderwidth=2, relief="groove")
    total_currentvalue.grid(row=coin_rows, column=6, sticky=N + S + E + W)

    #Total Profit/Loss
    total_profitandloss = Label(crypto, text="${0:.2f}".format(total_pl), bg="white",
                                fg=coin_status(float("{0:.2f}".format(total_pl))), font="Roboto 12", padx="7", pady="7",
                                borderwidth=2, relief="groove")
    total_profitandloss.grid(row=coin_rows, column=8, sticky=N + S + E + W)


    #Add Coins Buttons
    coin_name_txt = Entry(crypto, bg="white",fg="black", font="Roboto 12", borderwidth=2, relief="groove")
    coin_name_txt.grid(row=coin_rows + 1, column=1, sticky=N + S + E + W)

    coin_symbol_txt = Entry(crypto, bg="white",fg="black", font="Roboto 12", borderwidth=2, relief="groove")
    coin_symbol_txt.grid(row=coin_rows + 1, column=2, sticky=N + S + E + W)

    coin_ppaid_txt = Entry(crypto, bg="white",fg="black", font="Roboto 12", borderwidth=2, relief="groove")
    coin_ppaid_txt.grid(row=coin_rows + 1, column=3, sticky=N + S + E + W)

    coin_amount_txt = Entry(crypto, bg="white",fg="black", font="Roboto 12", borderwidth=2, relief="groove")
    coin_amount_txt.grid(row=coin_rows + 1, column=6, sticky=N + S + E + W)

    add_coin_btn = Button(crypto, text="Refresh", bg="#1d1d7c", fg="white", font="Roboto 12", command=my_portfolio,
                     padx="7", pady="7", borderwidth=5, relief="groove")
    add_coin_btn.grid(row=coin_rows + 1, column=6, sticky=N + S + E + W)

    #Refresh Button
    refresh = Button(crypto, text="Refresh", bg="#1d1d7c", fg="white", font="Roboto 12", command=my_portfolio,
                    padx="7", pady="7", borderwidth=2, relief="groove")
    refresh.grid(row=coin_rows+1, column=8, sticky=N + S + E + W)

    print("Total Profit/Loss for Portfolio : ", total_pl)

def app_header():

    portfolio_id = Label(crypto, text="Portfolio ID", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7", pady="7",
                 borderwidth=2, relief="groove")

    portfolio_id.grid(row=0, column=0, sticky=N + S + E + W)

    symbol = Label(crypto, text="Coin Symbol", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7", pady="7",
                 borderwidth=2, relief="groove")

    symbol.grid(row=0, column=2, sticky=N + S + E + W)

    price = Label(crypto, text="Price", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7", pady="7",
                  borderwidth=2,
                  relief="groove")
    price.grid(row=0, column=3, sticky=N + S + E + W)

    no_of_coins = Label(crypto, text="Number of Coins", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7",
                        pady="7",
                        borderwidth=2, relief="groove")
    no_of_coins.grid(row=0, column=4, sticky=N + S + E + W)

    amount_paid = Label(crypto, text="Total Amount Paid", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7",
                        pady="7", borderwidth=2, relief="groove")
    amount_paid.grid(row=0, column=5, sticky=N + S + E + W)

    current_val = Label(crypto, text="Current Value", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7",
                        pady="7",
                        borderwidth=2, relief="groove")
    current_val.grid(row=0, column=6, sticky=N + S + E + W)

    pl_per_coin = Label(crypto, text="Profit/Loss Per Coin", bg="#1d1d7c", fg="white", font="Roboto 12 bold", padx="7",
                        pady="7", borderwidth=2, relief="groove")
    pl_per_coin.grid(row=0, column=7, sticky=N + S + E + W)

    total_profitandloss = Label(crypto, text="Total Profit/Loss", bg="#1d1d7c", fg="white", font="Roboto 12 bold",
                                padx="7",
                                pady="7", borderwidth=2, relief="groove")
    total_profitandloss.grid(row=0, column=8, sticky=N + S + E + W)

app_header()
my_portfolio()
crypto.mainloop()


conn.close()

print("-----Program Completed-----")

