from flask import Flask, render_template
from database import init_db, get_all_drinks

app = Flask(__name__)


@app.route("/")
def index():
    # 確保資料表已建立
    init_db()

    # 從資料庫取得所有飲品
    drinks = get_all_drinks()

    # 將飲品資料傳送給 HTML
    return render_template("index.html", drinks=drinks)


if __name__ == "__main__":
    app.run(debug=True)
