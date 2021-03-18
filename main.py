
# -*- coding: utf-8 -*-
"""Main
For making dataset from Japanese fonts.

Args:
    --charfile (str): The path of list of characters.
    --fontsdir (str): The path of directory of fonts.
    --labelfile (str): The path of label file.
    --savedir (str): The path of directory to save images.
    --fontsize (int): Size of font.
    --imagesize (int): Size of image.

"""

import argparse
import os

from utils import * 
from utils.font import Font


def parser() -> object:
    """Arguments parser

    Returns:
        Arguments.
        
    """

    parser = argparse.ArgumentParser(description='For making dataset from Japanese fonts.')
    parser.add_argument('--charfile', type=str, default='./dataset/characters.txt', help='list of characters')
    parser.add_argument('--fontsdir', type=str, default='./fonts', help='directory of fonts')
    parser.add_argument('--labelfile', type=str, default='./dataset/label.csv', help='label file')
    parser.add_argument('--savedir', type=str, default='./dataset/images', help='directory for images')
    parser.add_argument('--fontsize', type=int, default=26, help='size of font')
    parser.add_argument('--imagesize', type=int, default=32, help='size of image')
    args = parser.parse_args()

    return args


def main(args: object) -> None:
    """Main
    
    Args:
        args: Arguments.
    
    Returns:
        None.

    """

    fonts: list = load_fonts(args.fontsdir)
    chars: list = load_chars(args.charfile)
    
    fontsize: int = args.fontsize
    imagesize: int = args.imagesize
    savedir: str = args.savedir
    label = []

    if not os.path.exists(f"{savedir}"):
        os.mkdir(f"{savedir}")

    for font in fonts:
        font.generate_images(chars=chars, fontsize=fontsize, imagesize=imagesize, savedir=savedir)
        # label += font.label

    # save_label(label=label, labelfile=args.labelfile)


if __name__ == '__main__':
    args = parser()
    main(args)