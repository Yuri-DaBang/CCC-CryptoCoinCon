### THIS PROGRAM WAS INITIALLY MADE TO STUDY cryptocoin MAK=RKET AND SOMEHOW PREDICT ITS NEXT MOVE ###

from flask import Flask, jsonify, render_template
import os
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import webbrowser
import os
import math
from tabulate import tabulate
import string
import random
import time
from xmlrpc.client import DateTime, _datetime
import matplotlib.pyplot as plt
import mplcursors
import datetime


class cryptocoinMarket:
    def __init__(self):
        self.balance = 0  # Initialize balance to zero
        self.cryptocoins = {}  # Initialize cryptocoins dictionary to store user's cryptocoins

    cryptocoin_prices = {
        "Bitcoin": 0,
        "Ethereum": 0,
        "Binance Coin": 0,
        "Solana": 0,
        "Cardano": 0,
        "XRP": 0,
        "Polkadot": 0,
        "Dogecoin": 0,
        "Avalanche": 0,
        # "Chainlink": 0,
        # "Litecoin": 0,
        # "Bitcoin Cash": 0,
        # "Stellar": 0,
        # "VeChain": 0,
        # "THETA": 0,
        # "EOS": 0,
        # "Tron": 0,
        # "Monero": 0,
        # "Neo": 0,
        # "Cosmos": 0,
        # "Algorand": 0,
        # "Dash": 0,
        # "Compound": 0,
        # "Tezos": 0,
        # "Yearn.finance": 0,
        # "Hcoin": -999,
        # "A3NA COIN": 0,
        # "E SUPER COIN": 0,
        # Add more cryptocurrencies and their prices as needed
    }

    crypto_ids = {
        "Bitcoin": 1,
        "Ethereum": 2,
        "Binance Coin": 3,
        "Solana": 4,
        "Cardano": 5,
        "XRP": 6,
        "Polkadot": 7,
        "Dogecoin": 8,
        "Avalanche": 9,
        # "Chainlink": 10,
        # "Litecoin": 11,
        # "Bitcoin Cash": 12,
        # "Stellar": 13,
        # "VeChain": 14,
        # "THETA": 15,
        # "EOS": 16,
        # "Tron": 17,
        # "Monero": 18,
        # "Neo": 19,
        # "Cosmos": 20,
        # "Algorand": 21,
        # "Dash": 22,
        # "Compound": 23,
        # "Tezos": 24,
        # "Yearn_finance": 25,
        # "Hcoin": 26,
        # "A3NA COIN": 27,
        # "E SUPER COIN": 28,
        # Add more cryptocurrencies and their IDs as needed
    }



    def display_cryptocoin_prices(self):
        headers = ["ID", "Crypto", "Cryptocoin Price"]
        rows = []
        for idx, (crypto, price) in enumerate(self.cryptocoin_prices.items(), start=1):
            if price > 0:
                rows.append([idx, crypto, f"${price}"])
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    def get_crypto_name_from_id(self, crypto_id):
        # Reverse lookup to find crypto name from its ID
        for crypto_name, _id in self.crypto_ids.items():
            if _id == crypto_id:
                return crypto_name
        return None  # Return None if ID is not found
    # Function to update crypto prices in _new_cryptocoin_prices
    def update_crypto_prices(self, new_prices):
        for crypto, price in new_prices.items():
            if crypto in self.cryptocoin_prices:
                self.cryptocoin_prices[crypto] = price
                print(f"Updated price for {crypto} to ${price}")
            else:
                print(f"crypto {crypto} not found.")

        # Return the updated cryptocoin prices dictionary
        return self.cryptocoin_prices
                
    def get_cryptocoin_price(self, crypto):
        # Assuming cryptocoin_prices is a dictionary containing crypto names and their respective cryptocoin prices
       
        if crypto in cryptocoin_prices:
            return cryptocoin_prices[crypto]
        else:
            print(f"crypto {crypto} not found.")
            return None

        @staticmethod
        def withdraw(amount, balance, cryptocoins):
            # Withdraw funds from the cryptocoin market (from the last amount invested)
            if balance > 0:
                print(f"Withdrew ${amount} from the cryptocoin market.")
                balance = 0
                cryptocoins.clear()
            else:
                print("No funds available for withdrawal.")
            return balance
        
    class SELF:
        def Banner():
            print('''
 a88888b.  888888ba  dP    dP  888888ba  d888888P  .88888.     8888ba.88ba   .d888888   888888ba  dP     dP  88888888b d888888P (V=0.0.1-Beta)
d8'   `88  88    `8b Y8.  .8P  88    `8b    88    d8'   `8b    88  `8b  `8b d8'    88   88    `8b 88   .d8'  88           88    
88        a88aaaa8P'  Y8aa8P  a88aaaa8P'    88    88     88    88   88   88 88aaaaa88a a88aaaa8P' 88aaa8P'  a88aaaa       88    
88         88   `8b.    88     88           88    88     88    88   88   88 88     88   88   `8b. 88   `8b.  88           88    
Y8.   .88  88     88    88     88           88    Y8.   .8P    88   88   88 88     88   88     88 88     88  88           88    
 Y88888P'  dP     dP    dP     dP           dP     `8888P'     dP   dP   dP 88     88   dP     dP dP     dP  88888888P    dP        
            ''')
            
        def About():
            print('[*] The program, designed for studying the cryptocoin market and predicting its future trends, combines finance and computational expertise. It features a customized algorithm and interactive display, generating simulated timelines for analysis. With insightful comparisons, it evaluates equity shifts, making it a valuable tool for financial exploration.')
          
        
            
    class New:
        class Timeline:
            def _timeline_(cryptoName,InitialcryptocoinPrice,TimeLineLenght,__LIST_TIMELINE__):
            
                _price = InitialcryptocoinPrice
                _crypto  = cryptoName
                _timelenght  = TimeLineLenght
            
                _timeline = __LIST_TIMELINE__
                _allowed_value = [_price-10000,_price-9000,_price-8000,_price-7000,_price-6000,_price-5000,_price-4000,_price-3000,_price-2000,_price-1000,_price,_price+1000,_price+2000,_price+3000,_price+4000,_price+5000,_price+6000,_price+7000,_price+8000,_price+9000,_price+10]

                for  _ts in range(1,_timelenght):
                    _next_price = (random.choice(_allowed_value))
                    _timeline.append(_next_price)
                    _allowed_value = [_next_price-100000,_next_price-90000,_next_price-80000,_next_price-70000,_next_price-60000,_next_price-50000,_next_price-40000,_next_price-30000,_next_price-20000,_next_price-10000,_next_price,_next_price+10000,_next_price+20000,_next_price+30000,_next_price+40000,_next_price+50000,_next_price+60000,_next_price+70000,_next_price+80000,_next_price+90000,_next_price+10]
            
                return (_timeline)
           
            def algoCustumCustum(cryptoName, InitialcryptocoinPrice, TimeLineLength,CUSTUNCUSTUM):
                timeline = []
                price = InitialcryptocoinPrice
                _percentage = CUSTUNCUSTUM/100*price
    
                for _ in range(TimeLineLength):
                    # Generate random price within a reasonable range
                    next_price = random.uniform(price - _percentage, price + _percentage)
                    timeline.append(round(next_price, 2))
                    price = next_price
    
                return timeline
            
            def algo_unpredictable(cryptoName, InitialcryptocoinPrice, TimeLineLength,ccFORNORESION):
                timeline = []
                price = InitialcryptocoinPrice           

                _nums = []

                for _ in range(TimeLineLength+1):
         
                    # Randomly generate values for _
                    _ = random.randint(1, 100)

                    _nums.append(_ + random.randint(1, 100))            # Adding a random value to each operation
                    _nums.append(_ + random.randint(1, 500))            # Adding a random value to each operation
                    _nums.append(_ + random.randint(1, 2000))           # Adding a random value to each operation
                    _nums.append(_ * random.randint(1, 3))            # Multiplying by a random value
                    _nums.append(_ * random.randint(1, 50))            # Multiplying by a random value
                    _nums.append(_ * random.randint(1, 2))           # Multiplying by a random value
                    _nums.append(_ / random.randint(2, 20))             # Dividing by a random value
                    _nums.append(_ / random.randint(2, 10))            # Dividing by a random value
                    _nums.append(_ / random.randint(2, 2))            # Dividing by a random value
                    _nums.append(_ - random.randint(1, 50))             # Subtracting a random value
                    _nums.append(_ - random.randint(1, 200))            # Subtracting a random value
                    _nums.append(_ - random.randint(16 , 999))            # Subtracting a random value

                _percentage = []
     
                for _ in range(TimeLineLength+1):
                    _val = (random.choice(_nums))
                    _percentage.append(_val)

                for _ in range(TimeLineLength+1):
                    # Generate random price within a reasonable range
                    next_price = random.uniform(price - _percentage[_], price + _percentage[_])
                    timeline.append(round(next_price, 2))
                    price = next_price
    
                return timeline

            def algoTwentyTwenty(cryptoName, InitialcryptocoinPrice, TimeLineLength,ccFORNORESION):
                timeline = []
                price = InitialcryptocoinPrice
    
                for _ in range(TimeLineLength):
                    # Generate random price within a reasonable range
                    next_price = random.uniform(price - (20/100*price), price + (20/100*price))
                    timeline.append(round(next_price, 2))
                    price = next_price
    
                return timeline
            
            def custom_algorithm_SPACE_LEAVE(cryptoName, InitialcryptocoinPrice, TimeLineLength):
                timeline = []
                price = InitialcryptocoinPrice
    
                for _ in range(TimeLineLength):
                    # Generate a random fluctuation
                    # We can use a normal distribution to simulate more realistic price changes
                    # Adjust the standard deviation based on your desired volatility
                    fluctuation = random.normalvariate(0, 9999999)  # Adjust 50 according to your needs
                    # Apply the fluctuation to the current price
                    next_price = price + fluctuation
                    # Ensure that the price does not drop below zero
                    next_price = max(0, next_price)
                    timeline.append(round(next_price, 2))
                    price = next_price
    
                return timeline

    
    class Display:
        class _timeline_:
            def _ObO_(__LIST_TIMELINE__):
                for _i in __LIST_TIMELINE__:
                    print(f"??? >>> {_i}")
                    time.sleep(1)

            @staticmethod
            def _chart_simple_(crypto_data, title='Comparison of Companies based on cryptocoin Prices', xlabel='Time', ylabel='cryptocoin Price', figsize=(10, 6)):
                plt.figure(figsize=figsize)

                for crypto, (investment, prices) in crypto_data.items():
                    plt.plot(range(1, len(int(prices)) + 1), prices, label=crypto)

                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.title(title)
                plt.legend()
                plt.tight_layout()
                plt.show()
                
            @staticmethod
            def _chart_with_price_(company_data, title='Comparison of Companies based on Stock Prices', xlabel='Time', ylabel='Stock Price', figsize=(10, 6)):
                plt.figure(figsize=figsize)

                for company, (investment, prices) in company_data.items():
                    line, = plt.plot(range(1, len(prices) + 1), prices, label=company)

                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.title(title)
                plt.legend()
                plt.tight_layout()

                # Adding annotations using mplcursors
                mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Price: {sel.target[1]}"))

                plt.show()
        
            def _chart_with_price_modified_(crypto_data, title='Comparison of Companies based on cryptocoin Prices', xlabel='Time', ylabel='cryptocoin Price', figsize=(10, 6)):
                plt.figure(figsize=figsize)

                for crypto, (investment, prices) in crypto_data.items():
                    # Check if prices is a list or tuple before passing to len()
                    if isinstance(prices, (list, tuple)):
                        plt.plot(range(1, len(int(prices)) + 1), prices, label=crypto)
                    else:
                        print(f"Prices for {crypto} is not a sequence type.")

                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.title(title)
                plt.legend()
                plt.tight_layout()

                # Adding annotations using mplcursors
                cursor = mplcursors.cursor(hover=True)

                @cursor.connect("add")
                def on_add(sel):
                    x, y = map(int, sel.target)
                    # Set the annotation text at a fixed position (top-right corner) and display vertically
                    plt.text(0.98, 0.95, f"Time: {x}\n\n{''.join(f'{crypto}: {prices[x-1]}' for crypto, (_, prices) in crypto_data.items())}",
                                horizontalalignment='right',
                                verticalalignment='top',
                                transform=plt.gca().transAxes,
                                bbox=dict(facecolor='white', alpha=0.8))

                plt.show()
        @staticmethod
        def Price_chart_simulation(crypto_names, initial_prices, num_days=100):
            crypto_prices = {name: [price] for name, price in zip(crypto_names, initial_prices)}
            crypto_stocks = {name: 0 for name in crypto_names}
            current_day = 0

            def simulate_prices():
                nonlocal current_day
                for _ in range(num_days):
                    current_day += 1
                    for crypto in crypto_names:
                        change = random.uniform(-0.1, 0.1)  # Simulate daily price change
                        new_price = max(0, crypto_prices[crypto][-1] * (1 + change))
                        crypto_prices[crypto].append(new_price)

            simulate_prices()

            fig, ax = plt.subplots()

            def animate(i):
                ax.clear()
                ax.set_title("Live Cryptocurrency Prices")
                ax.set_xlabel("Time (days)")
                ax.set_ylabel("Price (USD)")
                for crypto in crypto_names:
                    ax.plot(range(len(crypto_prices[crypto])), crypto_prices[crypto], label=crypto)
                ax.legend()

            def on_key(event):
                nonlocal current_day
                if event.key == '+':
                    selected_crypto = input("Enter the name of the cryptocurrency to buy: ")
                    if selected_crypto in crypto_names:
                        crypto_stocks[selected_crypto] += 1
                        print(f"Bought 1 stock of {selected_crypto}.")
                elif event.key == '-':
                    selected_crypto = input("Enter the name of the cryptocurrency to sell: ")
                    if selected_crypto in crypto_names and crypto_stocks[selected_crypto] > 0:
                        crypto_stocks[selected_crypto] -= 1
                        print(f"Sold 1 stock of {selected_crypto}.")

            fig.canvas.mpl_connect('key_press_event', on_key)

            ani = animation.FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)  # Set cache_frame_data to False
            plt.show()


                    
    class Math:    
        class _compare_:
            def _wealth_(cryptoName, StartingPrice, EndingPrice):
                _total_income_ = (EndingPrice - StartingPrice) / StartingPrice * 100
                print('╔════════════════════════════════════════════════════════════════════════')
                print(f'║ {cryptoName} Analysis:                        ')
                print('╠════════════════════════════════════════════════════════════════════════')
                print(f'║ Started with: {StartingPrice:<20} ')
                print(f'║ Ended with:   {EndingPrice:<20} ')
                print(f'║ Change in equity: {_total_income_:.2f}%{" " * (11 - len(str(_total_income_)))}')
                if _total_income_ < 0:
                    _loss_ = StartingPrice - EndingPrice
                    print(f'║ {cryptoName} incurred a loss of {_loss_:<15},\n║ equivalent to {-_total_income_:.2f}% of the initial investment.  ')
                elif _total_income_ > 0:
                    _profit_ = EndingPrice - StartingPrice
                    print(f'║ {cryptoName} gained a profit of {_profit_:<15},\n║ equivalent to {_total_income_:.2f}% of the initial investment.    ')
                else:
                    print(f'║ {cryptoName} maintained the same equity level. Better luck next time!{" " * 17}')
                print('╚════════════════════════════════════════════════════════════════════════')
                


    class PortfolioManager:
        @staticmethod
        def invest(crypto, num_cryptocoins, balance, cryptocoins, cryptocoin_prices):
            # Check if the crypto exists and retrieve its cryptocoin price
            if crypto not in cryptocoin_prices:
                print(f"crypto {crypto} not found.")
                return balance

            cryptocoin_price = cryptocoin_prices[crypto]

            # Calculate the total cost of the investment
            total_cost = num_cryptocoins * cryptocoin_price

            # Check if the user has enough balance to make the investment
            if balance < total_cost:
                print("Insufficient funds to buy the specified number of cryptocoins.")
                return balance

            # Update user's balance and cryptocoins
            balance -= total_cost
            if crypto in cryptocoins:
                cryptocoins[crypto] += num_cryptocoins
            else:
                cryptocoins[crypto] = num_cryptocoins

            print(f"Bought {num_cryptocoins} cryptocoins of {crypto} at ${cryptocoin_price} each. (which is around {num_cryptocoins*cryptocoin_price})")
            return balance

        @staticmethod
        def withdraw(amount, balance, cryptocoins, cryptocoin_prices):
            # Calculate the current value of all cryptocoins owned by the user
            total_cryptocoin_value = sum(cryptocoins[crypto] * cryptocoin_prices[crypto] for crypto in cryptocoins)

            # Check if the user has enough balance to make the withdrawal
            if balance + total_cryptocoin_value < amount:
                print("Insufficient funds for withdrawal.")
                return balance

            # Update user's balance
            balance += amount

            # Sell all cryptocoins owned by the user
            for crypto, num_cryptocoins in list(cryptocoins.items()):
                balance += num_cryptocoins * cryptocoin_prices[crypto]
                del cryptocoins[crypto]

            print(f"Withdrew ${amount} from the cryptocoin market.")
            return balance

    
    
    class Wallet:
        def __init__(self, balance=0):
            self.balance = balance
            self.cryptocoins = {}

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds.")

        def buy_cryptocoin(self, crypto, num_cryptocoins, cryptocoin_price):
            total_cost = num_cryptocoins * cryptocoin_price
            if self.balance >= total_cost:
                if crypto in self.cryptocoins:
                    self.cryptocoins[crypto]["quantity"] += num_cryptocoins
                else:
                    self.cryptocoins[crypto] = {"price": cryptocoin_price, "quantity": num_cryptocoins}
                self.balance -= total_cost
                print(f"Bought {num_cryptocoins} cryptocoins of {crypto} at ${cryptocoin_price} each. (which is around {num_cryptocoins*cryptocoin_price})")
            else:
                print("Insufficient funds to buy cryptocoins.")

        def sell_cryptocoin(self, crypto, num_cryptocoins, cryptocoin_price):
            if crypto in self.cryptocoins and self.cryptocoins[crypto]["quantity"] >= num_cryptocoins:
                self.cryptocoins[crypto]["quantity"] -= num_cryptocoins
                sale_amount = num_cryptocoins * cryptocoin_price
                self.balance += sale_amount
                print(f"Sold {num_cryptocoins} cryptocoins of {crypto} at ${cryptocoin_price} each.")
            else:
                print("Insufficient cryptocoins to sell.")

        def portfolio_worth(self, cryptocoin_prices):
            total_worth = self.balance
            for crypto, info in self.cryptocoins.items():
                if crypto in cryptocoin_prices:
                    total_worth += info["quantity"] * cryptocoin_prices[crypto]
            return total_worth

        def print_balance(self, cryptocoin_prices):
            print("{:<36} | {:<15} | {:<15} | {:<55}".format("Item", "Price", "Quantity", "TOTAL"))
            print("-" * 110)
            print("{:<36} | {:<15} | {:<15} | {:<55}".format("DOLLAR", "1.000", self.balance, f"${self.balance}"))
            for crypto, info in self.cryptocoins.items():
                price = cryptocoin_prices.get(crypto, "N/A")  # Get updated price or "N/A" if not found
                if price != "N/A":
                    quantity = info["quantity"]
                    total = price * quantity
                    print("{:<36} | {:<15} | {:<15} | {:<55}".format(crypto, price, quantity, f"${total}"))
                    
        def print_balance_of_one_specfic_crypto(self, cryptocoin_prices,_target_crypto):
            for crypto, info in self.cryptocoins(_target_crypto):
                price = cryptocoin_prices.get(crypto, "N/A")  # Get updated price or "N/A" if not found
                if price != "N/A":
                    quantity = info["quantity"]
                    total = price * quantity
                    print("{:<10} = {:<20}".format(crypto, quantity))


    
    
    
    class Data:
        
        def generate_passwords(length, count):
            characters = string.digits
            passwords = []
            for _ in range(count):
                password = ''.join(random.choice(characters) for _ in range(length))
                passwords.append(password)
            return passwords

        def __save__(_df,_data,_spcchar):
            _return = '[!] SAVEING ...\n[+] DONE'
            
            characters = string.ascii_letters + string.digits + string.punctuation
            _uvtfyufvf = _spcchar
            
            _name_ = f'{_df}_{random.choice(_uvtfyufvf)}'

            os.system(f"cd E:\enchant\sbin\website(s)\YV-Ideology\SMPS\data\ && echo NEWFILE >> {_name_}.txt")
            with open(f'E:\enchant\sbin\website(s)\YV-Ideology\SMPS\data\{_name_}.txt','w') as _datafile:
                _datafile.write(f'{_data}')
                #_datafile.write(jsonify(_data))

            return _return

        def __load__(_df):
            _return=''
            
            with open(f'/data/{_df}.json','rb') as _datafile:
                _return = _datafile.read()
                #_datafile.write(jsonify(_data))

            return _return
            



             
                      
        

   
    
