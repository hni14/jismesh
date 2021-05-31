from __future__ import absolute_import

import numpy as _np
import warnings
from . import _vector
from . import _scalar

class JismeshNonstandardWarning(Warning):
    pass

def unit_lat(level):
    warn_if_nonstandard(level)
    if _np.isscalar(level):
        unit_lat = _scalar.unit_lat
    else:
        unit_lat = _vector.unit_lat
    
    return unit_lat(level)

def unit_lon(level):
    warn_if_nonstandard(level)
    if _np.isscalar(level):
        unit_lon = _scalar.unit_lon
    else:
        unit_lon = _vector.unit_lon
    
    return unit_lon(level)

def to_meshcode(lat, lon, level, astype=_np.int64):
    warn_if_nonstandard(level)
    if _np.isscalar(lat) and _np.isscalar(lon) and _np.isscalar(level):
        to_meshcode = _scalar.to_meshcode
    else:
        to_meshcode = _vector.to_meshcode
    
    return to_meshcode(lat, lon, level, astype)

def to_meshlevel(meshcode):
    if _np.isscalar(meshcode):
        to_meshlevel = _scalar.to_meshlevel
    else:
        to_meshlevel = _vector.to_meshlevel
    
    meshlevel = to_meshlevel(meshcode)
    warn_if_nonstandard(meshlevel)
    return meshlevel

def to_meshpoint(meshcode, lat_multiplier, lon_multiplier):
    if _np.isscalar(meshcode) and _np.isscalar(lat_multiplier) and _np.isscalar(lon_multiplier):
        to_meshpoint = _scalar.to_meshpoint
    else:
        to_meshpoint = _vector.to_meshpoint

    to_meshlevel(meshcode)  # for JismeshNonstandardWarning

    return to_meshpoint(meshcode, lat_multiplier, lon_multiplier)

def to_envelope(meshcode_sw, meshcode_ne):
    assert _np.isscalar(meshcode_sw)
    assert _np.isscalar(meshcode_sw)
    assert type(meshcode_sw) == type(meshcode_ne)

    to_meshlevel(meshcode_sw)  # for JismeshNonstandardWarning
    to_meshlevel(meshcode_ne)  # for JismeshNonstandardWarning
    
    to_envelope = _scalar.to_envelope
    
    return to_envelope(meshcode_sw, meshcode_ne)

def to_intersects(meshcode, to_level):
    assert _np.isscalar(meshcode)
    assert _np.isscalar(to_level)

    warn_if_nonstandard(to_level)

    to_intersects = _scalar.to_intersects
    
    return to_intersects(meshcode, to_level)

def is_nonstandard(level):
    if _np.isscalar(level):
        is_nonstandard = _scalar.is_nonstandard
    else:
        is_nonstandard = _vector.is_nonstandard

    return is_nonstandard(level)

def warn_if_nonstandard(level):
    if is_nonstandard(level):
        warnings.warn("Levels 7, 8, 9, and 10 are not standard levels.", JismeshNonstandardWarning, stacklevel=3)