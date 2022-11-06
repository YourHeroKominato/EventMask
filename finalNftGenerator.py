from PIL import Image, ImageFont, ImageDraw
import os

##file path
cwd = os.getcwd().replace(os.sep, "/")

creepster_font_path = ""

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


def nftImageGenerator(
    event_name,
    event_attendee,
    base_img_path,
    creepster_font_path,
    token_Num=0,
):

    # line2
    img = centered_text_to_image(
        Image.open(
            r"path"
        ),
        event_attendee,
        creepster_font_path,
        34,
        (255, 255, 255),
        175,  # middle pixel would be 175
    )

    new_dir_path = os.path.join(
        r"path"
    )
    img.save(
        path".format(
            token_Num
        )
    )


nftImageGenerator(
    "Christmas party",
    "si",
    r"path",
    r"path",
    1,
)
