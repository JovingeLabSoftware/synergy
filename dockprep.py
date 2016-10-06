import chimera
import sys
import re
from DockPrep import prep
from DockPrep import AddH
from WriteMol2 import writeMol2

# ref: http://mailman.docking.org/pipermail/dock-fans/2007-May/001043.html
models = chimera.openModels.list(modelTypes=[chimera.Molecule])
prep(models, addHFunc=AddH.hbondAddHydrogens)

root = models[0].name.replace(".pdb", "")
if len(sys.argv) == 2:
     d = re.sub("/$", "", sys.argv[1]) + "/"
else:
     d = ""

writeMol2(models, d + root + "_prepped.mol2")

# ref: http://plato.cgl.ucsf.edu/pipermail/chimera-users/2011-March/006134.html
chimera.runCommand("surf")
surf = chimera.openModels.list(modelTypes=[chimera.MSMSModel])[0]
from WriteDMS import writeDMS
writeDMS(surf, d + root + ".dms")
