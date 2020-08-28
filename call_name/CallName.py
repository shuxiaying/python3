# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: name
# Author: TangJianjun
# Date: 2020/7/9
# Description:
# -----------------------------------------------------------------------------------
import datetime
import os
import random
import tkinter as tk
try:
    import pyttsx3
except:
    os.system('configuration.bat')  # 更新pip，安装pyttsx3
    try:
        import pyttsx3
    except:
        os.system('echo Something error, please check the proxy.')
    finally:
        pass
finally:
    pass


from call_name.config import CallNameDriver


class ForGUI:

    def __init__(self):
        # 引入pyttsx3库，实现语音播报
        try:
            self.eng = pyttsx3.init()
        except:
            os.system('echo can not start the function of speech.')
        finally:
            pass
        try:
            self.cname = CallNameDriver()
        except:
            msg["text"] = "未找到花名册"
            msg.update()
        else:
            try:
                record = self.cname.read_record()  # 读取记录
            except:
                self.cname.mk_record()  # 读取异常则重新创建记录
                record = self.cname.read_record()
            self.re_date = record["date"]  # 获取使用日期记录
            # 每5天初始化一次记录
            if len(self.re_date) > 5:
                self.cname.mk_record()  # 重新创建记录
            else:
                # 判断花名册是否有修改
                keys_list = self.cname.get_keys()
                try:
                    assert keys_list == self.cname.namelist
                except:
                    keys = set(keys_list)
                    names = set(self.cname.namelist)
                    new_add = names - keys  # 获取新增
                    new_del = keys - names  # 获取移除
                    if new_add:
                        self.cname.re_mod(new_add=new_add)
                    if new_del:
                        self.cname.re_mod(new_del=new_del)

    # 开始点名，输出有效姓名：姓名对应记录不为最大次数
    def start(self):
        bt["state"] = 'disable'  # 禁止重复点击
        times = self.cname.re_times()  # 获取记录次数
        max_times = max(times)  # 获取记录最大次数
        min_times = min(times)  # 获取记录最小次数
        td = str(datetime.datetime.today().date())  # 获取当前日期
        if not td in self.re_date:
            self.cname.re_mod(re_date=td)
        while True:
            name = self.cname.call_name()  # 产生随机姓名
            times = self.cname.call_times(name)  # 获取被点到成员记录次数
            if max_times != min_times:
                if times != max_times:
                    self.cname.re_mod(name=name)  # 修改记录
                    msg["text"] = name
                    msg.update()
                    try:
                        if sp_bt["text"] == "语音播报开":
                            self.eng.say(name)
                            self.eng.runAndWait()
                            self.eng.stop()
                    except:
                        pass
                    break
            else:
                self.cname.re_mod(name=name)  # 修改记录
                msg["text"] = name
                try:
                    if sp_bt["text"] == "语音播报开":
                        self.eng.say(name)
                        self.eng.runAndWait()
                        self.eng.stop()
                except:
                    pass
                break
        bt["state"] = 'normal'  # 恢复点击

    # 查看花名册
    def open_name_excel(self):
        try:
            os.system("start %s&exit" % self.cname.excel_file_path)
        except:
            msg["text"] = '\n未找到花名册╮(╯▽╰)╭\n'
            msg["font"] = ('', 18)
            msg.update()

    # 查看点名记录
    def open_record(self):
        try:
            os.system("start %s&exit" % self.cname.file_path)
        except:
            msg["text"] = '\n未找到点名记录╮(╯▽╰)╭\n'
            msg["font"] = ('', 18)
            msg.update()

    def sp_unchecked(self):
        sp_bt["command"] = self.sp_checked
        sp_bt["text"] = "语音播报关"
        sp_bt.update()

    def sp_checked(self):
        sp_bt["command"] = self.sp_unchecked
        sp_bt["text"] = "语音播报开"
        sp_bt.update()

    # 随机显示花名册名单
    def info(self):
        name_list = self.cname.namelist
        name = random.choice(name_list)
        msg["font"] = ('', 44)
        msg["text"] = (name)
        msg.update()

    def bt_listen(self):
        while bt["state"] == 'normal':
            bt['text'] = "就决定是你了"
            bt['command'] = self.bt_start
            bt.update()
            root.after(500, func=self.info)
            continue

    def bt_start(self):
        bt['command'] = self.bt_listen
        bt['text'] = "开始"
        bt.update()
        fg = ForGUI()
        root.after(500, fg.start)

if __name__ == '__main__':
    # 创建窗口
    root = tk.Tk(className="点名工具")
    # 设置窗口大小
    setWidth = 300
    setHeight = 200
    # 获取屏幕分辨率
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    x = int((screenWidth - setWidth) / 2)
    y = int((screenHeight - setHeight) / 2)
    # 设置窗口初始位置屏幕居中
    root.geometry("%sx%s+%s+%s" % (setWidth, setHeight, x, y))
    # 设置窗口宽高固定
    root.resizable(0, 0)
    # 创建菜单栏
    m1 = tk.Menu(root, tearoff=False)
    # 创建子菜单，不显示分窗
    MenuBar = tk.Menu(m1, tearoff=False)
    MenuBar.add_command(label='查看名单', command=ForGUI().open_name_excel)
    MenuBar.add_command(label='查看记录', command=ForGUI().open_record)
    MenuBar.add_command(label='清空记录', command=CallNameDriver().mk_record)

    # 将子菜单加入菜单栏中
    m1.add_cascade(label='选项', menu=MenuBar)
    m1.add_command(label='Exit', command=root.quit)
    # 将菜单栏添加到窗口
    root.config(menu=m1)

    f_sp = tk.Frame(root, width=300)
    f_sp.pack(pady=2)
    # 创建语音播报开关
    sp_bt = tk.Checkbutton(f_sp, text="语音播报关", font=('', 10), justify="right", command=ForGUI().sp_checked)
    sp_bt.pack()

    f1 = tk.Frame(root, bd=1, height=150, width=300)
    f1.pack(pady=6)
    # 创建文本显示
    msg = tk.Label(f1, text="\n别紧张(●ˇ∀ˇ●)\n",font=('', 18), fg="green")  # 创建文本控件
    msg.pack(pady=8)

    f2 = tk.Frame(root)
    f2.pack()
    # 创建开始按钮
    bt = tk.Button(f2, text='开始点名喽', stat="normal", command=ForGUI().bt_listen, bd=4, width=20, font=18)
    bt.pack(pady=6)

    root.mainloop()
