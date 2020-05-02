import utils
import os
import wx
import wx.adv

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Litorature Cracked',size = wx.Size(1027,465))
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 40, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Submit text')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            self.text_ctrl.Hide()
            png = wx.Image('img/whatever.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
            wordList = utils.extractWithGUI(value)
            with open("input.txt", 'w') as f:
                for word in wordList:
                    f.write(word)
                    f.write("\n")
            if os.path.exists("result.json"):
                os.remove("result.json")
            with open("input.txt", 'r') as f:
                contents = f.readlines()
                wordlist = []
                for line in contents:
                    wordlist.append(line.rstrip())
                words = ",".join(wordlist)
            path = utils.getPath()
            utils.crawl(words)
            utils.process(path)
            png = wx.Image('img/finish.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
