from brownie import FundMe, accounts, MockV3Aggregator, config, network
from scripts.helpful_scripts import (
    getAccount,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)
from web3 import Web3


def deploy_found_me():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        # price feed falso
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    account = getAccount()
    found_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"Contract deployed to {found_me}")
    return found_me


def main():
    deploy_found_me()
