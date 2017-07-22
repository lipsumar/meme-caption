# Meme caption generator

> Add text captions (top and bottom) to images using command line

Bog post: <http://blog.lipsumarium.com/caption-memes-in-python/>

## Install

1. Clone this repository
2. `cd` into the repo directory
3. Run `python meme.py images/Success-Kid.jpg "Top text here" "Bottom text here" out.jpg`

This should create a `out.jpg` image with your caption.

## Usage

```bash
python meme.py <imageFilePath> "<topCaption>" "<bottomCaption>" <outputFile>
```

Example:

```bash
python meme.py images/i-dont-always.jpg "i don't always make memes" "but when i do I use python" out.jpg
```

![example result](http://blog.lipsumarium.com/assets/img/posts/2017-07-22-caption-memes-in-python/out.jpg)
