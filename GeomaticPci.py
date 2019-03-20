from pci.api import datasource

## how to open the irvine.pix Dataset
import os
import pci
from pci.api import datasource as ds
# get the path to irvine.pix in the demo folder
irvine_pix = os.path.join(pci.getHomePath(), 'demo', 'irvine.pix')

# open the dataset
dataset = ds.open_dataset(irvine_pix)