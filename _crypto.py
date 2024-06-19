from ast import While
from asyncio.windows_events import NULL
import os
import random
import clpsLIB as _smps
import string
import _webapp as _website

_market = _smps.cryptocoinMarket()
_market.SELF.Banner()

print()
print()

global _ep_bitcoin_
global _ep_solana_
global _ep_ethereum_

import random

# Generating a list of one hundred random numbers
_randum_prices = [random.randint(-4250, 99000) for _ in range(9999)]

# Assigning new random prices to cryptocurrencies
new_prices = {
    "Hcoin": random.choice(_randum_prices),         # Updated price for Hcoin
    "A3NA COIN": random.choice(_randum_prices),     # Updated price for A3NA COIN
    "E SUPER COIN": random.choice(_randum_prices),  # Updated price for E SUPER COIN
    "Bitcoin": random.choice(_randum_prices),       # Updated price for Bitcoin
    "Ethereum": random.choice(_randum_prices),      # Updated price for Ethereum
    "Binance Coin": random.choice(_randum_prices),  # Updated price for Binance Coin
    "Solana": random.choice(_randum_prices),        # Updated price for Solana
    "Cardano": random.choice(_randum_prices),       # Updated price for Cardano
    "XRP": random.choice(_randum_prices),           # Updated price for XRP
    "Polkadot": random.choice(_randum_prices),      # Updated price for Polkadot
    "Dogecoin": random.choice(_randum_prices),      # Updated price for Dogecoin
    "Avalanche": random.choice(_randum_prices),     # Updated price for Avalanche
    # "Chainlink": random.choice(_randum_prices),     # Updated price for Chainlink
    # "Litecoin": random.choice(_randum_prices),      # Updated price for Litecoin
    # "Bitcoin Cash": random.choice(_randum_prices),  # Updated price for Bitcoin Cash
    # "Stellar": random.choice(_randum_prices),      # Updated price for Stellar
    # "VeChain": random.choice(_randum_prices),       # Updated price for VeChain
    # "THETA": random.choice(_randum_prices),         # Updated price for THETA
    # "EOS": random.choice(_randum_prices),           # Updated price for EOS
    # "Tron": random.choice(_randum_prices),          # Updated price for Tron
    # "Monero": random.choice(_randum_prices),        # Updated price for Monero
    # "Neo": random.choice(_randum_prices),           # Updated price for Neo
    # "Cosmos": random.choice(_randum_prices),        # Updated price for Cosmos
    # "Algorand": random.choice(_randum_prices),      # Updated price for Algorand
    # "Dash": random.choice(_randum_prices),          # Updated price for Dash
    # "Compound": random.choice(_randum_prices),      # Updated price for Compound
    # "Tezos": random.choice(_randum_prices),         # Updated price for Tezos
    # Add more cryptocurrencies and their updated prices as needed
}

# Creating a timeline list
_timelineLIST = []

# Creating variables for each cryptocurrency price
_tl_bitcoin = [_market.cryptocoin_prices["Bitcoin"]]
_tl_ethereum = [_market.cryptocoin_prices["Ethereum"]]
_tl_binance_coin = [_market.cryptocoin_prices["Binance Coin"]]
_tl_solana = [_market.cryptocoin_prices["Solana"]]
_tl_cardano = [_market.cryptocoin_prices["Cardano"]]
_tl_xrp = [_market.cryptocoin_prices["XRP"]]
_tl_polkadot = [_market.cryptocoin_prices["Polkadot"]]
_tl_dogecoin = [_market.cryptocoin_prices["Dogecoin"]]
_tl_avalanche = [_market.cryptocoin_prices["Avalanche"]]
# _tl_chainlink = [_market.cryptocoin_prices["Chainlink"]]
# _tl_litecoin = [_market.cryptocoin_prices["Litecoin"]]
# _tl_bitcoin_cash = [_market.cryptocoin_prices["Bitcoin Cash"]]
# _tl_stellar = [_market.cryptocoin_prices["Stellar"]]
# _tl_vechain = [_market.cryptocoin_prices["VeChain"]]
# _tl_theta = [_market.cryptocoin_prices["THETA"]]
# _tl_eos = [_market.cryptocoin_prices["EOS"]]
# _tl_tron = [_market.cryptocoin_prices["Tron"]]
# _tl_monero = [_market.cryptocoin_prices["Monero"]]
# _tl_neo = [_market.cryptocoin_prices["Neo"]]
# _tl_cosmos = [_market.cryptocoin_prices["Cosmos"]]
# _tl_algorand = [_market.cryptocoin_prices["Algorand"]]
# _tl_dash = [_market.cryptocoin_prices["Dash"]]
# _tl_compound = [_market.cryptocoin_prices["Compound"]]
# _tl_tezos = [_market.cryptocoin_prices["Tezos"]]
# # Add more _tl_* variables for other cryptocurrencies as needed

# _tl_hcoin = [_market.cryptocoin_prices["Hcoin"]]
# _tl_solana = [_market.cryptocoin_prices["A3NA COIN"]]
# _tl_ethereum = [_market.cryptocoin_prices["E SUPER COIN"]]
# # Add more _tl_* variables for other cryptocurrencies as needed

global _investment_into_wallet 
_investment_into_wallet = 1000000

_max_timeline_ = 20000
    
#_investment_ = 10000

# Instantiate the Wallet class
wallet = _market.Wallet()
# Invest in multiple companies
wallet.deposit(_investment_into_wallet)  # Deposit MONEY into the wallet

username = input("what is your name: ")

_randum_prices=[]

updated_prices = _market.update_crypto_prices(new_prices)

def __help():
    print('_invest.py USAGE:')
    print('''
opt | description                   | Later ./args
.   | .                             | .  
..  | ..                            | ..            
 1  | to show account balance       | l()
 2  | to show cryptocoin balance    | l()
 3  | to list cryptos               | l()
 4  | to buy cryptocoins of cryptos | l(_name,_number_of_cryptocoins)
 4b | to sell cryptocoins of cryptos| l(_name,_number_of_cryptocoins)         
 5  | to create a timeline          | l(_time_lenght,_change_ratio)
 6  | to compare your earnings      | l()       
 7  | to save and exit              | l()
 8  | help                          | l()         
''')
    
__help()

while True:
     try:
        #__help()
        print()
        _option = input(f'{username} ==> ')
        
        if _option == '8':
            __help()
        elif _option == '7':
            #Save user balance and cryptocoin information to file
            portfolio_worth = wallet.portfolio_worth(updated_prices)
            _market.Data.__save__("user_balance", f'DATA WITH ALGO (CustomCustom) with _change_ratio == {_change_ratio} and _timeline_ == {_tlL}:\n\n USER:{username}, started with just ({_investment_into_wallet}), bought many cryptocoins and earned a total of ({portfolio_worth})\n and his summry is as follows\n{wallet.print_balance(updated_prices)}{"balance": wallet.balance, "cryptocoins": wallet.cryptocoins}', string.ascii_letters + string.digits + string.punctuation)
        elif _option == '1':
            portfolio_worth = wallet.portfolio_worth(updated_prices)
            print(f"Portfolio worth: ${portfolio_worth}")
        elif _option == '2':
            # Print balance with updated prices
            wallet.print_balance(updated_prices)
        elif _option == '3':
            _market.display_cryptocoin_prices()
        elif _option == '4':
            print()
            _comname = input('Crypto Name Or ID: ')
            if _comname != '':
                if _comname.isdigit():
                    _index = int(_comname) - 1
                    cryptos = list(_market.cryptocoin_prices.keys())
                    if 0 <= _index < len(cryptos):
                        _comname = cryptos[_index]
                        print(f'PRICE OF ONE SHARE ({_comname}):', _market.cryptocoin_prices[_comname])
                        if _market.cryptocoin_prices[_comname] <= 0:
                            print(f'[-] YOU CANNOT BUY CRYPTOCOINS OF THIS CRYPTO ({_comname}) (price is less)')
                        else:
                            print(f'Number of cryptocoins to BUY of crypto ({_comname})\nMAX is : {wallet.balance /_market.cryptocoin_prices[_comname]}')
                            _numcryptocoins = input(f'>>>')
                            try:
                                wallet.buy_cryptocoin(_comname, float(_numcryptocoins), _market.cryptocoin_prices[_comname])  # Buy cryptocoins of specified crypto
                            except:
                                print('[-] Error')
                    else:
                        print('[!] Invalid Crypto ID')
                else:
                    print(f'[!] Invalid Crypto ID')
            else:
                print('[-] Exception (USER MISTAKE)')
        elif _option == '4b':
            print()
            _comname = input('Crypto Name Or ID: ')
            if _comname != '':
                if _comname.isdigit():
                    _index = int(_comname) - 1
                    cryptos = list(_market.cryptocoin_prices.keys())
                    if 0 <= _index < len(cryptos):
                        _comname = cryptos[_index]
                        print(f'PRICE OF ONE SHARE ({_comname}):', _market.cryptocoin_prices[_comname])
                        
                        print(f'Number of cryptocoins to SELL of crypto ({_comname})\nMAX is : {wallet.cryptocoins[_comname]["quantity"]}')
                        _numcryptocoins = input(f'>>>')

                        try:
                            wallet.sell_cryptocoin(_comname, float(_numcryptocoins), _market.cryptocoin_prices[_comname])  # Sell cryptocoins of specified crypto
                        except:
                            print('[-] Error')
                    else:
                        print('[!] Invalid Crypto ID')
                else:
                    print(f'[!] Invalid Crypto ID')
            else:
                print('[-] Exception (USER MISTAKE)')
        elif _option == '5':
             print()

             _tlL = int(input('How much time difference (e.g. 50,200,1000) (below 20000): '))
             if _max_timeline_ >= _tlL:
                 _change_ratio = int(input('How much market change ratio should be (in %age) (e.g. 55,25,99,1,43) (below 100): '))              

                 _tl_bitcoin = _market.New.Timeline.algoTwentyTwenty("bitcoin",_market.cryptocoin_prices["Bitcoin"], _tlL,_change_ratio)
                 _tl_ethereum = _market.New.Timeline.algoTwentyTwenty("ethereum",_market.cryptocoin_prices["Ethereum"], _tlL,_change_ratio)
                 _tl_binance_coin = _market.New.Timeline.algoTwentyTwenty("binance_coin",_market.cryptocoin_prices["Binance Coin"], _tlL,_change_ratio)
                 _tl_solana = _market.New.Timeline.algoTwentyTwenty("solana",_market.cryptocoin_prices["Solana"], _tlL,_change_ratio)
                 _tl_cardano = _market.New.Timeline.algoTwentyTwenty("cardano",_market.cryptocoin_prices["Cardano"], _tlL,_change_ratio)
                 _tl_xrp = _market.New.Timeline.algoTwentyTwenty("xrp",_market.cryptocoin_prices["XRP"], _tlL,_change_ratio)
                 _tl_polkadot = _market.New.Timeline.algoTwentyTwenty("polkadot",_market.cryptocoin_prices["Polkadot"], _tlL,_change_ratio)
                 _tl_dogecoin = _market.New.Timeline.algoTwentyTwenty("dogecoin",_market.cryptocoin_prices["Dogecoin"], _tlL,_change_ratio)
                 _tl_avalanche = _market.New.Timeline.algoTwentyTwenty("avalanche",_market.cryptocoin_prices["Avalanche"], _tlL,_change_ratio)
                 # _tl_chainlink = _market.New.Timeline.algoTwentyTwenty("chainlink",_market.cryptocoin_prices["Chainlink"], _tlL,_change_ratio)
                 # _tl_litecoin = _market.New.Timeline.algoTwentyTwenty("litecoin",_market.cryptocoin_prices["Litecoin"], _tlL,_change_ratio)
                 # _tl_bitcoin_cash = _market.New.Timeline.algoTwentyTwenty("bitcoin_cash",_market.cryptocoin_prices["Bitcoin Cash"], _tlL,_change_ratio)
                 # _tl_stellar = _market.New.Timeline.algoTwentyTwenty("stellar",_market.cryptocoin_prices["Stellar"], _tlL,_change_ratio)
                 # _tl_vechain = _market.New.Timeline.algoTwentyTwenty("vechain",_market.cryptocoin_prices["VeChain"], _tlL,_change_ratio)
                 # _tl_theta = _market.New.Timeline.algoTwentyTwenty("theta",_market.cryptocoin_prices["THETA"], _tlL,_change_ratio)
                 # _tl_eos = _market.New.Timeline.algoTwentyTwenty("eos",_market.cryptocoin_prices["EOS"], _tlL,_change_ratio)
                 # _tl_tron = _market.New.Timeline.algoTwentyTwenty("tron",_market.cryptocoin_prices["Tron"], _tlL,_change_ratio)
                 # _tl_monero = _market.New.Timeline.algoTwentyTwenty("monero",_market.cryptocoin_prices["Monero"], _tlL,_change_ratio)
                 # _tl_neo = _market.New.Timeline.algoTwentyTwenty("neo",_market.cryptocoin_prices["Neo"], _tlL,_change_ratio)
                 # _tl_cosmos = _market.New.Timeline.algoTwentyTwenty("cosmos",_market.cryptocoin_prices["Cosmos"], _tlL,_change_ratio)
                 # _tl_algorand = _market.New.Timeline.algoTwentyTwenty("algorand",_market.cryptocoin_prices["Algorand"], _tlL,_change_ratio)
                 # _tl_dash = _market.New.Timeline.algoTwentyTwenty("dash",_market.cryptocoin_prices["Dash"], _tlL,_change_ratio)
                 # _tl_compound = _market.New.Timeline.algoTwentyTwenty("compound",_market.cryptocoin_prices["Compound"], _tlL,_change_ratio)
                 # _tl_tezos = _market.New.Timeline.algoTwentyTwenty("tezos",_market.cryptocoin_prices["Tezos"], _tlL,_change_ratio)
                 # _tl_hcoin = _market.New.Timeline.algoTwentyTwenty("hcoin",_market.cryptocoin_prices["Hcoin"], _tlL,_change_ratio)
                 # _tl_a3na_coin = _market.New.Timeline.algoTwentyTwenty("a3na_coin",_market.cryptocoin_prices["A3NA COIN"], _tlL,_change_ratio)
                 # _tl_e_super_coin = _market.New.Timeline.algoTwentyTwenty("e_super_coin",_market.cryptocoin_prices["E SUPER COIN"], _tlL,_change_ratio)

                 _ep_bitcoin_ = _tl_bitcoin[-1]
                 _ep_ethereum_ = _tl_ethereum[-1]
                 _ep_binance_coin_ = _tl_binance_coin[-1]
                 _ep_solana_ = _tl_solana[-1]
                 _ep_cardano_ = _tl_cardano[-1]
                 _ep_xrp_ = _tl_xrp[-1]
                 _ep_polkadot_ = _tl_polkadot[-1]
                 _ep_dogecoin_ = _tl_dogecoin[-1]
                 _ep_avalanche_ = _tl_avalanche[-1]
                 # _ep_chainlink_ = _tl_chainlink[-1]
                 # _ep_litecoin_ = _tl_litecoin[-1]
                 # _ep_bitcoin_cash_ = _tl_bitcoin_cash[-1]
                 # _ep_stellar_ = _tl_stellar[-1]
                 # _ep_vechain_ = _tl_vechain[-1]
                 # _ep_theta_ = _tl_theta[-1]
                 # _ep_eos_ = _tl_eos[-1]
                 # _ep_tron_ = _tl_tron[-1]
                 # _ep_monero_ = _tl_monero[-1]
                 # _ep_neo_ = _tl_neo[-1]
                 # _ep_cosmos_ = _tl_cosmos[-1]
                 # _ep_algorand_ = _tl_algorand[-1]
                 # _ep_dash_ = _tl_dash[-1]
                 # _ep_compound_ = _tl_compound[-1]
                 # _ep_tezos_ = _tl_tezos[-1]
                 # _ep_hcoin_ = _tl_hcoin[-1]
                 # _ep_a3na_coin_ = _tl_a3na_coin[-1]
                 # _ep_e_super_coin_ = _tl_e_super_coin[-1]

                 _market.cryptocoin_prices["Bitcoin"] = _ep_bitcoin_
                 _market.cryptocoin_prices["Ethereum"] = _ep_ethereum_
                 _market.cryptocoin_prices["Binance Coin"] = _ep_binance_coin_
                 _market.cryptocoin_prices["Solana"] = _ep_solana_
                 _market.cryptocoin_prices["Cardano"] = _ep_cardano_
                 _market.cryptocoin_prices["XRP"] = _ep_xrp_
                 _market.cryptocoin_prices["Polkadot"] = _ep_polkadot_
                 _market.cryptocoin_prices["Dogecoin"] = _ep_dogecoin_
                 # _market.cryptocoin_prices["Avalanche"] = _ep_avalanche_
                 # _market.cryptocoin_prices["Chainlink"] = _ep_chainlink_
                 # _market.cryptocoin_prices["Litecoin"] = _ep_litecoin_
                 # _market.cryptocoin_prices["Bitcoin Cash"] = _ep_bitcoin_cash_
                 # _market.cryptocoin_prices["Stellar"] = _ep_stellar_
                 # _market.cryptocoin_prices["VeChain"] = _ep_vechain_
                 # _market.cryptocoin_prices["THETA"] = _ep_theta_
                 # _market.cryptocoin_prices["EOS"] = _ep_eos_
                 # _market.cryptocoin_prices["Tron"] = _ep_tron_
                 # _market.cryptocoin_prices["Monero"] = _ep_monero_
                 # _market.cryptocoin_prices["Neo"] = _ep_neo_
                 # _market.cryptocoin_prices["Cosmos"] = _ep_cosmos_
                 # _market.cryptocoin_prices["Algorand"] = _ep_algorand_
                 # _market.cryptocoin_prices["Dash"] = _ep_dash_
                 # _market.cryptocoin_prices["Compound"] = _ep_compound_
                 # _market.cryptocoin_prices["Tezos"] = _ep_tezos_
                 # _market.cryptocoin_prices["Hcoin"] = _ep_hcoin_
                 # _market.cryptocoin_prices["A3NA COIN"] = _ep_a3na_coin_
                 # _market.cryptocoin_prices["E SUPER COIN"] = _ep_e_super_coin_

                 _tl_bitcoin.append(_ep_bitcoin_)
                 _tl_ethereum.append(_ep_ethereum_)
                 _tl_binance_coin.append(_ep_binance_coin_)
                 _tl_solana.append(_ep_solana_)
                 _tl_cardano.append(_ep_cardano_)
                 _tl_xrp.append(_ep_xrp_)
                 _tl_polkadot.append(_ep_polkadot_)
                 _tl_dogecoin.append(_ep_dogecoin_)
                 _tl_avalanche.append(_ep_avalanche_)
                 # _tl_chainlink.append(_ep_chainlink_)
                 # _tl_litecoin.append(_ep_litecoin_)
                 # _tl_bitcoin_cash.append(_ep_bitcoin_cash_)
                 # _tl_stellar.append(_ep_stellar_)
                 # _tl_vechain.append(_ep_vechain_)
                 # _tl_theta.append(_ep_theta_)
                 # _tl_eos.append(_ep_eos_)
                 # _tl_tron.append(_ep_tron_)
                 # _tl_monero.append(_ep_monero_)
                 # _tl_neo.append(_ep_neo_)
                 # _tl_cosmos.append(_ep_cosmos_)
                 # _tl_algorand.append(_ep_algorand_)
                 # _tl_dash.append(_ep_dash_)
                 # _tl_compound.append(_ep_compound_)
                 # _tl_tezos.append(_ep_tezos_)
                 # _tl_hcoin.append(_ep_hcoin_)
                 # _tl_a3na_coin.append(_ep_a3na_coin_)
                 # _tl_e_super_coin.append(_ep_e_super_coin_)

                 new_prices = {
                 "Bitcoin": _ep_bitcoin_,
                 "Ethereum": _ep_ethereum_,
                 "Binance Coin": _ep_binance_coin_,
                 "Solana": _ep_solana_,
                 "Cardano": _ep_cardano_,
                 "XRP": _ep_xrp_,
                 "Polkadot": _ep_polkadot_,
                 "Dogecoin": _ep_dogecoin_,
                 "Avalanche": _ep_avalanche_,
                 # "Chainlink": _ep_chainlink_,
                 # "Litecoin": _ep_litecoin_,
                 # "Bitcoin Cash": _ep_bitcoin_cash_,
                 # "Stellar": _ep_stellar_,
                 # "VeChain": _ep_vechain_,
                 # "THETA": _ep_theta_,
                 # "EOS": _ep_eos_,
                 # "Tron": _ep_tron_,
                 # "Monero": _ep_monero_,
                 # "Neo": _ep_neo_,
                 # "Cosmos": _ep_cosmos_,
                 # "Algorand": _ep_algorand_,
                 # "Dash": _ep_dash_,
                 # "Compound": _ep_compound_,
                 # "Tezos": _ep_tezos_,
                 # "Hcoin": _ep_hcoin_,
                 # "A3NA COIN": _ep_a3na_coin_,
                 # "E SUPER COIN": _ep_e_super_coin_
                 }

                 updated_prices = _market.update_crypto_prices(new_prices)

                 _chart_data = {
                 "Bitcoin": (_market.cryptocoin_prices["Bitcoin"], (_tl_bitcoin)),
                 "Ethereum": (_market.cryptocoin_prices["Ethereum"], (_tl_ethereum)),
                 "Binance Coin": (_market.cryptocoin_prices["Binance Coin"], (_tl_binance_coin)),
                 "Solana": (_market.cryptocoin_prices["Solana"], (_tl_solana)),
                 "Cardano": (_market.cryptocoin_prices["Cardano"], (_tl_cardano)),
                 "XRP": (_market.cryptocoin_prices["XRP"], (_tl_xrp)),
                 "Polkadot": (_market.cryptocoin_prices["Polkadot"], (_tl_polkadot)),
                 "Dogecoin": (_market.cryptocoin_prices["Dogecoin"], (_tl_dogecoin)),
                 "Avalanche": (_market.cryptocoin_prices["Avalanche"], (_tl_avalanche)),
                 # "Chainlink": (_market.cryptocoin_prices["Chainlink"], (_tl_chainlink)),
                 # "Litecoin": (_market.cryptocoin_prices["Litecoin"], (_tl_litecoin)),
                 # "Bitcoin Cash": (_market.cryptocoin_prices["Bitcoin Cash"], (_tl_bitcoin_cash)),
                 # "Stellar": (_market.cryptocoin_prices["Stellar"], (_tl_stellar)),
                 # "VeChain": (_market.cryptocoin_prices["VeChain"], (_tl_vechain)),
                 # "THETA": (_market.cryptocoin_prices["THETA"], (_tl_theta)),
                 # "EOS": (_market.cryptocoin_prices["EOS"], (_tl_eos)),
                 # "Tron": (_market.cryptocoin_prices["Tron"], (_tl_tron)),
                 # "Monero": (_market.cryptocoin_prices["Monero"], (_tl_monero)),
                 # "Neo": (_market.cryptocoin_prices["Neo"], (_tl_neo)),
                 # "Cosmos": (_market.cryptocoin_prices["Cosmos"], (_tl_cosmos)),
                 # "Algorand": (_market.cryptocoin_prices["Algorand"], (_tl_algorand)),
                 # "Dash": (_market.cryptocoin_prices["Dash"], (_tl_dash)),
                 # "Compound": (_market.cryptocoin_prices["Compound"], (_tl_compound)),
                 # "Tezos": (_market.cryptocoin_prices["Tezos"], (_tl_tezos)),
                 # "Hcoin": (_market.cryptocoin_prices["Hcoin"], (_tl_hcoin)),
                 # "A3NA COIN": (_market.cryptocoin_prices["A3NA COIN"], (_tl_a3na_coin)),
                 # "E SUPER COIN": (_market.cryptocoin_prices["E SUPER COIN"], (_tl_e_super_coin))
                 }
                 #_website.runwebsite(_chart_data)
                 _market.Display._timeline_._chart_with_price_(_chart_data)   
             else:
                 print(f'[!] Your given timeline ({_tlL}) is greater or equal then ({_max_timeline_}), so we cannot process it because of computer reasons, to change this simple change _max_timeline_ to whatever you want!.')
        elif _option == '5a':
            # Example usage:
           
            # Example usage:
            cryptocurrencies = ["Bitcoin", "Ethereum", "Binance Coin", "Solana", "Cardano"]
            initial_prices = [random.uniform(50000, 70000) for _ in range(len(cryptocurrencies))]
            _market.Display.Price_chart_simulation(cryptocurrencies, initial_prices)
        elif _option == '6':
            _profit = wallet.balance
            
            if _profit >= _investment_into_wallet:
                _total_profit = wallet.balance / _investment_into_wallet * 100
                _profit_money = _total_profit /100 * _investment_into_wallet
                print(f'\n HURRAH! GOOD WORK, You had a profot of {_total_profit} which is around {_profit_money}')
            elif _profit <= _investment_into_wallet:
                _total_loss = wallet.balance / _investment_into_wallet * 100
                _loss_money = _total_loss /100 * _investment_into_wallet
                print(f'\n BETTER LUCK NEXT TIME , You had a loss of {_total_loss} which is around {_loss_money}')
            else:
                print('')

     except Exception as e:
         print(f'[-] ERROR OCCURRED: {e}')
