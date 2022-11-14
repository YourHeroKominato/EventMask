from brownie import ERC721Test, accounts, config
import json

# mint function
def safeMint():

    account = accounts.load("eventmask")  # use your own account id
    print(account)

    contra_ob_ERC721Test = ERC721Test[-1]
    # 0 means firtst contract, -1 means latest one

    ob_value = contra_ob_ERC721Test.safeMint(
        "to_of_certificate",  # to_of_certificate
        "name_of_certificate",  # name_of_certificate
        "description_of_certificate",  # description_of_certificate
        "token_image_of_certificate",  # token_image_of_certificate
        "attribute_of_certificate",  # attribute_of_certificate
        "0",  # value_of_certificate
        {"from": account},
    )

    print(ob_value)
    show_message = "Minted"
    return show_message


def main():
    safeMint()
