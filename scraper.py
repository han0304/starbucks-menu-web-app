import requests
from bs4 import BeautifulSoup

from database import insert_drinks


URL = "https://www.starbucks.com.tw/products/drinks/view.jspx?catId=1"


def scrape_drinks():
    """從 Starbucks 台灣網站取得熱濃縮咖啡飲品"""

    drinks = []

    try:
        response = requests.get(
            URL,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("article")

        for article in articles:
            heading = article.find("h2")

            if heading is None:
                continue

            if heading.get_text(strip=True) == "熱濃縮咖啡飲料":
                drink_items = article.find("ul")

                if drink_items is None:
                    continue

                for item in drink_items.find_all("li"):
                    title_cn = item.find("h1", class_="title_cn")
                    title_en = item.find("h3", class_="title_en")

                    if title_cn and title_en:
                        drinks.append((
                            title_cn.get_text(strip=True),
                            title_en.get_text(strip=True)
                        ))

        return drinks

    except requests.exceptions.RequestException as error:
        print(f"無法取得網頁內容：{error}")

    return []


def main():
    drinks = scrape_drinks()

    if not drinks:
        print("沒有取得飲品資料，請檢查網站或網頁結構。")
        return

    insert_drinks(drinks)

    print(f"成功取得 {len(drinks)} 筆飲品資料！")
    print("資料已寫入 SQLite 資料庫。")


if __name__ == "__main__":
    main()
