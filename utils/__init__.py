# -*- coding: utf-8 -*-
"""Util functions"""

import glob
import csv

from utils.font import Font


def load_fonts(fontsdir: str) -> list:
    """Load fonts
    
    Loads all fonts in fontsdir, and returns list of Font object.

    Returns:
        List of Font object.

    """

    fonts: list = []

    files = glob.glob(f"{fontsdir}/*")
    for file in files:
        fonts.append(Font(file))

    return fonts

def load_chars(charfile: str) -> list:
    """Load characters
    
    Loads all characters in charfile, and returns list of characters.

    Returns:
        List of characters.

    """

    f = open(charfile, 'r')
    chars: list = f.read().splitlines()

    return chars

def save_label(label: list, labelfile: str) -> None:
    """Save label

    Saves set of image name and label to csv.

    Args:
        label: List of set of image name and label.
        labelfile: Path of label file.

    """

    with open(labelfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(label)
    