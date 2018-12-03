class MoleculeSpliter(object):

    def __init__(self, molecule, split_num):
        self.molecule = molecule
        self.split_num = split_num

    def split_molecule(self):
        with open(self.molecule, "r") as f:
            line = f.readline()
            print(line)
