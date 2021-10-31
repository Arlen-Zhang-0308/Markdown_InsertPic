import wx, pyperclip
from PIL import ImageGrab

img_name = ''

def save_button(e):
    try:
        img_name = inp.GetValue()
        img = ImageGrab.grabclipboard()
        '''图片保存的路径'''
        img.save('F:/In_school/考研/专业课/信号与系统/pics/' + img_name + '.png')
        '''插入的Markdown语句：   ![文件名](pics/文件名.png "文件名")   '''
        content = '![' + img_name + '](pics/' + img_name + '.png \"' + img_name + '\")  \n'
        pyperclip.copy(content)
        pyperclip.paste()
        inp.Clear()
        lab.SetLabel('保存成功。')
    except:
        lab.SetLabel('保存失败。')

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, title='Markdown图片插入辅助', size=(300, 170), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP) # 创建窗口

    inp = wx.TextCtrl(frame, pos=(0,0), size=(283, 50))
    
    but = wx.Button(frame, label='保存图片',pos=(0, 50), size=(283, 50))
    but.Bind(wx.EVT_BUTTON, save_button)

    lab = wx.StaticText(frame, label='提示信息', pos=(20, 105), size=(283, 50))

    frame.Show()
    app.MainLoop()      # 打开主循环。