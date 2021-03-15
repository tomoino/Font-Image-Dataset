# Font-Image-Dataset
Create a data set of character images from fonts.

## Installation
```bash
$ git clone git@github.com:tomoino/Font-Image-Dataset.git
```

## Usage
1. Set up the environment.
    ```bash
    $ cd Japanese-Font-Dataset
    $ sh docker/build.sh
    $ sh docker/run.sh
    $ sh docker/exec.sh
    ```
1. Put the font files (.ttf or .otf) in "./fonts".
1. Put the characters you want to make into an image into "./dataset/characters.txt".
1. Run main.py.
    ```bash
    python main.py \
        --charfile ./dataset/characters.txt \
        --fontsdir ./fonts \
        --labelfile ./dataset/label.csv \
        --savedir ./dataset/images \
        --fontsize 26 \
        --imagesize 32
    ```
