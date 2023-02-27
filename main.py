import io

import requests
from PIL import Image
from PIL.Image import Resampling

cover_offset_y = 253
cover_height = 2012

info_url = "https://service-0wsl5m13-1256946954.cd.apigw.tencentcs.com/release/qndxx"


def main():
    base = Image.open("base.png")
    cover_url = requests.get(info_url).json()["dxx_img"]
    cover = Image.open(io.BytesIO(requests.get(cover_url).content))

    width = base.size[0]

    resized_cover = cover.resize((width, cover_height), Resampling.LANCZOS)

    base.paste(resized_cover, (0, cover_offset_y))
    base.save("output.png")


if __name__ == "__main__":
    main()
