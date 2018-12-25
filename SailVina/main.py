from tkinter import *
from tkinter.ttk import *
from SailVina import configer, s_tab, tooltip
from tkinter import messagebox
from SailVina import s_button
from SailVina import s_entry


class MainWindows(object):

    def __init__(self):
        self.main_window = Tk()
        self.notebook = None

        self.tab1 = None
        self.tab2 = None
        self.tab3 = None
        self.tab4 = None
        self.tab5 = None
        self.tab6 = None
        self.tab7 = None
        self.tab8 = None

        self.top = None

        # 初始化配置存储对象
        self.config = configer.Configer()

        # 标题
        self.main_window.title("SailVina v2.0")

        # 禁用窗口缩放
        self.main_window.resizable(width=False, height=False)

        # 屏幕居中显示
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x = (screen_width / 2) - (620 / 2)
        y = (screen_height / 2) - (380 / 2)
        self.main_window.geometry('%dx%d+%d+%d' % (620, 380, x, y))
        self.__create_notebook()

    def __create_notebook(self):
        self.notebook = Notebook()
        self.tab1 = Frame(self.notebook)
        self.tab2 = Frame(self.notebook)
        self.tab3 = Frame(self.notebook)
        self.tab4 = Frame(self.notebook)
        self.tab5 = Frame(self.notebook)
        self.tab6 = Frame(self.notebook)
        self.tab7 = Frame(self.notebook)
        self.tab8 = Frame(self.notebook)
        self.notebook.add(self.tab3, text="准备受体")
        self.notebook.add(self.tab1, text="准备对接配置")
        self.notebook.add(self.tab2, text="准备配体")
        self.notebook.add(self.tab4, text="分子对接")
        self.notebook.add(self.tab8, text="工具")
        self.notebook.add(self.tab5, text="生成复合物")
        self.notebook.add(self.tab7, text="分析作用力")
        self.notebook.add(self.tab6, text="关于")

        # 默认显示卡
        self.notebook.select(tab_id=0)

        self.notebook.place(x=10, y=10, width=600, height=360)

    def save_para(self):
        if messagebox.askokcancel("退出", "保存参数并退出软件？"):
            tab1.save_para()
            tab2.save_para()
            tab4.save_para()
            tab5.save_para()
            self.config.save_para()
            self.main_window.destroy()

    def set_config(self):
        self.top = Toplevel(self.main_window)
        # 居中显示
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x = (screen_width / 2) - (400 / 2)
        y = (screen_height / 2) - (100 / 2)
        self.top.geometry('%dx%d+%d+%d' % (400, 100, x, y))
        self.top.resizable(width=False, height=False)
        self.top.title("设置参数")
        self.top.attributes('-topmost', True)
        self.top.focus()
        self.top.grab_set()

        # 进行布局
        y = 10
        choose_python_path = s_button.SButton(self.top,
                                              text="选择ADT的python路径",
                                              x=10, y=y)
        tooltip.create_tooltip(choose_python_path.button, "必须选择mgltools目录里面的python.exe文件！\n"
                                                          "比如：\nC:/mgltools/python.exe")
        choose_python_path_entry = s_entry.SEntry(root=self.top,
                                                  textvariable=StringVar(),
                                                  text=configer.Configer.get_para("python_path"),
                                                  x=150, y=y + 4, width=200)
        tooltip.create_tooltip(choose_python_path_entry.entry, "ADT的python路径")
        choose_python_path.bind_open_file(entry_text=choose_python_path_entry.textvariable,
                                          title="选择ADT中的python.exe",
                                          file_type="exe")


if __name__ == '__main__':
    # 创建主窗口对象
    sail_vina = MainWindows()
    # 调用参数对象
    sail_vina.config.first_open()
    # 添加切换卡
    tab1 = s_tab.Tab1(sail_vina.tab1, sail_vina.config)
    tab2 = s_tab.Tab2(sail_vina.tab2, sail_vina.config)
    tab3 = s_tab.Tab3(sail_vina.tab3, sail_vina.config)
    tab4 = s_tab.Tab4(sail_vina.tab4, sail_vina.config)
    tab5 = s_tab.Tab5(sail_vina.tab5, sail_vina.config)
    tab6 = s_tab.Tab6(sail_vina.tab6, sail_vina.config)
    tab7 = s_tab.Tab7(sail_vina.tab7, sail_vina.config)
    tab8 = s_tab.Tab8(sail_vina.tab8, sail_vina.config)

    # 脚本配置
    config_button = Button(sail_vina.main_window, text="脚本配置", command=sail_vina.set_config)
    config_button.place(x=510, y=5, width=80)
    tooltip.create_tooltip(config_button, "设置脚本所需路径")

    # 退出按钮
    exit_button = Button(sail_vina.main_window, text="退出", command=sail_vina.save_para)
    exit_button.place(x=510, y=335, width=80)
    tooltip.create_tooltip(exit_button, "保存参数并退出软件")

    # 退出保存参数
    sail_vina.main_window.protocol("WM_DELETE_WINDOW", sail_vina.save_para)

    # 显示窗体
    sail_vina.main_window.mainloop()
