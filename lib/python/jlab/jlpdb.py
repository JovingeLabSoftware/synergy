import os
from Bio import PDB
import re


"""
Functions for manipulating PDB file relevant to jlab projects.

Adapted from David Cain's answer here:
http://stackoverflow.com/questions/11685716/how-to-extract-chains-from-a-pdb-file

"""

class Splitter:
    """Extracts and cleans a chain from a pdb file.

    The Splitter object must first be instantiated and then make_pdb can be called.
    In this way, multiple files can be processed with one Splitter object.  Non-backbone
    residues (including ligands and solvents) are stripped in the process.

    Attributes:
        out_dir (str, optional): Where to output the resulting pdb file. Default is current working directory

    """
    def __init__(self, out_dir=None):
        self.parser = PDB.PDBParser()
        self.writer = PDB.PDBIO()
        if out_dir is None:
            out_dir = os.getcwd()
        self.out_dir = out_dir

    def make_pdb(self, pdb_path, chain_letter, overwrite=False, struct=None):
        """ Create a new PDB file containing only the specified chains.

        Returns the path to the created file.

        :param pdb_path: full path to the crystal structure
        :param chain_letter: chain id to extract (single letter, case insensitive)
        :param overwrite: write over the output file if it exists
        """
        chain_letter = chain_letter.upper()
        base = pdb_path.replace("\\\\", "/").split("/").pop()

        # Input/output files
        (pdb_dir, pdb_fn) = os.path.split(pdb_path)
        pdb_id = pdb_fn[3:7]
        out_name = base.replace(".pdb", "_" + chain_letter + ".pdb")
        out_path = os.path.join(self.out_dir, out_name)

        # Skip PDB generation if the file already exists
        if (not overwrite) and (os.path.isfile(out_path)):
            print("Chain %s of '%s' already extracted to '%s'." %
                  (", ".join(chain_letter), pdb_id, out_name))
            return out_path

        # Get structure, write new file with only given chains
        if struct is None:
            struct = self.parser.get_structure(pdb_id, pdb_path)
        self.writer.set_structure(struct)
        self.writer.save(out_path, select=_selectChains(chain_letter))

        return out_path


class _selectChains(PDB.Select):
    def __init__(self, chain_letter):
        self.chain_letter = chain_letter

    def accept_chain(self, chain):
        return (chain.get_id() in self.chain_letter)

    def accept_residue(self, residue):
        # reject all non protein residues
        # hetero atoms (which in PDB parlance means small molecules that are not part of a
        # protein or nucleotide polymer) will have a het id (residue.get_id[0]) specified
        # whereas members of the polymer (i.e. the protein) will not.
        # This seems to effectively exclude ligands and solvents
        return  residue.get_id()[0] == ' '
