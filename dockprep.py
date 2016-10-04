import chimera
import sys
from DockPrep import prep
from DockPrep import AddH

# ref: http://mailman.docking.org/pipermail/dock-fans/2007-May/001043.html

models = chimera.openModels.list(modelTypes=[chimera.Molecule])
prep(models, addHFunc=AddH.hbondAddHydrogens)
print str(models[0].name)

root = models[0].name.replace(".pdb", "")
from WriteMol2 import writeMol2
writeMol2(models, root + "_prepped.mol2")

# ref: http://plato.cgl.ucsf.edu/pipermail/chimera-users/2011-March/006134.html
chimera.runCommand("surf")
surf = chimera.openModels.list(modelTypes=[chimera.MSMSModel])[0]
from WriteDMS import writeDMS
writeDMS(surf, root + ".dms")
