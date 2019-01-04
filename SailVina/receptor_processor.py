from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import Structure
from Bio.PDB.PDBIO import PDBIO


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
