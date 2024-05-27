import feedparser

html_front_string = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body {
            width: 100vw;
            box-sizing: border-box;
            font-family: 'Tahoma', sans-serif;
        }

        header {
            text-align: center;
        }

        header > h1 {
            font-size: 2rem;
            color: #333;
        }

        .navbar {
            padding: 0 8rem;
        }

        .navbar-table {
            display: table;
            width: 100%;
        }

        .navbar-table > tr {
            display: table-row;
            width: 100%;
        }

        .navbar-table > tr > td {
            text-align: center;
        }

        .news {
            padding: 0 20rem;
        }

        .news-item {
            width: 100%;
            border: 1px solid #ccc;
            overflow: auto;
            margin-bottom: 1rem;
        }
    </style>
</head>
<body>
<header>
    <h1>markstanl news</h1>
    <h2>news that I think is cool</h2>
</header>
<nav class="navbar">
    <table class="navbar-table">
        <tr>
            <td><a href="https://github.com/markstanl/google-news-rss-feed">github</a></td>
            <td><a href="https://www.linkedin.com/in/markstanl/">linkedin</a></td>
        </tr>
    </table>
</nav>
<main style="width: 100%;">
    <section class="news"> """

html_back_string = """
    </section>
</main>

</body>
</html>"""


def parse_feed(url: str) -> feedparser.FeedParserDict:
    """
    Parses the RSS feed from the given URL into a feedparser object
    :param url: the rss url to be parsed
    :return: the parsed feed
    """
    return feedparser.parse(url)


def generate_html(feed_to_html: feedparser.FeedParserDict) -> str:
    """
    Generates the HTML code to be sent to a user using the template string from the outer definition
    :param feed_to_html: the RSS feed to be converted to HTML
    :return: a string representation of the HTML code
    """
    html = html_front_string
    for entry in feed_to_html.entries:
        if 'summary' not in entry:
            entry.summary = ""
        html += f"""<div class="news-item">
            <h3>{entry.title}</h3>
            <p>
                {entry.summary}
            </p>
            <a href="{entry.link}">Read More</a>
        </div>"""
    html += html_back_string
    return html


def generate_file(html_contents: str, file_name: str):
    """
    Writes the string representation of the HTML code to a file in the src/html_contents directory
    :param html_contents: the string representation of the HTML code
    :param file_name: the name of the file to be written to
    :return: none
    """
    file_name = "./src/html_contents/" + file_name
    with open(file_name, 'w') as file:
        file.write(html_contents)


if __name__ == '__main__':
    feed = parse_feed('http://rss.cnn.com/rss/edition.rss')
    html_content = generate_html(feed)
    generate_file(html_content, 'index.html')

