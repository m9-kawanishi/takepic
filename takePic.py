import os
# opencvをインポートする前にこの処理を加えると起動が早くなる
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import time
import beep
import sys


# 変数設定
FOLDER_NAME = "./test/" # 保存先ディレクトリ
FILE_NAME = "test_" # ファイル名（共通）
EXTENSION = ".jpg"
SLEEP_SEC = 3 # 撮影間隔[sec]
SHOW_WIN_SCALE = 0.5 # 表示ウィンドウの倍率

counter = 0 # ファイル名（番号）

# カメラの設定（引数：デバイスID）
cap = cv2.VideoCapture(0)

# 初期設定画面
counter = int(input("Please input first file no: "))
cmd = input("Are you sure start process? (y/n): ")
print("\n")
print("When you quit process, please put control+c", file=sys.stderr)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160) 

cv2.namedWindow("camera", cv2.WINDOW_NORMAL)

# フォルダがなかったら作成
os.makedirs(FOLDER_NAME, exist_ok=True)

# 繰り返し処理
while cmd == "y":

    try:

        # ファイル名生成
        fileName = FOLDER_NAME + FILE_NAME + str(counter) + EXTENSION

        # カメラ画像取得
        ret, frame = cap.read()
        time.sleep(0.1)

        # 画像保存
        cv2.imwrite(fileName, frame)

        # 表示用に画像サイズを変更
        edt_h = int(frame.shape[0]*SHOW_WIN_SCALE)
        edt_w = int(frame.shape[1]*SHOW_WIN_SCALE)
        cv2.resizeWindow("camera", edt_w, edt_h) 

        # カメラ画像出力
        cv2.imshow('camera', frame)
        
        # 画像保存が完了したらビープ音を鳴らす
        beep.beepOn(1500, 500)
        print(fileName + " was saved", file=sys.stderr)
        
        # 一定時間停止
        time.sleep(SLEEP_SEC)

        counter += 1

    # control+cが入力されたら処理を終了
    except KeyboardInterrupt:
        print("receive control+c\n")
        cmd = "n"

# メモリ解放
cap.release()
cv2.destroyAllWindows()

print("Finish process")