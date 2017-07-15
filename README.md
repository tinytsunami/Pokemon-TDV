# Pokemon-TDV
統計整理寶可夢能力。自動計算三防數值並統整起來。

## 目錄
* [內容](#內容)
* [資料](#資料)

## 內容
在 main.py 中：
1. 自動計算三防數值
2. 檢查寶可夢的雙防較低者，為挑選性格
3. 計算最佳三防數值（TDV）
4. 建立整體的資料庫

在 evolution.py 中：
1. 自動分辨是否可以使用進化輝石（しんかのきせき）

※ 資料庫使用了 Splite3

## 資料
所有的附屬資料皆在 data/ 目錄下：

|名稱|內容|
|:-:|:-:|
|database.db|建立出來的總資料。觀看請使用 [SQLite DB Browser](http://sqlitebrowser.org/)|
|pokemon.sql|從 database.db 導出的寶可夢能力資料|
|tdv_data.sql|從 database.db 導出的寶可夢三防數值資料|
|ultimate_pokemon.csv|彙整最終進化型的列表資料|
