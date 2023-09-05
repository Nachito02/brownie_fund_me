from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 20000000000


def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    # price feed falso
    print(f"the active network is {network.show_active()}")
    print(f"Deploying the mocks")
    MockV3Aggregator.deploy(DECIMALS, Web3.toWei(2000, "ether"), {"from": getAccount()})
    # MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": getAccount()})

    print("Mocks deployed")
