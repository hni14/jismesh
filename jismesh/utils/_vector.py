# -*- coding: utf-8 -*-

from __future__ import division as _division
import sys as _sys
import numpy as _np
if _sys.version_info.major < 3:
    import functools32 as _functools
else:
    import functools as _functools

def _get_num_digits(t):
    return _np.floor(_np.log10(t)+1)

def _slice(t, start, stop):
    num_digits = _get_num_digits(t)
    return (t % 10 ** (num_digits-start)) // 10 ** (num_digits-stop)

# unit in degree of latitude and longitude for each mesh level. 
_unit_lat_lv1 = _functools.lru_cache(1)(lambda: 2/3)
_unit_lon_lv1 = _functools.lru_cache(1)(lambda: 1)
_unit_lat_40000 = _functools.lru_cache(1)(lambda: _unit_lat_lv1()/2)
_unit_lon_40000 = _functools.lru_cache(1)(lambda: _unit_lon_lv1()/2)
_unit_lat_20000 = _functools.lru_cache(1)(lambda: _unit_lat_40000()/2)
_unit_lon_20000 = _functools.lru_cache(1)(lambda: _unit_lon_40000()/2)
_unit_lat_16000 = _functools.lru_cache(1)(lambda: _unit_lat_lv1()/5)
_unit_lon_16000 = _functools.lru_cache(1)(lambda: _unit_lon_lv1()/5)
_unit_lat_lv2 = _functools.lru_cache(1)(lambda: _unit_lat_lv1()/8)
_unit_lon_lv2 = _functools.lru_cache(1)(lambda: _unit_lon_lv1()/8)
_unit_lat_8000 = _functools.lru_cache(1)(lambda: _unit_lat_lv1()/10)
_unit_lon_8000 = _functools.lru_cache(1)(lambda: _unit_lon_lv1()/10)
_unit_lat_5000 = _functools.lru_cache(1)(lambda: _unit_lat_lv2()/2)
_unit_lon_5000 = _functools.lru_cache(1)(lambda: _unit_lon_lv2()/2)
_unit_lat_4000 = _functools.lru_cache(1)(lambda: _unit_lat_8000()/2)
_unit_lon_4000 = _functools.lru_cache(1)(lambda: _unit_lon_8000()/2)
_unit_lat_2500 = _functools.lru_cache(1)(lambda: _unit_lat_5000()/2)
_unit_lon_2500 = _functools.lru_cache(1)(lambda: _unit_lon_5000()/2)
_unit_lat_2000 = _functools.lru_cache(1)(lambda: _unit_lat_lv2()/5)
_unit_lon_2000 = _functools.lru_cache(1)(lambda: _unit_lon_lv2()/5)
_unit_lat_lv3 = _functools.lru_cache(1)(lambda: _unit_lat_lv2()/10)
_unit_lon_lv3 = _functools.lru_cache(1)(lambda: _unit_lon_lv2()/10)
_unit_lat_lv4 = _functools.lru_cache(1)(lambda: _unit_lat_lv3()/2)
_unit_lon_lv4 = _functools.lru_cache(1)(lambda: _unit_lon_lv3()/2)
_unit_lat_lv5 = _functools.lru_cache(1)(lambda: _unit_lat_lv4()/2)
_unit_lon_lv5 = _functools.lru_cache(1)(lambda: _unit_lon_lv4()/2)
_unit_lat_lv6 = _functools.lru_cache(1)(lambda: _unit_lat_lv5()/2)
_unit_lon_lv6 = _functools.lru_cache(1)(lambda: _unit_lon_lv5()/2)
_unit_lat_lv7 = _functools.lru_cache(1)(lambda: _unit_lat_lv6()/2)
_unit_lon_lv7 = _functools.lru_cache(1)(lambda: _unit_lon_lv6()/2)
_unit_lat_lv8 = _functools.lru_cache(1)(lambda: _unit_lat_lv7()/2)
_unit_lon_lv8 = _functools.lru_cache(1)(lambda: _unit_lon_lv7()/2)
_unit_lat_lv9 = _functools.lru_cache(1)(lambda: _unit_lat_lv8()/2)
_unit_lon_lv9 = _functools.lru_cache(1)(lambda: _unit_lon_lv8()/2)
_unit_lat_lv10 = _functools.lru_cache(1)(lambda: _unit_lat_lv9()/2)
_unit_lon_lv10 = _functools.lru_cache(1)(lambda: _unit_lon_lv9()/2)

_supported_levels = [1, 40000, 20000, 16000, 2, 8000, 5000, 4000, 2500, 2000, 3, 4, 5, 6, 7, 8, 9, 10]
_nonstandard_levels = [7, 8, 9, 10]

def unit_lat(level):
    level = _np.atleast_1d(level).astype(_np.int64)

    if not _np.all(_np.isin(level, _supported_levels)):
        raise ValueError('Unsupported level is specified.')
    
    lat = _np.zeros(level.size, dtype=_np.float64)
    lat[level==1] = _unit_lat_lv1()
    lat[level==40000] = _unit_lat_40000()
    lat[level==20000] = _unit_lat_20000()
    lat[level==16000] = _unit_lat_16000()
    lat[level==2] = _unit_lat_lv2()
    lat[level==8000] = _unit_lat_8000()
    lat[level==5000] = _unit_lat_5000()
    lat[level==4000] = _unit_lat_4000()
    lat[level==2500] = _unit_lat_2500()
    lat[level==2000] = _unit_lat_2000()
    lat[level==3] = _unit_lat_lv3()
    lat[level==4] = _unit_lat_lv4()
    lat[level==5] = _unit_lat_lv5()
    lat[level==6] = _unit_lat_lv6()
    lat[level==7] = _unit_lat_lv7()
    lat[level==8] = _unit_lat_lv8()
    lat[level==9] = _unit_lat_lv9()
    lat[level==10] = _unit_lat_lv10()

    if lat.size == 1:
        lat =  _np.asscalar(lat)

    return lat

def unit_lon(level):
    level = _np.atleast_1d(level).astype(_np.int64)

    if not _np.all(_np.isin(level, _supported_levels)):
        raise ValueError('Unsupported level is specified.')
    
    lon = _np.zeros(level.size, dtype=_np.float64)
    lon[level==1] = _unit_lon_lv1()
    lon[level==40000] = _unit_lon_40000()
    lon[level==20000] = _unit_lon_20000()
    lon[level==16000] = _unit_lon_16000()
    lon[level==2] = _unit_lon_lv2()
    lon[level==8000] = _unit_lon_8000()
    lon[level==5000] = _unit_lon_5000()
    lon[level==4000] = _unit_lon_4000()
    lon[level==2500] = _unit_lon_2500()
    lon[level==2000] = _unit_lon_2000()
    lon[level==3] = _unit_lon_lv3()
    lon[level==4] = _unit_lon_lv4()
    lon[level==5] = _unit_lon_lv5()
    lon[level==6] = _unit_lon_lv6()
    lon[level==7] = _unit_lon_lv7()
    lon[level==8] = _unit_lon_lv8()
    lon[level==9] = _unit_lon_lv9()
    lon[level==10] = _unit_lon_lv10()

    if lon.size == 1:
        lon =  _np.asscalar(lon)

    return lon

def to_meshcode(lat, lon, level, astype):
    """緯度経度から指定次の地域メッシュコードを算出する。

    Args:
        lat: 世界測地系の緯度(度単位)
        lon: 世界測地系の経度(度単位)
        level: 地域メッシュコードの次数
                1次(80km四方):1
                40倍(40km四方):40000
                20倍(20km四方):20000
                16倍(16km四方):16000
                2次(10km四方):2
                8倍(8km四方):8000
                5倍(5km四方):5000
                4倍(4km四方):4000
                2.5倍(2.5km四方):2500
                2倍(2km四方):2000
                3次(1km四方):3
                4次(500m四方):4
                5次(250m四方):5
                6次(125m四方):6
                7次(62.5m四方):7
                8次(31.25m四方):8
                9次(15.625m四方):9
                10次(7.8125四方):10
        astype: 戻り値メッシュコードの型
    Return:
        指定次の地域メッシュコード

    """
    # reminder of latitude and longitude by its unit in degree of mesh level.
    rem_lat_lv0 = lambda lat: lat
    rem_lon_lv0 = lambda lon: lon % 100
    rem_lat_lv1 = lambda lat: rem_lat_lv0(lat) % _unit_lat_lv1()
    rem_lon_lv1 = lambda lon: rem_lon_lv0(lon) % _unit_lon_lv1()
    rem_lat_40000 = lambda lat: rem_lat_lv1(lat) % _unit_lat_40000()
    rem_lon_40000 = lambda lon: rem_lon_lv1(lon) % _unit_lon_40000()
    rem_lat_20000 = lambda lat: rem_lat_40000(lat) % _unit_lat_20000()
    rem_lon_20000 = lambda lon: rem_lon_40000(lon) % _unit_lon_20000()
    rem_lat_16000 = lambda lat: rem_lat_lv1(lat) % _unit_lat_16000()
    rem_lon_16000 = lambda lon: rem_lon_lv1(lon) % _unit_lon_16000()
    rem_lat_lv2 = lambda lat: rem_lat_lv1(lat) % _unit_lat_lv2()
    rem_lon_lv2 = lambda lon: rem_lon_lv1(lon) % _unit_lon_lv2()
    rem_lat_8000 = lambda lat: rem_lat_lv1(lat) % _unit_lat_8000()
    rem_lon_8000 = lambda lon: rem_lon_lv1(lon) % _unit_lon_8000()
    rem_lat_5000 = lambda lat: rem_lat_lv2(lat) % _unit_lat_5000()
    rem_lon_5000 = lambda lon: rem_lon_lv2(lon) % _unit_lon_5000()
    rem_lat_4000 = lambda lat: rem_lat_8000(lat) % _unit_lat_4000()
    rem_lon_4000 = lambda lon: rem_lon_8000(lon) % _unit_lon_4000()
    rem_lat_2500 = lambda lat: rem_lat_5000(lat) % _unit_lat_2500()
    rem_lon_2500 = lambda lon: rem_lon_5000(lon) % _unit_lon_2500()
    rem_lat_2000 = lambda lat: rem_lat_lv2(lat) % _unit_lat_2000()
    rem_lon_2000 = lambda lon: rem_lon_lv2(lon) % _unit_lon_2000()
    rem_lat_lv3 = lambda lat: rem_lat_lv2(lat) % _unit_lat_lv3()
    rem_lon_lv3 = lambda lon: rem_lon_lv2(lon) % _unit_lon_lv3()
    rem_lat_lv4 = lambda lat: rem_lat_lv3(lat) % _unit_lat_lv4()
    rem_lon_lv4 = lambda lon: rem_lon_lv3(lon) % _unit_lon_lv4()
    rem_lat_lv5 = lambda lat: rem_lat_lv4(lat) % _unit_lat_lv5()
    rem_lon_lv5 = lambda lon: rem_lon_lv4(lon) % _unit_lon_lv5()
    rem_lat_lv6 = lambda lat: rem_lat_lv5(lat) % _unit_lat_lv6()
    rem_lon_lv6 = lambda lon: rem_lon_lv5(lon) % _unit_lon_lv6()
    rem_lat_lv7 = lambda lat: rem_lat_lv6(lat) % _unit_lat_lv7()
    rem_lon_lv7 = lambda lon: rem_lon_lv6(lon) % _unit_lon_lv7()
    rem_lat_lv8 = lambda lat: rem_lat_lv7(lat) % _unit_lat_lv8()
    rem_lon_lv8 = lambda lon: rem_lon_lv7(lon) % _unit_lon_lv8()
    rem_lat_lv9 = lambda lat: rem_lat_lv8(lat) % _unit_lat_lv9()
    rem_lon_lv9 = lambda lon: rem_lon_lv8(lon) % _unit_lon_lv9()
    rem_lat_lv10 = lambda lat: rem_lat_lv9(lat) % _unit_lat_lv10()
    rem_lon_lv10 = lambda lon: rem_lon_lv9(lon) % _unit_lon_lv10()

    def meshcode_lv1(lat, lon):
        ab = (rem_lat_lv0(lat) // _unit_lat_lv1())
        cd = rem_lon_lv0(lon) // _unit_lon_lv1()
        return ab*100 + cd

    def meshcode_40000(lat, lon):
        e = (rem_lat_lv1(lat) // _unit_lat_40000())*2 + (rem_lon_lv1(lon) // _unit_lon_40000()) + 1
        return meshcode_lv1(lat, lon)*10 + e

    def meshcode_20000(lat, lon):
        f = (rem_lat_40000(lat) // _unit_lat_20000())*2 + (rem_lon_40000(lon) // _unit_lon_20000()) + 1
        g = 5
        return meshcode_40000(lat, lon)*100 + f*10 + g

    def meshcode_16000(lat, lon):
        e = (rem_lat_lv1(lat) // _unit_lat_16000())*2
        f = (rem_lon_lv1(lon) // _unit_lon_16000())*2
        g = 7
        return meshcode_lv1(lat, lon)*1000 + e*100 + f*10 + g

    def meshcode_lv2(lat, lon):
        e = (rem_lat_lv1(lat) // _unit_lat_lv2())
        f = (rem_lon_lv1(lon) // _unit_lon_lv2())
        return meshcode_lv1(lat, lon)*100 + e*10 + f

    def meshcode_8000(lat, lon):
        e = (rem_lat_lv1(lat) // _unit_lat_8000())
        f = (rem_lon_lv1(lon) // _unit_lon_8000())
        g = 6
        return meshcode_lv1(lat, lon)*1000 + e*100 + f*10 + g

    def meshcode_5000(lat, lon):
        g = (rem_lat_lv2(lat) // _unit_lat_5000())*2 + (rem_lon_lv2(lon) // _unit_lon_5000()) + 1
        return meshcode_lv2(lat, lon)*10 + g

    def meshcode_4000(lat, lon):
        h = (rem_lat_8000(lat) // _unit_lat_4000())*2 + (rem_lon_8000(lon) // _unit_lon_4000()) + 1
        i = 7
        return meshcode_8000(lat, lon)*100 + h*10 + i

    def meshcode_2500(lat, lon):
        h = (rem_lat_5000(lat) // _unit_lat_2500())*2 + (rem_lon_5000(lon) // _unit_lon_2500()) + 1
        i = 6
        return meshcode_5000(lat, lon)*100 + h*10 + i

    def meshcode_2000(lat, lon):
        g = (rem_lat_lv2(lat) // _unit_lat_2000())*2
        h = (rem_lon_lv2(lon) // _unit_lon_2000())*2
        i = 5
        return meshcode_lv2(lat, lon)*1000 + g*100 + h*10 + i

    def meshcode_lv3(lat, lon):
        g = (rem_lat_lv2(lat) // _unit_lat_lv3())
        h = (rem_lon_lv2(lon) // _unit_lon_lv3())
        return meshcode_lv2(lat, lon)*100 + g*10 + h

    def meshcode_lv4(lat, lon):
        i = (rem_lat_lv3(lat) // _unit_lat_lv4())*2 + (rem_lon_lv3(lon) // _unit_lon_lv4()) + 1
        return meshcode_lv3(lat, lon)*10 + i

    def meshcode_lv5(lat, lon):
        j = (rem_lat_lv4(lat) // _unit_lat_lv5())*2 + (rem_lon_lv4(lon) // _unit_lon_lv5()) + 1
        return meshcode_lv4(lat, lon)*10 + j

    def meshcode_lv6(lat, lon):
        k = (rem_lat_lv5(lat) // _unit_lat_lv6())*2 + (rem_lon_lv5(lon) // _unit_lon_lv6()) + 1
        return meshcode_lv5(lat, lon)*10 + k

    def meshcode_lv7(lat, lon):
        l = (rem_lat_lv6(lat) // _unit_lat_lv7())*2 + (rem_lon_lv6(lon) // _unit_lon_lv7()) + 1
        return meshcode_lv6(lat, lon)*10 + l

    def meshcode_lv8(lat, lon):
        m = (rem_lat_lv7(lat) // _unit_lat_lv8())*2 + (rem_lon_lv7(lon) // _unit_lon_lv8()) + 1
        return meshcode_lv7(lat, lon)*10 + m

    def meshcode_lv9(lat, lon):
        n = (rem_lat_lv8(lat) // _unit_lat_lv9())*2 + (rem_lon_lv8(lon) // _unit_lon_lv9()) + 1
        return meshcode_lv8(lat, lon)*10 + n

    def meshcode_lv10(lat, lon):
        o = (rem_lat_lv9(lat) // _unit_lat_lv10())*2 + (rem_lon_lv9(lon) // _unit_lon_lv10()) + 1
        return meshcode_lv9(lat, lon)*10 + o

    lat = _np.atleast_1d(lat).astype(_np.float64)
    lon = _np.atleast_1d(lon).astype(_np.float64)
    level = _np.atleast_1d(level).astype(_np.int64)

    if not _np.all(_np.isin(level, _supported_levels)):
        raise ValueError('Unsupported level is specified.')

    if _np.any(lat < 0) | _np.any(lat >= 66.66):
        raise ValueError('The latitude is out of bound(0 <= latitude < 66.66).')

    if _np.any(lon < 100) | _np.any(lon >= 180):
        raise ValueError('The longitude is out of bound(100 <= longitude < 180).')

    meshcode_shape = max(lat.size, lon.size, level.size)
    meshcode = _np.zeros(meshcode_shape, dtype=_np.float64)
    
    if _np.any(_np.isin(level, 1)):
        meshcode += meshcode_lv1(lat, lon) * (level == 1)

    if _np.any(_np.isin(level, 40000)):
        meshcode += meshcode_40000(lat, lon) * (level == 40000)
    
    if _np.any(_np.isin(level, 20000)):
        meshcode += meshcode_20000(lat, lon) * (level == 20000)
    
    if _np.any(_np.isin(level, 16000)):
        meshcode += meshcode_16000(lat, lon) * (level == 16000)

    if _np.any(_np.isin(level, 2)):
        meshcode += meshcode_lv2(lat, lon) * (level == 2)

    if _np.any(_np.isin(level, 8000)):
        meshcode += meshcode_8000(lat, lon) * (level == 8000)

    if _np.any(_np.isin(level, 5000)):
        meshcode += meshcode_5000(lat, lon) * (level == 5000)

    if _np.any(_np.isin(level, 4000)):
        meshcode += meshcode_4000(lat, lon) * (level == 4000)

    if _np.any(_np.isin(level, 2500)):
        meshcode += meshcode_2500(lat, lon) * (level == 2500)

    if _np.any(_np.isin(level, 2000)):
        meshcode += meshcode_2000(lat, lon) * (level == 2000)

    if _np.any(_np.isin(level, 3)):
        meshcode += meshcode_lv3(lat, lon) * (level == 3)

    if _np.any(_np.isin(level, 4)):
        meshcode += meshcode_lv4(lat, lon) * (level == 4)

    if _np.any(_np.isin(level, 5)):
        meshcode += meshcode_lv5(lat, lon) * (level == 5)

    if _np.any(_np.isin(level, 6)):
        meshcode += meshcode_lv6(lat, lon) * (level == 6)

    if _np.any(_np.isin(level, 7)):
        meshcode += meshcode_lv7(lat, lon) * (level == 7)

    if _np.any(_np.isin(level, 8)):
        meshcode += meshcode_lv8(lat, lon) * (level == 8)

    if _np.any(_np.isin(level, 9)):
        meshcode += meshcode_lv9(lat, lon) * (level == 9)

    if _np.any(_np.isin(level, 10)):
        meshcode += meshcode_lv10(lat, lon) * (level == 10)
    
    meshcode = meshcode.astype(_np.int64)
    meshcode = meshcode.astype(astype)

    if meshcode.size == 1:
        meshcode =  _np.asscalar(meshcode)

    return meshcode

def to_meshlevel(meshcode):
    """メッシュコードから次数を算出する。

    Args:
        meshcode: メッシュコード
    Return:
        地域メッシュコードの次数
                1次(80km四方):1
                40倍(40km四方):40000
                20倍(20km四方):20000
                16倍(16km四方):16000
                2次(10km四方):2
                8倍(8km四方):8000
                5倍(5km四方):5000
                4倍(4km四方):4000
                2.5倍(2.5km四方):2500
                2倍(2km四方):2000
                3次(1km四方):3
                4次(500m四方):4
                5次(250m四方):5
                6次(125m四方):6
                7次(62.5m四方):7
                8次(31.25m四方):8
                9次(15.625m四方):9
                10次(7.8125四方):10
    """
    meshcode = _np.array(meshcode).astype(_np.int64)
    level = _np.full(meshcode.shape, _np.int64(-1))
    num_digits = _get_num_digits(meshcode)

    #ab = _slice(meshcode, 0, 2)
    #cd = _slice(meshcode, 2, 4)
    #e = _slice(meshcode, 4, 5)
    #f = _slice(meshcode, 5, 6)
    g = _slice(meshcode, 6, 7)
    #h = _slice(meshcode, 7, 8)
    i = _slice(meshcode, 8, 9)
    j = _slice(meshcode, 9, 10)
    k = _slice(meshcode, 10, 11)
    l = _slice(meshcode, 11, 12)
    m = _slice(meshcode, 12, 13)
    n = _slice(meshcode, 13, 14)
    o = _slice(meshcode, 14, 15)

    level[(num_digits==4)] = 1
    level[(num_digits==5)] = 40000
    level[(num_digits==6)] = 2
    level[(num_digits==7) & (_np.isin(g, [1,2,3,4]))] = 5000
    level[(num_digits==7) & (g == 6)] = 8000
    level[(num_digits==7) & (g == 5)] = 20000
    level[(num_digits==7) & (g == 7)] = 16000
    level[(num_digits==8)] = 3
    level[(num_digits==9) & (_np.isin(i, [1,2,3,4]))] = 4
    level[(num_digits==9) & (i == 5)] = 2000
    level[(num_digits==9) & (i == 6)] = 2500
    level[(num_digits==9) & (i == 7)] = 4000
    level[(num_digits==10) & (_np.isin(j, [1,2,3,4]))] = 5
    level[(num_digits==11) & (_np.isin(k, [1,2,3,4]))] = 6
    level[(num_digits==12) & (_np.isin(k, [1,2,3,4]))] = 7
    level[(num_digits==13) & (_np.isin(k, [1,2,3,4]))] = 8
    level[(num_digits==14) & (_np.isin(k, [1,2,3,4]))] = 9
    level[(num_digits==15) & (_np.isin(k, [1,2,3,4]))] = 10

    if level.size == 1:
        level =  _np.asscalar(level)

    return level

def to_meshpoint(meshcode, lat_multiplier, lon_multiplier):
    """地域メッシュコードから緯度経度を算出する。
        下記のメッシュに対応している。
                1次(80km四方):1
                40倍(40km四方):40000
                20倍(20km四方):20000
                16倍(16km四方):16000
                2次(10km四方):2
                8倍(8km四方):8000
                5倍(5km四方):5000
                4倍(4km四方):4000
                2.5倍(2.5km四方):2500
                2倍(2km四方):2000
                3次(1km四方):3
                4次(500m四方):4
                5次(250m四方):5
                6次(125m四方):6
                7次(62.5m四方):7
                8次(31.25m四方):8
                9次(15.625m四方):9
                10次(7.8125四方):10

    Args:
        meshcode: 指定次の地域メッシュコード
        lat_multiplier: 当該メッシュの基準点(南西端)から、緯度座標上の点の位置を当該メッシュの単位緯度の倍数で指定
        lon_multiplier: 当該メッシュの基準点(南西端)から、経度座標上の点の位置を当該メッシュの単位経度の倍数で指定
    Return:
        lat: 世界測地系の緯度(度単位)
        lon: 世界測地系の経度(度単位)

    """
    meshcode = _np.array(meshcode).astype(_np.int64)

    ab = _slice(meshcode, 0, 2)
    cd = _slice(meshcode, 2, 4)
    e = _slice(meshcode, 4, 5)
    f = _slice(meshcode, 5, 6)
    g = _slice(meshcode, 6, 7)
    h = _slice(meshcode, 7, 8)
    i = _slice(meshcode, 8, 9)
    j = _slice(meshcode, 9, 10)
    k = _slice(meshcode, 10, 11)
    l = _slice(meshcode, 11, 12)
    m = _slice(meshcode, 12, 13)
    n = _slice(meshcode, 13, 14)
    o = _slice(meshcode, 14, 15)

    level = to_meshlevel(meshcode)

    target_lv1 = level == 1
    target_40000 = level == 40000
    target_20000 = level == 20000
    target_16000 = level == 16000
    target_8000 = level == 8000
    target_4000 = level == 4000
    target_lv2 = level == 2
    target_5000 = level == 5000
    target_2500 = level == 2500
    target_2000 = level == 2000
    target_lv3 = level == 3
    target_lv4 = level == 4
    target_lv5 = level == 5
    target_lv6 = level == 6
    target_lv7 = level == 7
    target_lv8 = level == 8
    target_lv9 = level == 9
    target_lv10 = level == 10

    # level 1
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':1},        '5339'),
    targets = target_lv1 | target_40000 | target_20000 | target_16000 | target_8000 | target_4000 | target_lv2 | target_5000 | target_2500 | target_2000 | target_lv3 | target_lv4 | target_lv5 | target_lv6 | target_lv7 | target_lv8 | target_lv9| target_lv10
    lat = (ab * _unit_lat_lv1()) * targets
    lon = (cd * _unit_lon_lv1() + 100) * targets

    # level 40000
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':40000},    '53392'),
    targets = target_40000 | target_20000
    lat += ((e//3 == 1) * _unit_lat_40000()) * targets
    lon += ((e%2 == 0) * _unit_lon_40000()) * targets

    # level 20000
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':20000},    '5339235'),
    targets = target_20000
    lat += ((f//3 == 1) * _unit_lat_20000()) * targets
    lon += ((f%2 == 0) * _unit_lon_20000()) * targets

    # level 16000
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':16000},    '5339467'),
    targets = target_16000
    lat += (e//2 * _unit_lat_16000()) * targets
    lon += (f//2 * _unit_lon_16000()) * targets

    # level 8000
    #    ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':8000},     '5339476'),
    targets = target_8000 | target_4000
    lat += (e * _unit_lat_8000()) * targets
    lon += (f * _unit_lon_8000()) * targets
    
    # level 4000
    #    ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':4000},     '533947637'),
    targets = target_4000
    lat += ((h//3 == 1) * _unit_lat_4000()) * targets
    lon += ((h%2 == 0) * _unit_lon_4000()) * targets

    # level 2
    #  ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':2},        '533935'),
    targets = target_lv2 | target_5000 | target_2500 | target_2000 | target_lv3 | target_lv4 | target_lv5 | target_lv6 | target_lv7 | target_lv8 | target_lv9 | target_lv10
    lat += (e * _unit_lat_lv2()) * targets
    lon += (f * _unit_lon_lv2()) * targets

    # level 5000
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':5000},     '5339354'),
    targets = target_5000 | target_2500
    lat += ((g//3 == 1) * _unit_lat_5000()) * targets
    lon += ((g%2 == 0) * _unit_lon_5000()) * targets

    # level 2500
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':2500},     '533935446'),
    targets = target_2500
    lat += ((h//3 == 1) * _unit_lat_2500()) * targets
    lon += ((h%2 == 0) * _unit_lon_2500()) * targets

    # level 2000
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':2000},     '533935885'),
    targets = target_2000
    lat += (g//2 * _unit_lat_2000()) * targets
    lon += (h//2 * _unit_lon_2000()) * targets

    # level 3
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':3},        '53393599'),
    targets = target_lv3 | target_lv4 | target_lv5 | target_lv6 | target_lv7 | target_lv8 | target_lv9 | target_lv10
    lat += (g * _unit_lat_lv3()) * targets
    lon += (h * _unit_lon_lv3()) * targets

    # level 4
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':4},        '533935992'),
    targets = target_lv4 | target_lv5 | target_lv6 | target_lv7 | target_lv8 | target_lv9 | target_lv10
    lat += ((i//3 == 1) * _unit_lat_lv4()) * targets
    lon += ((i%2 == 0) * _unit_lon_lv4()) * targets

    # level 5
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':5},        '5339359921'),
    targets = target_lv5 | target_lv6 | target_lv7 | target_lv8 | target_lv9 | target_lv10
    lat += ((j//3 == 1) * _unit_lat_lv5()) * targets
    lon += ((j%2 == 0) * _unit_lon_lv5()) * targets

    # level 6
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':6},        '53393599212'),
    targets = target_lv6 | target_lv7 | target_lv8 | target_lv9 | target_lv10
    lat += ((k//3 == 1) * _unit_lat_lv6()) * targets
    lon += ((k%2 == 0) * _unit_lon_lv6()) * targets

    # level 7
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':7},        '533935992121'),
    targets = target_lv7 | target_lv8 | target_lv9 | target_lv10
    lat += ((k//3 == 1) * _unit_lat_lv7()) * targets
    lon += ((k%2 == 0) * _unit_lon_lv7()) * targets

    # level 8
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':8},        '5339359921211'),
    targets = target_lv8 | target_lv9 | target_lv10
    lat += ((k//3 == 1) * _unit_lat_lv8()) * targets
    lon += ((k%2 == 0) * _unit_lon_lv8()) * targets

    # level 9
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':9},        '53393599212113'),
    targets = target_lv9 | target_lv10
    lat += ((k//3 == 1) * _unit_lat_lv9()) * targets
    lon += ((k%2 == 0) * _unit_lon_lv9()) * targets

    # level 10
    # ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':10},        '533935992121134'),
    targets = target_lv10
    lat += ((k//3 == 1) * _unit_lat_lv10()) * targets
    lon += ((k%2 == 0) * _unit_lon_lv10()) * targets

    # メッシュ内座標
    lat +=  unit_lat(level)*lat_multiplier
    lon +=  unit_lon(level)*lon_multiplier

    return lat, lon

def is_nonstandard(level):
    return _np.any(_np.isin(level, _nonstandard_levels))