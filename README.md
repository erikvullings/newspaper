# Extracting news articles with Newspaper 

Extract a list of news articles using newspaper4k and saves the URL, title, text, top image URL, and publication date to a JSON array.

## Installation pre-requirements on Ubuntu

```bash
sudo apt-get install python3 python3-dev
sudo apt-get install python3-pip
sudo apt-get install libxml2-dev libxslt-dev
sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev
```

NOTE: If you find problem installing `libpng12-dev`, try installing `libpng-dev`.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Run

Use `-f` to specify the output file, followed by a list or URLs to process.

```bash
python3 get_articles.py -f articles.json \
  https://www.example1.com \ 
  https://www.example2.com
```
