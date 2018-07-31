#!/usr/bin/python3
#coding: utf-8
#-------------------------------------------------------------------------------------
# DivideImage ver1.0.0  2018.08.01
#
# Linux Mint 18.1 - Python 2.7.12 - /usr/bin/python  - utf-8 / LF 
# Linux Mint 18.1 - Python 3.5.2  - /usr/bin/python3 - utf-8 / LF 
#-------------------------------------------------------------------------------------
import tkinter
import tkinter.filedialog
from pathlib import Path
from pathlib import PurePath
from PIL import Image, ImageFilter


class Application(tkinter.Frame):

    #----------------------------------------------------------------
    # 初期化。
    #
    #----------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title('画像分割')
        w = 640
        h = 240
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        self.entry10000_text  = tkinter.StringVar() #ファイルパス
        self.entry10001_text  = tkinter.StringVar() #チップの幅
        self.entry10001_text.set('{0:d}'.format(48))
        self.entry10002_text  = tkinter.StringVar() #チップの高さ
        self.entry10002_text.set('{0:d}'.format(48))
        self.master.geometry("%dx%d+%d+%d" % (w, h, (sw - w) / 2, (sh - h) / 2))
        self.create_widgets()


    #----------------------------------------------------------------
    # ウィジェットの作成。
    #
    #----------------------------------------------------------------
    def create_widgets(self):
        panel10000 = tkinter.Frame(self.master)
        panel11000 = tkinter.Frame(self.master)
        label10000 = tkinter.Label(panel11000, text='画像ファイル')
        label10000.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=16)
        panel11000.pack(side=tkinter.TOP, anchor=tkinter.NW, pady=8)
        panel12000 = tkinter.Frame(self.master)
        entry10000 = tkinter.Entry(panel12000, width=64, textvariable = self.entry10000_text, bg='white')
        entry10000.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=16)
        butto10000 = tkinter.Button(panel12000, text='…')
        butto10000.configure(command = self.select)
        butto10000.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=8)
        panel12000.pack(side=tkinter.TOP, anchor=tkinter.NW, pady=8)
        panel13000 = tkinter.Frame(self.master)
        label10001 = tkinter.Label(panel13000, text='width')
        label10001.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=16)
        entry10001 = tkinter.Entry(panel13000, textvariable = self.entry10001_text, bg='white')
        entry10001.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=8)
        label10002 = tkinter.Label(panel13000, text='height')
        label10002.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=16)
        entry10002 = tkinter.Entry(panel13000, textvariable = self.entry10002_text, bg='white')
        entry10002.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=8)
        panel13000.pack(side=tkinter.TOP, anchor=tkinter.NW, pady=8)
        panel14000 = tkinter.Frame(self.master)
        butto10001 = tkinter.Button(panel14000, text='出力')
        butto10001.configure(command = self.export)
        butto10001.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=16)
        panel14000.pack(side=tkinter.TOP, anchor=tkinter.NW, pady=32)
        panel10000.pack(side=tkinter.TOP, anchor=tkinter.NW, pady=8)


    #----------------------------------------------------------------
    # 選択ボタンが押された時の処理。
    #
    #----------------------------------------------------------------
    def select(self):
        #ファイルダイアログを開く
        ft = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))
        fp = tkinter.filedialog.askopenfilename(filetypes = ft)
        if len(fp) > 0:
            self.entry10000_text.set(fp)


    #----------------------------------------------------------------
    # 出力ボタンが押された時の処理。
    #
    #----------------------------------------------------------------
    def export(self):
        #チップの幅と高さを得る
        cw = self.to_int(self.entry10001_text.get())
        if cw is None:
            cw = 48
            self.entry10001_text.set('{0:d}'.format(48))
        ch = self.to_int(self.entry10002_text.get())
        if ch is None:
            ch = 48
            self.entry10002_text.set('{0:d}'.format(48))
        #元ファイルのパス
        pp = PurePath(self.entry10000_text.get())
        #出力
        img = Image.open(self.entry10000_text.get())
        for i in range(img.height // ch):
            for j in range(img.width // cw):
                pt = pp.with_name(pp.stem + '_y{:02d}'.format(i) + 'x{:02d}'.format(j) + pp.suffix)
                box = (j * cw, i * ch, j * cw + cw, i * ch + ch)
                reg = img.crop(box)
                reg.save(str(pt), quality=75)
        img.close()


    #----------------------------------------------------------------
    # 文字列を int 値に変換する。
    # 文字列が有効でない場合は None を返す。
    #
    #----------------------------------------------------------------
    def to_int(self, str):
        val = None
        b = self.is_int_expression(str)
        if b is True:
            val = int(str)
        return val


    #----------------------------------------------------------------
    # 文字列が int 値に変換可能な場合はTrueを返す。
    #
    #----------------------------------------------------------------
    def is_int_expression(self, str = ''):
        try:
            val = int(str)
            return True
        except ValueError:
            return False



root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
