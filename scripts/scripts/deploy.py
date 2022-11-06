from brownie import accounts, config, network, ERC721Test


def deploy_ERC721Test():
    ## use this on testnbet
    account = accounts.load("eventmask")  # use your own account id
    print("Made from:{}".format(account))

    # account = get_account

    contra_of_ERC721Test = ERC721Test.deploy(
        {"from": account}
    )  # make sure to add from if it's transaction, not a call
    print("contact address:{}".format(contra_of_ERC721Test))


def main():
    deploy_ERC721Test()
