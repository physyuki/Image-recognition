import facerecog_main as fm
import pandas as pd
import time
import json

if __name__ == '__main__':
    #=====人物名を登録=====
    skipped_count = 0
    pID_df = pd.DataFrame()
    df = pd.read_csv("player.csv", index_col=0)

    print("人物名の登録を開始します")
    for i, rows in df.iterrows():
        name = rows["roma"]
        try:
            print(name)
            response = fm.makePerson(name)
            time.sleep(3)
            print(response)
            json_dic = json.loads(response.text)
            personId = json_dic['personId']
            print(personId)
        except Exception as e:
            print(e)
            skipped_count +=1
            print("{}をスキップしました:スキップ数:{}".format(name, skipped_count))
            personId = ""

        se = pd.Series([personId], ["personId"])
        pID_df = pID_df.append(se, ignore_index=True)

    df = pd.concat([df, pID_df], axis=1)
    df.to_csv("player_info.csv")
    print("人物名の登録が完了しました")

    #=====人物の顔画像を登録=====
    skipped_count = 0
    pFID_df = pd.DataFrame()
    df = pd.read_csv("player_info.csv", index_col=0)

    print("人物の顔画像登録を開始します")
    for i, rows in df.iterrows():
        name = rows["name"]
        pId = rows["personId"]
        image = rows["image"]

        try:
            print(name)
            r = fm.addFaceToPerson(pId, image)
            print(r)
            json_dic = json.loads(r.text)
            pFId = json_dic['persistedFaceId']
            print(pFId)
            time.sleep(3)
        except Exception as e:
            print(e)
            skipped_count +=1
            print("{}をスキップしました:スキップ数:{}".format(name, skipped_count))
            pFId = ""

        se = pd.Series([pFId], ["persistedFaceId"])
        pFID_df = pFID_df.append(se, ignore_index=True)

    df = pd.concat([df, pFID_df], axis=1)
    df.to_csv("player_info.csv")
    print("人物の顔画像登録が完了しました")
