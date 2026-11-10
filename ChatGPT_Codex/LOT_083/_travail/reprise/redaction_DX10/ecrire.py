from lib import Cours
import p01_04,p05_07,p08_10,p11,p12_14
c=Cours()
for module in [p01_04,p05_07,p08_10,p11,p12_14]:module.rediger(c)
c.assembler()
