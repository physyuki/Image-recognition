import facerecog_main as fm
import json
import pandas as pd
import sys

if __name__ == '__main__':
    #=====人物の候補を探す=====
    filename = sys.argv[1]
    with open(filename, 'rb') as f:
        binary = f.read()
    response = fm.detectFaceBylocal(binary)
    data = json.loads(response.text)
    faceId = data[0]['faceId']

    #=====人物を特定=====
    response = fm.identify(faceId)
    data = json.loads(response.text)
    candidates = data[0]['candidates']
    pId = candidates[0]['personId']
    conf = candidates[0]['confidence']
    df = pd.read_csv("player_info.csv", index_col=0)
    index = df[df.personId == pId].index[0]
    identifiedname = df.loc[index, 'name']
    print("候補:{}, 信頼度:{}".format(identifiedname, conf))
