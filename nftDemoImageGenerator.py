from PIL import Image, ImageFont, ImageDraw
import os

##file path
cwd = os.getcwd().replace(os.sep, "/")

# create function
def centered_text_to_image(base_img, text, font_path, font_size, font_color, height):

    draw = ImageDraw.Draw(base_img)

    font = ImageFont.truetype(font_path, font_size)

    # 文字がベース画像からはみ出ないように処理
    if draw.textsize(text, font=font)[0] > base_img.size[0] - 30:
        while draw.textsize(text + "…", font=font)[0] > base_img.size[0] - 30:
            text = text[:-1]
        text = text + "…"

    draw.text(
        ((base_img.size[0] - draw.textsize(text, font=font)[0]) / 2, height),
        text,
        font_color,
        font=font,
    )

    return base_img


def nftDemoImageGenerator(
    event_attendee,
    event_name,
    dao_name,
    event_date,
    base_img_path,
    medium_font_path,
    creepster_font_path,
):

    # line1
    base_img = centered_text_to_image(
        Image.open(base_img_path),
        "This is presented to",
        medium_font_path,
        18,
        (255, 255, 255),
        125,  # middle pixel would be 175
    )

    # line2
    base_img = centered_text_to_image(
        base_img,
        event_attendee,
        creepster_font_path,
        34,
        (255, 255, 255),
        175,  # middle pixel would be 175
    )

    # line3
    base_img = centered_text_to_image(
        base_img,
        "Thank you for coming to {}".format(event_name),
        medium_font_path,
        14,
        (255, 255, 255),
        250,  # middle pixel would be 175
    )

    # line4
    base_img = centered_text_to_image(
        base_img,
        "Presented by {} / {} ".format(dao_name, event_date),
        medium_font_path,
        12,
        (224, 224, 224),
        275,  # middle pixel would be 175
    )

    first_path = os.path.join("./image/output/", event_name)
    os.makedirs(first_path, exist_ok=True)
    base_img.save(os.path.join(os.path.join(first_path, "cop.png")))
