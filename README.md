*** 以YOLOv3識別肺炎X光圖片

**** (訓練與測試資料已移除)
此YOLOv3採用darknet架構，需預先載入。
** 訓練與測試的圖檔路徑
*** 訓練:

`/1/train/`

*** 測試:

`/1/val/`

1.進入/darknet 路徑
2.訓練模型:

`./darknet detector train cfg/cat_and_dog.data cfg/cat_and_dog_yolov3.cfg backup/cat_and_dog_yolov3_final.weights`

需要標示圖片目錄於 : `/1/train/train.list`

3.測試單張圖片:

`./darknet detector test cfg/cat_and_dog.data cfg/cat_and_dog_yolov3.cfg backup/cat_and_dog_yolov3_final.weights /home/kuo4567654/1/val/LLL009801.png`

(圖片可以任意改成其他)

需要標示圖片目錄於: `/1/val/val.list`

4.模型評估:

`./darknet detector recall cfg/cat_and_dog.data cfg/cat_and_dog_yolov3.cfg backup/cat_and_dog_yolov3_final.weights`

需要標示圖片目錄於: `/1/val/val.list`

(本次使用140筆測試資料)
