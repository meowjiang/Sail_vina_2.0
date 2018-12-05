import os
import configer

python_path = configer.Configer.get_para("python_path")
pdbqt_to_pdb_path = os.path.realpath(__file__) + "/../res/pdbqt_to_pdb.py"
cmd = "%s %s" % (python_path, pdbqt_to_pdb_path)
text = os.system(cmd)
if text == 1:
    print("不对")
else:
    print("通过")

"advd".startswith()
