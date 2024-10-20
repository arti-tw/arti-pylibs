import base64
from io import BytesIO
from pathlib import Path
from typing import Any, Union

from PIL import Image


def validate_image_extension(image_path: str):
    if not (
        image_path.endswith(".png")
        or image_path.endswith(".jpg")
        or image_path.endswith(".jpeg")
    ):
        raise ValueError("Only PNG and JPG/JPEG images are supported.")


def image_path_to_base64(image: str):
    with open(image, "rb") as f:
        image_data = f.read()
    return base64.b64encode(image_data).decode("utf-8")


def pil_image_to_base64(image: Image.Image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()
    return base64.b64encode(img_bytes).decode("utf-8")


def base64_to_pil_image(base64_string: str):
    if base64_string.startswith("data:image"):
        base64_string = base64_string.split("base64,")[-1]
    image_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(image_data))


def image_to_base64(image: Union[str, Image.Image, Path, Any]) -> str:
    if isinstance(image, Path):
        image = str(image)

    if isinstance(image, str):
        image = image.strip()

        if image.startswith("data:image"):
            image = image.split("base64,")[-1]

        # file path
        if "." in image:
            validate_image_extension(image)
            return image_path_to_base64(image)
        # base64
        else:
            return image

    if isinstance(image, Image.Image):
        return pil_image_to_base64(image)

    raise ValueError("Invalid image type.")
