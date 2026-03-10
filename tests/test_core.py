import numpy as np
from src.core import inundation_mask,depth_grid,exposed_fraction
def test_depth_and_mask():
+    dem=np.array([[1,3],[5,7]],float)
+    assert inundation_mask(dem,4).tolist()==[[True,True],[False,False]]
+    assert depth_grid(dem,4).tolist()==[[3,1],[0,0]]
+    assert exposed_fraction(dem,4)==.5
