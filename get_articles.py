import newspaper
import sys
import uuid
import json
import argparse


class Article:
    def __init__(self, title, url, text, image_url, published_at):
        self.id = str(uuid.uuid4())
        self.title = title
        self.url = url
        self.text = text
        self.image_url = image_url
        self.published_at = published_at

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "text": self.text,
            "imageUrl": self.image_url,
            "publishedAt": self.published_at.isoformat() if self.published_at else None,
        }


def fetch_article_as_object(url):
    article = newspaper.Article(url)
    article.download()  # Download the article content
    article.parse()  # Parse the article content

    title = article.title
    text = article.text
    image_url = article.top_image
    pub_date = article.publish_date
    published_at = pub_date if pub_date else None

    # Ensure image_url is properly formatted as a string
    image_url = str(image_url) if image_url else None

    # article.nlp()
    # print(article.keywords)
    # print(article.summary)

    return Article(title, url, text, image_url, published_at)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch articles from URLs and output as JSON."
    )
    parser.add_argument("urls", nargs="+", help="List of URLs to fetch articles from")
    parser.add_argument(
        "-f",
        "--output_file",
        default="articles.json",
        help="Output JSON file name (default: articles.json)",
    )
    args = parser.parse_args()

    urls = args.urls
    articles = []

    for url in urls:
        try:
            article_obj = fetch_article_as_object(url)
            articles.append(article_obj)
        except Exception as e:
            print(f"Error processing {url}: {e}")
            continue

    # Convert articles to JSON format
    json_articles = [article.to_dict() for article in articles]

    output_file = args.output_file
    if output_file:
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(json_articles, f, indent=4, ensure_ascii=False)
            print(f"Articles saved to {output_file}")
        except Exception as e:
            print(f"Error saving to file {output_file}: {e}")
    else:
        print(json.dumps(json_articles, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
