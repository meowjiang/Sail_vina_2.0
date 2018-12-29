TAB1_TEXT = "本界面来生成Vina对接所需要的配置文件。\n\n" \
            "操作步骤\n" \
            "1.在“主要参数”、“可选”中填写数值\n" \
            "2.选择输出目录，点击输出即可。\n\n" \
            "工具的使用\n" \
            "1.如果有要修改的config文件，通过“读取配置文件”来进行读取。" \
            "选择相应的config.txt，点击读取到参数，修改后再输出即可。\n" \
            "2.本工具可以使用共晶位点中的配体来自动计算对接位点，" \
            "\n参考文献：Feinstein WP, Brylinski M. (2015) Calculating an optimal box size for ligand docking and " \
            "virtual screening against experimental and predicted binding pockets. J Cheminform 7 (1):18\n" \
            "注意：选择的配体必须是pdbqt格式，使用ADT将配体挖出来即可。"

TAB2_TEXT = "本界面用于进行对接配体的格式转换\n\n" \
            "操作步骤\n" \
            "1.在“脚本配置”中选择ADT中的python.exe文件（需要安装mgltools，详情见README文件）\n" \
            "2.在“输入选项”中选择输入格式，选择配体或者配体所在的文件夹\n" \
            "3.在“输出选项”中选择输出格式，输入转换格式的pH值，是否生成" \
            "3D构象，是否进行能量最小化，选择能量最小化的力场，选择要输出配体的文件夹\n" \
            "4.点击开始转换。\n\n" \
            "脚本说明\n" \
            "由于格式转化调用的是obabel的格式转换功能，obabel转换成pdbqt文件会出现问题，导致苯环断裂" \
            "等问题。所以当转换成pdbqt文件时，先通过obabel转换成pdb文件，再通过adt的方法转换成pdbqt格式，" \
            "所以进度条会显示两遍。" \

TAB3_TEXT = "tab3帮助"

TAB4_TEXT = "本界面用于调用vina进行分子对接\n\n" \
            "操作步骤\n" \
            "1.选择配体\n" \
            "2.选择受体\n" \
            "3.选择结果输出的文件夹\n" \
            "4.输入每个配体要对接的次数\n" \
            "5.点击开始对接\n\n" \
            "对接说明\n" \
            "1.选择的配体只能是pdbqt文件或者含有pdbqt文件的文件夹\n" \
            "2.选择的受体是一个文件夹，受体在文件夹中，必须命名为“preped.pdbqt”" \
            "否则无法识别，并且需要config.txt文件，否则无法对接。\n" \
            "    如果要对多个受体进行对接，请选择包含这些受体文件夹的文件夹。比如要对接的" \
            "受体为A、B、C，分别为C:/receptors/A，C:/receptors/B，C:/receptors/C，选择" \
            "C:/receptors即可。"

TAB5_TEXT = "tab5帮助"

TAB6_TEXT = "tab5帮助"

TAB7_TEXT = "tab5帮助"

TAB8_TEXT = "tab5帮助"
