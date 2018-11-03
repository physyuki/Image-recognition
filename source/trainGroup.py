import facerecog_main as fm

if __name__ == '__main__':
    #=====人物の顔画像を学習=====
    response = fm.trainGroup()
    print(response)
