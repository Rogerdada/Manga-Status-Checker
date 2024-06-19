import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 定义一个函数来检查漫画更新
def check_update(url, manga_name, manga_link):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # 你需要检查HTML结构以确保你使用了正确的类名和标签
    updates = soup.find_all("div", class_="cont-list")

    for update in updates:
        # 假设更新的信息如你截图中所示
        title = update.find('dt', text='更新至：').find_next_sibling('dd').text
        date = update.find('dt', text='更新于：').find_next_sibling('dd').text
        date_now = datetime.strptime(date, "%Y-%m-%d")
        now =datetime.now()
        one_week_ago = now - timedelta(days=7)
        if one_week_ago <= date_now <= now:
            print(f'\033[93m{manga_name}: {title}, 更新日期: {date}, 連結: {manga_link}\033[0m')
        else:
            print(f'{manga_name}: {title}, 更新日期: {date}')
# 定义两个漫画的URL和名字
mangas = [
    {'url': 'https://m.manhuagui.com/comic/23766/', 'name': '勇者系列','Link': 'https://m.manhuagui.com/comic/23766/'},
    {'url': 'https://m.manhuagui.com/comic/36859/', 'name': '怪獸8號','Link': 'https://m.manhuagui.com/comic/36859/'},
    {'url': 'https://m.manhuagui.com/comic/1128/', 'name': '航海王','Link': 'https://m.manhuagui.com/comic/1128/'},
    {'url': 'https://m.manhuagui.com/comic/31317/', 'name': '大黑暗','Link': 'https://m.manhuagui.com/comic/31317/'},
    {'url': 'https://m.manhuagui.com/comic/31550/', 'name': '間諜家家酒','Link': 'https://m.manhuagui.com/comic/31550/'},
    {'url': 'https://m.manhuagui.com/comic/38431/', 'name': '坂本Days','Link': 'https://m.manhuagui.com/comic/38431/'},
    {'url': 'https://m.manhuagui.com/comic/30782/', 'name': '拳願奧米茄','Link': 'https://m.manhuagui.com/comic/30782/'},
    {'url': 'https://m.manhuagui.com/comic/35937/', 'name': '葬送的芙莉蓮','Link': 'https://m.manhuagui.com/comic/35937/'}
]

# 遍历漫画列表，检查每部漫画的更新
for manga in mangas:
    check_update(manga['url'], manga['name'], manga['Link'])


input("Press Enter to exit...")