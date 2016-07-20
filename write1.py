#-*- coding: utf-8 -*-

out = open("result.txt", "w")     # result.txtファイルを書き込みモード("w")で作成し、foutという変数に入れる

out.writelines("TEST=firstWrite\n") # writelineメソッドを使って文字列を書き込む
out.writelines("TEST1=secondWrite")

out.close()                       # 開いたファイルを閉じる