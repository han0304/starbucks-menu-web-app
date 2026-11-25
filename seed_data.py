from database import init_db, insert_drinks

# 從原始 Excel 整理出的飲品資料
# 已移除重複項目，保留 10 種飲品
drinks = [
    ("芝麻瑪奇朵", "Sesame Macchiato"),
    ("可可瑪奇朵", "Cocoa Macchiato"),
    ("那堤", "Caffè Latte"),
    ("焦糖瑪奇朵", "Caramel Macchiato"),
    ("摩卡", "Caffè Mocha"),
    ("卡布奇諾", "Cappuccino"),
    ("美式咖啡", "Caffè Americano"),
    ("濃縮咖啡", "Espresso"),
    ("特選馥郁那堤", "Espresso Choice Extra Shot Latte"),
    ("馥列白", "Flat White")
]


def main():
    # 建立資料表
    init_db()

    # 將飲品資料寫入資料庫
    insert_drinks(drinks)

    print(f"成功匯入 {len(drinks)} 種飲品！")


if __name__ == "__main__":
    main()
