from tkinter import *
from tkinter.ttk import *
import s_button
import s_entry
import tooltip, configer, check
from tkinter import messagebox
import os
from s_toplevel import *


class SetConfig(object):

    def __init__(self, root, config):
        self.root = root
        self.config = config
        self.top = STopLevel(self.root, 400, 130, "设置参数").toplevel

        self.choose_python_path_entry = None
        self.choose_obabel_path_entry = None

        self.choose_python()
        self.choose_obabel()
        self.yesorno()

    def choose_python(self):
        y = 10  # python路径
        choose_python_path = s_button.SButton(self.top,
                                              text="选择ADT的python路径",
                                              x=10, y=y)
        tooltip.create_tooltip(choose_python_path.button, "必须选择mgltools目录里面的python.exe文件！\n"
                                                          "比如：\nC:/mgltools/python.exe")
        self.choose_python_path_entry = s_entry.SEntry(root=self.top,
                                                       textvariable=StringVar(),
                                                       text=configer.Configer.get_para("python_path"),
                                                       x=150, y=y + 4, width=230)
        tooltip.create_tooltip(self.choose_python_path_entry.entry, "ADT的python路径")
        choose_python_path.bind_open_file(entry_text=self.choose_python_path_entry.textvariable,
                                          title="选择ADT中的python.exe",
                                          file_type="exe", parent=self.top)

    def choose_obabel(self):
        y = 50  # python路径
        choose_obabel_path = s_button.SButton(self.top,
                                              text="选择obabel.exe的路径",
                                              x=10, y=y)
        tooltip.create_tooltip(choose_obabel_path.button, "选择obabel.exe文件")
        self.choose_obabel_path_entry = s_entry.SEntry(root=self.top,
                                                       textvariable=StringVar(),
                                                       text=configer.Configer.get_para("obabel_path"),
                                                       x=150, y=y + 4, width=230)
        tooltip.create_tooltip(self.choose_obabel_path_entry.entry, "obabel.exe位置")
        choose_obabel_path.bind_open_file(entry_text=self.choose_obabel_path_entry.textvariable,
                                          title="选择obabel.exe",
                                          file_type="exe", parent=self.top)

    def yesorno(self):
        y = 90
        ok_but = Button(self.top, text="确定", command=self.save_para)
        ok_but.place(x=200, y=y)
        cancel_btn = Button(self.top, text="取消", command=self.top.destroy)
        cancel_btn.place(x=300, y=y)

        self.top.protocol("WM_DELETE_WINDOW", self.ask_save_para)

    def save_para(self):
        # 判断路径
        # 检查python
        python_path = self.choose_python_path_entry.textvariable.get()
        if not check.Check.check_python(python_path):
            return

        # 检查obabel
        obabel_path = self.choose_obabel_path_entry.textvariable.get()
        if not check.Check.check_obabel(obabel_path):
            return

        self.config.para_dict["python_path"] = python_path
        self.config.para_dict["obabel_path"] = obabel_path
        # 读取原始的配置文件
        with open(os.path.realpath(sys.argv[0]) + "/../para.txt", "r") as f:
            for line in f.readlines():
                key = line.split("=")[0]
                if key == "python_path" or key == "obabel_path":
                    continue
                try:
                    value = line.split("=")[1]
                except IndexError:
                    value = ""
                self.config.para_dict[key] = value.strip()

        self.config.save_para()
        self.top.destroy()
        messagebox.showinfo("成功", "路径配置成功！")

    def ask_save_para(self):
        if messagebox.askokcancel("退出", "保存参数？"):
            self.save_para()
