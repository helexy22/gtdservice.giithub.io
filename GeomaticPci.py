# how to open the irvine.pix Dataset
import os
import pci
from pci.api import datasource as ds
irvine_pix = os.path.join(pci.getHomePath(), 'demo', 'irvine.pix') # get the path to irvine.pix in the demo folder
dataset = ds.open_dataset(irvine_pix) # open the dataset

# The following example shows how get the number of rows, columns and channels of a Dataset.
with ds.open_dataset(irvine_pix) as dataset:
    rows = dataset.width
    cols = dataset.height
    chans = dataset.chan_count
