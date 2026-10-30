"""Reconstruit les dix monographies à partir des textes originaux versionnés."""
import importlib
for batch in ('1_2','3_4','5_6','7_8','9_10'):
    importlib.import_module('phase_b_'+batch).rediger()
