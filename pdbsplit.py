import sys
sys.path.insert(0, sys.path[0] + '/lib/python')

from jlab import jlpdb

if __name__ == "__main__":
    """ Parses PDB files desired chain, and creates new PDB structures,
        stripping all non-protein residues (inculding solvents and ligands)
    """
    import sys

    if not len(sys.argv) >= 3:
        print "Usage: $ python %s source chain [outdir]" % __file__
        sys.exit()

    if len(sys.argv) == 4:
        splitter = jlpdb.Splitter(sys.argv[3])
    else:
        splitter = jlpdb.Splitter()

    splitter.make_pdb(sys.argv[1], sys.argv[2])
