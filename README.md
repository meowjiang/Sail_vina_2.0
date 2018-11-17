## Sail_vina_2.0
Autodock Vina对接GUI界面

开发中……，已经完成：
1. 准备配置文件
2. 准备配体
3. 批量对接  

下一步计划：  
1. 将openbabel的python模块导入，就不需要安装obabel了
2. 研究plip，就可以自动准备配体了

---
###使用教程
软件的安装：  
解压到需要安装的目录，直接运行内部的main.exe文件即可。  
注意：本软件的解压路径不要包含空格！
  
系统需求：  
- 安装obabel并将obabel.exe放在环境变量中
    1. 安装obabel  
        [64位下载](https://sourceforge.net/projects/openbabel/files/openbabel/2.4.1/OpenBabel-2.4.1.exe/download)
        [32位下载](https://sourceforge.net/projects/openbabel/files/openbabel/2.4.1/OpenBabel-2.4.1-x86.exe/download)
    2. 找到安装目录，将obabel.exe添加到环境变量
  比如C:\OpenBabel-2.4.1\obabel.exe
  则将C:\OpenBabel-2.4.1这个目录添加到环境变量即可。  
  
        - 添加环境变量(win10为例)  
  打开"此电脑"-->鼠标右键"属性"-->左边"高级系统设置"-->下方"环境变量"
  -->下方"系统变量"找到变量名Path-->选中点击"编辑"-->点击"浏览"-->选择C:\OpenBabel-2.4.1-->点击确定即可
    3. 按下"win+r"，输入“cmd"。在命令行输入obabel
 ,如果**没有**出现  
 
 >'obabel'不是内部或外部命令，也不是可运行的程序或批处理文件

 则设置成功
  
- 安装ADT  
[ADT下载](http://mgltools.scripps.edu/downloads/downloads/tars/releases/REL1.5.6/mgltools_win32_1.5.6_Setup.exe)
---
###教程：伊马替尼以及自定义配体和络氨酸激酶对接