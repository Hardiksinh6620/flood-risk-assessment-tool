import numpy as np
from .validation import finite
def inundation_mask(dem,water_level,nodata=None):
    dem=finite(dem,"dem"); mask=dem<=float(water_level)
    if nodata is not None: mask=np.logical_and(mask,dem!=nodata)
    return mask
def depth_grid(dem,water_level):
    dem=finite(dem,"dem"); return np.maximum(float(water_level)-dem,0)
def exposed_fraction(dem,water_level): return float(inundation_mask(dem,water_level).mean())
