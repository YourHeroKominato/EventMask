import qrcode


# def Qr_generator(user_display_name, sent_from_channel_name, user_address):
#     img = qrcode.make(
#         "https://globalhouseteam-web3.bubbleapps.io/{}/{}/{}".format(
#             user_display_name, sent_from_channel_name, user_address
#         )
#     )
#     img.save("./image/output/some_file.jpg")


def Qr_generator(user_display_name, sent_from_channel_name, user_address):
    img = qrcode.make(
        "https://globalhouseteam-web3.bubbleapps.io?discord_account_name={}&discord_event_name={}&discord_account_wallet={}".format(
            user_display_name, sent_from_channel_name, user_address
        )
    )
    img.save("./image/output/some_file.jpg")
