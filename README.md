## Sail_vina_2.0
Autodock Vina对接GUI界面

开发中……，已经完成：
1. 准备配置文件
2. 准备配体
3. 批量对接
4. 生成配体-蛋白复合物  

下一步计划：  
1. 研究plip，生成相互作用力并生成图片

---
### 软件的安装：  
解压main.zip到需要安装的目录，直接运行内部的main.exe文件即可。  
注意：本软件的解压路径不要包含空格和中文！
  
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
 出现如下结果则设置成功  
 ![obabel](https://raw.githubusercontent.com/beikwx/Sail_vina_2.0/master/readme_pic/cmd_obabel.jpg)
  
- 安装ADT  
[ADT下载](http://mgltools.scripps.edu/downloads/downloads/tars/releases/REL1.5.6/mgltools_win32_1.5.6_Setup.exe)

---

### 教程：伊马替尼以及自定义配体和络氨酸激酶对接
可以通过本教程测试软件是否配置正确，建议使用同样的文件夹。  

本教程文件夹目录：  
D:/test_sailvina/Ligands/mol  
D:/test_sailvina/Ligands/pdbqt  
D:/test_sailvina/Proteins/1IEP_imatinib  
D:/test_sailvina/Docking_output  

1. 去pdbbank[下载1IEP](https://files.rcsb.org/download/1IEP.pdb)蛋白文件放置到D:/test_sailvina/Proteins/1IEP_imatinib
文件夹下
![pdb](https://raw.githubusercontent.com/beikwx/Sail_vina_2.0/master/readme_pic/pdb_bank.jpg)
2. 使用autodock tools导出共晶配体，准备受体文件。 
    - 打开ADT，导入刚下载的蛋白 
    - Edit - delete water
    - 选择B链, 然后Edit - Delete - Delete Selected Atoms。（因为AB同源，保留A链进行对接即可）
    - 选择A链中的CL1、CL2、CL4、CL5，同上删除。（删除氯离子）
    - 选择STI201，然后Select - Invert Selection，再Edit - Misc - 
    Split Selection - OK（分离配体和受体蛋白，配体叫1iep，受体叫1iep_copy1）
    - Ligand - Input - Choose - 弹出选择框 - 双击1iep - 确定（让ADT确定配体）
    - Ligand - Output - Save as PDBQT（导出共晶配体）
    保存共晶配体到D:/test_sailvina/Proteins/1IEP_imatinib/co_cystal.pdbqt（
    ADT的Bug，这里需要手动输入后缀）
    - Grid - Macromolecule - Choose - 弹出选择框 - 双击1iep_copy1 - 确定（一般弹出-contains no non-bonded atoms表示受体没有问题） - 选择D:/test_sailvina/Proteins/1IEP_imatinib/preped.pdbqt保存（受体一定要保存成这个名字，否则无法识别）
    - 关闭ADT
3. 生成对接配置文件
    - 打开SailVina
    - 在“准备对接配置”选项卡的“工具”中点击读取共晶配体。选择D:/test_sailvina/Proteins/1IEP_imatinib/co_cystal.pdbqt
    - 点击计算对接位点 - 确定，参数会变成如下（由于盒子总大小不能超过27000，所以如果过大需要根据实际需求修改盒子大小）  
    ![co_ligand](https://raw.githubusercontent.com/beikwx/Sail_vina_2.0/master/readme_pic/load_co_ligand.jpg)
    - 点击选择输出目录，选择D:/test_sailvina/Proteins/1IEP_imatinib，点击输出 - 确定
4. 准备配体
    - 使用化学作图软件（Chemdraw等）绘制出要对接的配体，保存成mol格式。（作为对接的验证，需要重新绘制原始共晶配体进行再对接re-docking，根据rmsd来判断对接的可靠程度。）本教程绘制2个，伊马替尼和尼洛替尼。保存到D:/test_sailvina/Ligands/mol文件夹中
    - 在SailVina“准备配体”选项卡中，按照下图配置参数。（脚本配置中的ADT的python路径请选择自己安装的路径）  
    ![preped_ligand](https://raw.githubusercontent.com/beikwx/Sail_vina_2.0/master/readme_pic/preped_ligands.jpg)
    - 点击“开始转换”等待完成即可。
5. 分子对接
    - 在“分子对接选项”卡中按照下图选择  
    ![docking](https://raw.githubusercontent.com/beikwx/Sail_vina_2.0/master/readme_pic/docking.jpg)  
    - 点击“开始对接”即可进行对接。（由于Vina对接会消耗大量CPU资源，如果出现未响应为正常现象，请等待对接完成）  
    ![docking_process](https://raw.githubusercontent.com/beikwx/Sail_vina_2.0/master/readme_pic/docking_process.jpg)
6. 结果分析
    - 目前处于开发阶段，对接结果保存在Docking_output文件夹中，可自行查看分析。  
    ![docking_result](https://raw.githubusercontent.com/beikwx/Sail_vina_2.0/master/readme_pic/docking_result.jpg)  
    图中绿色为对接配体，蓝色为原始共晶配体，可以看到对接结果还是比较可靠的。  
    查看作用力，rmsd计算将在后续版本提供。