import os
import sys


class Configer(object):

    def __init__(self):
        self.para_dict = {}

    @staticmethod
    def first_open():
        if not os.path.exists(os.path.realpath(sys.argv[0]) + "/../para.txt"):
            with open(os.path.realpath(sys.argv[0]) + "/../para.txt", "w") as f:
                initial_value = "center_x=0.0\n" \
                                "center_y=0.0\n" \
                                "center_z=0.0\n" \
                                "size_x=0.0\n" \
                                "size_y=0.0\n" \
                                "size_z=0.0\n" \
                                "exhaustiveness=8\n" \
                                "num_modes=9\n" \
                                "energy_range=3\n" \
                                "read_config=\n" \
                                "choose_raw_ligand=\n" \
                                "output_config=\n" \
                                "choose_ligands=\n" \
                                "input_format=\n" \
                                "output_format\n" \
                                "gen3d=1\n" \
                                "pH=7.4\n" \
                                "is_minimize=1\n" \
                                "minimize=\n" \
                                "ligand_output_dir=\n" \
                                "python_path=\n" \
                                "choose_docking_ligands=\n" \
                                "choose_docking_proteins=\n" \
                                "choose_docking_output=\n" \
                                "docking_times=1\n"
                f.write(initial_value)

    @staticmethod
    def get_para(para_text):
        with open(os.path.realpath(sys.argv[0]) + "/../para.txt", "r") as f:
            for line in f.readlines():
                if line.split("=")[0] == para_text:
                    return line.split("=")[1].strip()
            else:
                return ""

    def save_para(self):
        with open(os.path.realpath(sys.argv[0]) + "/../para.txt", "w") as f:
            for para in self.para_dict:
                f.write("%s=%s\n" % (para, self.para_dict[para]))


class ConfigReader(object):
    @staticmethod
    def get_config_para(parameter):
        if parameter == "\n":
            return "", ""
        return parameter.split("=")[0].strip(), parameter.split("=")[1].strip()


class ConfigWriter(object):

    @staticmethod
    def write_config(para_dict, output_path):
        with open("%s/config.txt" % output_path, "w") as f:
            for para in para_dict:
                line = "%s %s\n" % (para, para_dict[para])
                f.writelines(line)
