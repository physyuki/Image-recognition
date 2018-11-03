from selenium import webdriver
import pandas

driver = webdriver.Chrome()
df = pandas.DataFrame()

#CSS SELECTORの設定
PLAYER_LIST = ".list3"
POSITION = "a"
PLAYER_NAME = ".name_large"
ROMANAME = "dd" #FACE API用のローマ字
IMAGE = "img"

#スクレイピング実行
driver.get("https://m.hanshintigers.jp/data/player_list/2018/")
all_plist = driver.find_elements_by_css_selector(PLAYER_LIST)
for position in all_plist:
    try:
        players = position.find_elements_by_css_selector(POSITION)
        for player in players:
            name = player.find_element_by_css_selector(PLAYER_NAME).text
            print(name)

            thumnailURL = player.find_element_by_css_selector(IMAGE).get_attribute("src")
            print(thumnailURL)

            roma = player.find_element_by_css_selector(ROMANAME).text
            roma = roma.split("\n")[1]
            print(roma)

            se = pandas.Series([name, roma, thumnailURL],["name", "roma", "image"])
            df = df.append(se, ignore_index=True)
    except Exception as e:
        print(e)

print("Finished Scraping. Writing CSV.......")
df.to_csv("player.csv")
print("DONE")
driver.close()
