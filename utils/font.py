# -*- coding: utf-8 -*-
"""Font Class"""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


class Font:
    """Font class

    Attributes:
        name (str): Name of font.
        path (str): Path of font.
        label (list): List of set of image name and label.
            example: [("a.png", "a"), ...]

    """

    def __init__(self, path: str) -> None:
        """Initialization

        Args:
            path: Path of font.

        """

        self.path = path
        self.name = os.path.splitext(os.path.basename(path))[0]
        self.label = []

    def generate_images(self, chars: list, fontsize: int, imagesize: int, savedir: str):
        """Generate images

        Generates and saves images.

        Args:
            chars: List of characters to generate.
            size: Size of font.
            savedir: Path of directory to save images.

        """

        savedir = Path(savedir)
        image_font = ImageFont.truetype(font = self.path, size = fontsize)
        
        images: list = []
        image_w, image_h = (imagesize, imagesize)

        for char in chars:
            image = Image.new('L', (image_w, image_h), 255)
            draw = ImageDraw.Draw(image)
            draw.font = image_font
            char_w, char_h = draw.textsize(char)
            draw.text(((image_w-char_w)/2,(image_h-char_h)/2), char, fill=0)

            image_name = f"{self.name}_{char}.png"
            if not os.path.exists(f"{savedir}/{char}"):
                os.mkdir(f"{savedir}/{char}")
            image_path = f"{savedir}/{char}/{image_name}"
            image.save(image_path)
            # self.label.append((image_name, char))

        

