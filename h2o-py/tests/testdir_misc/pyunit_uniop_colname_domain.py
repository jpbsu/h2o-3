from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils

#Test to see if you apply H2O uniop methods to an H2OFrame it will not overwrite the column headers & domains

def pyunit_colname_uniop():
    dataframe = {'A': [1,0,3,4], 'B': [5,6,-6, -1], 'C':[-4, -6, -7, 8]}
    frame = h2o.H2OFrame(dataframe)
    frame_asin = frame.asin()
    assert frame.names == frame_asin.names,"Expected equal col names after uniop operation"
    assert frame.types == frame_asin.types,"Expected equal col types after uniop operation"

if __name__ == "__main__":
    pyunit_utils.standalone_test(pyunit_colname_uniop)
else:
    pyunit_colname_uniop()