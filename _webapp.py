from flask import Flask, render_template
import random
import webbrowser
import time
import clpsLIB as _smps

app = Flask(__name__)
_market = _smps.cryptocoinMarket()
# Generating a list of one hundred random numbers
_randum_prices = [random.randint(-4250, 99000) for _ in range(9999)]

class cryptocoinMarket:
    cryptocoin_prices = {  # Define cryptocoin_prices as a class attribute
    "Bitcoin": random.choice(_randum_prices),       # Updated price for Bitcoin
    "Ethereum": random.choice(_randum_prices),      # Updated price for Ethereum
    "Binance Coin": random.choice(_randum_prices),  # Updated price for Binance Coin
    "Solana": random.choice(_randum_prices),        # Updated price for Solana
    "Cardano": random.choice(_randum_prices),       # Updated price for Cardano
    "XRP": random.choice(_randum_prices),           # Updated price for XRP
    "Polkadot": random.choice(_randum_prices),      # Updated price for Polkadot
    "Dogecoin": random.choice(_randum_prices),      # Updated price for Dogecoin
    "Avalanche": random.choice(_randum_prices),     # Updated price for Avalanche
    }

    # Other methods...


@app.route('/')
def index():
                 _tlL  = 19999
                 _change_ratio = 25
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
                 crypto_data = _chart_data
                 return render_template('index.html', crypto_data=crypto_data)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
