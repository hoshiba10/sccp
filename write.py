#-*- coding: utf-8 -*-
from datetime import datetime

out = open("result.csv", "a")     # result.txtファイルを書き込みモード("w")で作成し、foutという変数に入れる

out.writelines(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ",")
out.writelines("TEST=firstWrite" + ",") # writelineメソッドを使って文字列を書き込む
out.writelines("TEST1=secondWrite\n")

out.close()                       # 開いたファイルを閉じる