from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import Structure, Model, Chain, Select
from Bio.PDB import PDBIO


class ReceptorProcessor(object):

    @staticmethod
    def get_structure(pdb_path: str):
        parse = PDBParser(PERMISSIVE=1)
        pdb_id = pdb_path.strip("/")[-1].strip(".")[0]
        structure = parse.get_structure(pdb_id, pdb_path)
        return structure

    @staticmethod
    def get_model_nums(structure: Structure):
        times = 0
        models = structure.get_models()
        for model in models:
            times += 1
        return times

    @staticmethod
    def get_model_ids(structure: Structure):
        models = structure.get_models()
        model_list = []
        for model in models:
            model_list.append(model.get_id())
        return model_list

    @staticmethod
    def get_chain_nums(model: Model):
        times = 0
        chains = model.get_chains()
        for chain in chains:
            times += 1
        return times

    @staticmethod
    def get_chain_ids(model: Model):
        chains = model.get_chains()
        chain_list = []
        for chain in chains:
            chain_list.append(chain.get_id())
        return chain_list

    @staticmethod
    def get_het_nums(chain: Chain):
        times = 0
        residues = chain.get_residues()
        for residue in residues:
            residue_id = residue.get_id()
            hetfield = residue_id[0]
            if hetfield != " " and hetfield != "W":
                times += 1
        return times

    @staticmethod
    def get_het_ids(chain: Chain):
        residues = chain.get_residues()
        residue_list = []
        for residue in residues:
            residue_id = residue.get_id()
            hetfield = residue_id[0]
            if hetfield != " " and hetfield != "W":
                residue_list.append(hetfield)
        return residue_list

    @staticmethod
    def get_het_idname(hetname, chain: Chain):
        residues = chain.get_residues()
        for residue in residues:
            residue_id = residue.get_id()
            hetfield = residue_id[0]
            if hetfield != " " and hetfield != "W":
                if residue_id[0] == hetname:
                    return residue_id
        else:
            return None


class LigandExtractor(object):
    structure = None
    model_num = None
    chain_name = None
    residue_name = None

    model = None
    chain = None
    ligand = None

    def __init__(self, structure, model_num, chain_name, residue_name):
        LigandExtractor.structure = structure
        LigandExtractor.model_num = model_num
        LigandExtractor.chain_name = chain_name
        LigandExtractor.residue_name = residue_name

    def extract_ligand(self, save_path):
        # 拿到model对象
        LigandExtractor.model = LigandExtractor.structure[LigandExtractor.model_num]
        # 拿到chain对象
        LigandExtractor.chain = LigandExtractor.model[LigandExtractor.chain_name]
        # 拿到配体对象
        for protein_res in self.chain.child_list:
            if LigandExtractor.residue_name == protein_res.resname:
                LigandExtractor.ligand = protein_res

        class LigandSelect(Select):

            def accept_model(self, model):
                if model == LigandExtractor.model:
                    return 1
                else:
                    return 0

            def accept_chain(self, chain):
                if chain == LigandExtractor.chain:
                    return 1
                else:
                    return 0

            def accept_residue(self, residue):
                if residue == LigandExtractor.ligand:
                    return 1
                else:
                    return 0

        io = PDBIO()
        io.set_structure(self.structure)
        io.save(save_path + "/%s_%s.pdb" % (LigandExtractor.chain_name, LigandExtractor.residue_name), LigandSelect())


if __name__ == '__main__':
    s = PDBParser().get_structure("3ln1", "D:/Desktop/3ln1.pdb")
    extractor = LigandExtractor(s, 0, "A", "CEL")
    extractor.extract_ligand("D:/Desktop")
