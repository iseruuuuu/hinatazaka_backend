from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

BLOG_URL = "https://www.hinatazaka46.com/s/official/diary/member/list"

@app.route("/latest")  # この行を更新
def get_latest_blog():
    response = requests.get(BLOG_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    latest_blog = soup.find("div", class_="c-blog-article__title")
    title = latest_blog.text.strip()
    return jsonify(title=title)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  

