# -*- coding: utf-8 -*-

from __future__ import division as _division
import sys as _sys
import numpy as _np
if _sys.version_info.major < 3:
    import functools32 as _functools
else:
    import functools as _functools

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

_dict_unit_lat_lon = {
    1 : (_unit_lat_lv1, _unit_lon_lv1),
    40000 : (_unit_lat_40000, _unit_lon_40000),
    20000 : (_unit_lat_20000, _unit_lon_20000),
    16000 : (_unit_lat_16000, _unit_lon_16000),
    2 : (_unit_lat_lv2, _unit_lon_lv2),
    8000 : (_unit_lat_8000, _unit_lon_8000),
    5000 : (_unit_lat_5000, _unit_lon_5000),
    4000 : (_unit_lat_4000, _unit_lon_4000),
    2500 : (_unit_lat_2500, _unit_lon_2500),
    2000 : (_unit_lat_2000, _unit_lon_2000),
    3 : (_unit_lat_lv3, _unit_lon_lv3),
    4 : (_unit_lat_lv4, _unit_lon_lv4),
    5 : (_unit_lat_lv5, _unit_lon_lv5),
    6 : (_unit_lat_lv6, _unit_lon_lv6),
    7 : (_unit_lat_lv7, _unit_lon_lv7),
    8 : (_unit_lat_lv8, _unit_lon_lv8),
    9 : (_unit_lat_lv9, _unit_lon_lv9),
    10 : (_unit_lat_lv10, _unit_lon_lv10)
}

_nonstandard_levels = [7, 8, 9, 10]

def unit_lat(level):
    return _dict_unit_lat_lon[level][0]()

def unit_lon(level):
    return _dict_unit_lat_lon[level][1]()

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
    Return:
        指定次の地域メッシュコード

    """

    if not 0 <= lat < 66.66:
        raise ValueError('the latitude is out of bound.')

    if not 100 <= lon < 180:
        raise ValueError('the longitude is out of bound.')

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
        ab = int(rem_lat_lv0(lat) / _unit_lat_lv1())
        cd = int(rem_lon_lv0(lon) / _unit_lon_lv1())
        return str(ab) + str(cd)

    def meshcode_40000(lat, lon):
        e = int(rem_lat_lv1(lat) / _unit_lat_40000())*2 + int(rem_lon_lv1(lon) / _unit_lon_40000()) + 1
        return meshcode_lv1(lat, lon) + str(e)

    def meshcode_20000(lat, lon):
        f = int(rem_lat_40000(lat) / _unit_lat_20000())*2 + int(rem_lon_40000(lon) / _unit_lon_20000()) + 1
        g = 5
        return meshcode_40000(lat, lon) + str(f) + str(g)

    def meshcode_16000(lat, lon):
        e = int(rem_lat_lv1(lat) / _unit_lat_16000())*2
        f = int(rem_lon_lv1(lon) / _unit_lon_16000())*2
        g = 7
        return meshcode_lv1(lat, lon) + str(e) + str(f) + str(g)

    def meshcode_lv2(lat, lon):
        e = int(rem_lat_lv1(lat) / _unit_lat_lv2())
        f = int(rem_lon_lv1(lon) / _unit_lon_lv2())
        return meshcode_lv1(lat, lon) + str(e) + str(f)

    def meshcode_8000(lat, lon):
        e = int(rem_lat_lv1(lat) / _unit_lat_8000())
        f = int(rem_lon_lv1(lon) / _unit_lon_8000())
        g = 6
        return meshcode_lv1(lat, lon) + str(e) + str(f) + str(g)

    def meshcode_5000(lat, lon):
        g = int(rem_lat_lv2(lat) / _unit_lat_5000())*2 + int(rem_lon_lv2(lon) / _unit_lon_5000()) + 1
        return meshcode_lv2(lat, lon) + str(g)

    def meshcode_4000(lat, lon):
        h = int(rem_lat_8000(lat) / _unit_lat_4000())*2 + int(rem_lon_8000(lon) / _unit_lon_4000()) + 1
        i = 7
        return meshcode_8000(lat, lon) + str(h) + str(i)

    def meshcode_2500(lat, lon):
        h = int(rem_lat_5000(lat) / _unit_lat_2500())*2 + int(rem_lon_5000(lon) / _unit_lon_2500()) + 1
        i = 6
        return meshcode_5000(lat, lon) + str(h) + str(i)

    def meshcode_2000(lat, lon):
        g = int(rem_lat_lv2(lat) / _unit_lat_2000())*2
        h = int(rem_lon_lv2(lon) / _unit_lon_2000())*2
        i = 5
        return meshcode_lv2(lat, lon) + str(g) + str(h) + str(i)

    def meshcode_lv3(lat, lon):
        g = int(rem_lat_lv2(lat) / _unit_lat_lv3())
        h = int(rem_lon_lv2(lon) / _unit_lon_lv3())
        return meshcode_lv2(lat, lon) + str(g) + str(h)

    def meshcode_lv4(lat, lon):
        i = int(rem_lat_lv3(lat) / _unit_lat_lv4())*2 + int(rem_lon_lv3(lon) / _unit_lon_lv4()) + 1
        return meshcode_lv3(lat, lon) + str(i)

    def meshcode_lv5(lat, lon):
        j = int(rem_lat_lv4(lat) / _unit_lat_lv5())*2 + int(rem_lon_lv4(lon) / _unit_lon_lv5()) + 1
        return meshcode_lv4(lat, lon) + str(j)

    def meshcode_lv6(lat, lon):
        k = int(rem_lat_lv5(lat) / _unit_lat_lv6())*2 + int(rem_lon_lv5(lon) / _unit_lon_lv6()) + 1
        return meshcode_lv5(lat, lon) + str(k)

    def meshcode_lv7(lat, lon):
        k = int(rem_lat_lv6(lat) / _unit_lat_lv7())*2 + int(rem_lon_lv6(lon) / _unit_lon_lv7()) + 1
        return meshcode_lv6(lat, lon) + str(k)

    def meshcode_lv8(lat, lon):
        k = int(rem_lat_lv7(lat) / _unit_lat_lv8())*2 + int(rem_lon_lv7(lon) / _unit_lon_lv8()) + 1
        return meshcode_lv7(lat, lon) + str(k)

    def meshcode_lv9(lat, lon):
        k = int(rem_lat_lv8(lat) / _unit_lat_lv9())*2 + int(rem_lon_lv8(lon) / _unit_lon_lv9()) + 1
        return meshcode_lv8(lat, lon) + str(k)

    def meshcode_lv10(lat, lon):
        k = int(rem_lat_lv9(lat) / _unit_lat_lv10())*2 + int(rem_lon_lv9(lon) / _unit_lon_lv10()) + 1
        return meshcode_lv9(lat, lon) + str(k)

    if level == 1:
        return astype(meshcode_lv1(lat, lon))

    if level == 40000:
        return astype(meshcode_40000(lat, lon))

    if level == 20000:
        return astype(meshcode_20000(lat, lon))

    if level == 16000:
        return astype(meshcode_16000(lat, lon))

    if level == 2:
        return astype(meshcode_lv2(lat, lon))

    if level == 8000:
        return astype(meshcode_8000(lat, lon))

    if level == 5000:
        return astype(meshcode_5000(lat, lon))

    if level == 4000:
        return astype(meshcode_4000(lat, lon))

    if level == 2500:
        return astype(meshcode_2500(lat, lon))

    if level == 2000:
        return astype(meshcode_2000(lat, lon))

    if level == 3:
        return astype(meshcode_lv3(lat, lon))

    if level == 4:
        return astype(meshcode_lv4(lat, lon))

    if level == 5:
        return astype(meshcode_lv5(lat, lon))

    if level == 6:
        return astype(meshcode_lv6(lat, lon))

    if level == 7:
        return astype(meshcode_lv7(lat, lon))

    if level == 8:
        return astype(meshcode_lv8(lat, lon))

    if level == 9:
        return astype(meshcode_lv9(lat, lon))

    if level == 10:
        return astype(meshcode_lv10(lat, lon))

    raise ValueError("the level is unsupported.")

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
    meshcode = str(meshcode)
    length = len(meshcode)
    if length == 4:
        return 1

    if length == 5:
        return 40000

    if length == 6:
        return 2

    if length == 7:
        if meshcode[6:7] in ['1','2','3','4']:
            return 5000

        if meshcode[6:7] == '6':
            return 8000

        if meshcode[6:7] == '5':
            return 20000

        if meshcode[6:7] == '7':
            return 16000

    if length == 8:
        return 3

    if length == 9:
        if meshcode[8:9] in ['1','2','3','4']:
            return 4

        if meshcode[8:9] == '5':
            return 2000

        if meshcode[8:9] == '6':
            return 2500

        if meshcode[8:9] == '7':
            return 4000

    if length == 10:
        if meshcode[9:10] in ['1','2','3','4']:
            return 5

    if length == 11:
        if meshcode[10:11] in ['1','2','3','4']:
            return 6

    if length == 12:
        if meshcode[11:12] in ['1','2','3','4']:
            return 7

    if length == 13:
        if meshcode[12:13] in ['1','2','3','4']:
            return 8

    if length == 14:
        if meshcode[13:14] in ['1','2','3','4']:
            return 9

    if length == 15:
        if meshcode[14:15] in ['1','2','3','4']:
            return 10

    return -1

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
    meshcode = str(meshcode)

    def mesh_cord(func_higher_cord, func_unit_cord, func_multiplier):
        return func_higher_cord() + func_unit_cord() * func_multiplier()

    lat_multiplier_lv = lambda: lat_multiplier

    lon_multiplier_lv = lambda: lon_multiplier

    lat_multiplier_lv1 = _functools.partial(
        lambda meshcode: int(meshcode[0:2]), meshcode=meshcode)

    lon_multiplier_lv1 = _functools.partial(
        lambda meshcode: int(meshcode[2:4]), meshcode=meshcode)

    lat_multiplier_40000 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[4:5])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_40000 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[4:5])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_20000 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[5:6])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_20000 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[5:6])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_16000 = _functools.partial(
        lambda meshcode: int(meshcode[4:5])/2, meshcode=meshcode)

    lon_multiplier_16000 = _functools.partial(
        lambda meshcode: int(meshcode[5:6])/2, meshcode=meshcode)

    lat_multiplier_lv2 = _functools.partial(
        lambda meshcode: int(meshcode[4:5]), meshcode=meshcode)

    lon_multiplier_lv2 = _functools.partial(
        lambda meshcode: int(meshcode[5:6]), meshcode=meshcode)

    lat_multiplier_8000 = _functools.partial(
        lambda meshcode: int(meshcode[4:5]), meshcode=meshcode)

    lon_multiplier_8000 = _functools.partial(
        lambda meshcode: int(meshcode[5:6]), meshcode=meshcode)

    lat_multiplier_5000 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[6:7])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_5000 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[6:7])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_4000 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[7:8])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_4000 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[7:8])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_2500 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[7:8])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_2500 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[7:8])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_2000 = _functools.partial(
        lambda meshcode: int(meshcode[6:7])/2, meshcode=meshcode)

    lon_multiplier_2000 = _functools.partial(
        lambda meshcode: int(meshcode[7:8])/2, meshcode=meshcode)

    lat_multiplier_lv3 = _functools.partial(
        lambda meshcode: int(meshcode[6:7]), meshcode=meshcode)

    lon_multiplier_lv3 = _functools.partial(
        lambda meshcode: int(meshcode[7:8]), meshcode=meshcode)

    lat_multiplier_lv4 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[8:9])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_lv4 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[8:9])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_lv5 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[9:10])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_lv5 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[9:10])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_lv6 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[10:11])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_lv6 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[10:11])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_lv7 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[11:12])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_lv7 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[11:12])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_lv8 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[12:13])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_lv8 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[12:13])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_lv9 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[13:14])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_lv9 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[13:14])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)

    lat_multiplier_lv10 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[14:15])-1)[2:].zfill(2)[0:1]), meshcode=meshcode)

    lon_multiplier_lv10 = _functools.partial(
        lambda meshcode: int(bin(int(meshcode[14:15])-1)[2:].zfill(2)[1:2]), meshcode=meshcode)


    mesh_lv1_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=lambda: 0,
        func_unit_cord=_unit_lat_lv1,
        func_multiplier=lat_multiplier_lv1)

    mesh_lv1_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=lambda: 100,
        func_unit_cord=_unit_lon_lv1,
        func_multiplier=lon_multiplier_lv1)

    mesh_40000_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lat,
        func_unit_cord=_unit_lat_40000,
        func_multiplier=lat_multiplier_40000)

    mesh_40000_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lon,
        func_unit_cord=_unit_lon_40000,
        func_multiplier=lon_multiplier_40000)

    mesh_20000_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_40000_default_lat,
        func_unit_cord=_unit_lat_20000,
        func_multiplier=lat_multiplier_20000)

    mesh_20000_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_40000_default_lon,
        func_unit_cord=_unit_lon_20000,
        func_multiplier=lon_multiplier_20000)

    mesh_16000_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lat,
        func_unit_cord=_unit_lat_16000,
        func_multiplier=lat_multiplier_16000)

    mesh_16000_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lon,
        func_unit_cord=_unit_lon_16000,
        func_multiplier=lon_multiplier_16000)

    mesh_lv2_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lat,
        func_unit_cord=_unit_lat_lv2,
        func_multiplier=lat_multiplier_lv2)

    mesh_lv2_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lon,
        func_unit_cord=_unit_lon_lv2,
        func_multiplier=lon_multiplier_lv2)

    mesh_8000_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lat,
        func_unit_cord=_unit_lat_8000,
        func_multiplier=lat_multiplier_8000)

    mesh_8000_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lon,
        func_unit_cord=_unit_lon_8000,
        func_multiplier=lon_multiplier_8000)

    mesh_5000_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv2_default_lat,
        func_unit_cord=_unit_lat_5000,
        func_multiplier=lat_multiplier_5000)

    mesh_5000_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv2_default_lon,
        func_unit_cord=_unit_lon_5000,
        func_multiplier=lon_multiplier_5000)

    mesh_4000_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_8000_default_lat,
        func_unit_cord=_unit_lat_4000,
        func_multiplier=lat_multiplier_4000)

    mesh_4000_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_8000_default_lon,
        func_unit_cord=_unit_lon_4000,
        func_multiplier=lon_multiplier_4000)

    mesh_2500_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_5000_default_lat,
        func_unit_cord=_unit_lat_2500,
        func_multiplier=lat_multiplier_2500)

    mesh_2500_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_5000_default_lon,
        func_unit_cord=_unit_lon_2500,
        func_multiplier=lon_multiplier_2500)

    mesh_2000_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv2_default_lat,
        func_unit_cord=_unit_lat_2000,
        func_multiplier=lat_multiplier_2000)

    mesh_2000_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv2_default_lon,
        func_unit_cord=_unit_lon_2000,
        func_multiplier=lon_multiplier_2000)

    mesh_lv3_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv2_default_lat,
        func_unit_cord=_unit_lat_lv3,
        func_multiplier=lat_multiplier_lv3)

    mesh_lv3_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv2_default_lon,
        func_unit_cord=_unit_lon_lv3,
        func_multiplier=lon_multiplier_lv3)

    mesh_lv4_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv3_default_lat,
        func_unit_cord=_unit_lat_lv4,
        func_multiplier=lat_multiplier_lv4)

    mesh_lv4_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv3_default_lon,
        func_unit_cord=_unit_lon_lv4,
        func_multiplier=lon_multiplier_lv4)

    mesh_lv5_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv4_default_lat,
        func_unit_cord=_unit_lat_lv5,
        func_multiplier=lat_multiplier_lv5)

    mesh_lv5_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv4_default_lon,
        func_unit_cord=_unit_lon_lv5,
        func_multiplier=lon_multiplier_lv5)

    mesh_lv6_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv5_default_lat,
        func_unit_cord=_unit_lat_lv6,
        func_multiplier=lat_multiplier_lv6)

    mesh_lv6_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv5_default_lon,
        func_unit_cord=_unit_lon_lv6,
        func_multiplier=lon_multiplier_lv6)

    mesh_lv7_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv6_default_lat,
        func_unit_cord=_unit_lat_lv7,
        func_multiplier=lat_multiplier_lv7)

    mesh_lv7_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv6_default_lon,
        func_unit_cord=_unit_lon_lv7,
        func_multiplier=lon_multiplier_lv7)

    mesh_lv8_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv7_default_lat,
        func_unit_cord=_unit_lat_lv8,
        func_multiplier=lat_multiplier_lv8)

    mesh_lv8_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv7_default_lon,
        func_unit_cord=_unit_lon_lv8,
        func_multiplier=lon_multiplier_lv8)

    mesh_lv9_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv8_default_lat,
        func_unit_cord=_unit_lat_lv9,
        func_multiplier=lat_multiplier_lv9)

    mesh_lv9_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv8_default_lon,
        func_unit_cord=_unit_lon_lv9,
        func_multiplier=lon_multiplier_lv9)

    mesh_lv10_default_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv9_default_lat,
        func_unit_cord=_unit_lat_lv10,
        func_multiplier=lat_multiplier_lv10)

    mesh_lv10_default_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv9_default_lon,
        func_unit_cord=_unit_lon_lv10,
        func_multiplier=lon_multiplier_lv10)

    mesh_lv1_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lat,
        func_unit_cord=_unit_lat_lv1,
        func_multiplier=lat_multiplier_lv)

    mesh_lv1_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv1_default_lon,
        func_unit_cord=_unit_lon_lv1,
        func_multiplier=lon_multiplier_lv)

    mesh_40000_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_40000_default_lat,
        func_unit_cord=_unit_lat_40000,
        func_multiplier=lat_multiplier_lv)

    mesh_40000_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_40000_default_lon,
        func_unit_cord=_unit_lon_40000,
        func_multiplier=lon_multiplier_lv)

    mesh_20000_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_20000_default_lat,
        func_unit_cord=_unit_lat_20000,
        func_multiplier=lat_multiplier_lv)

    mesh_20000_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_20000_default_lon,
        func_unit_cord=_unit_lon_20000,
        func_multiplier=lon_multiplier_lv)

    mesh_16000_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_16000_default_lat,
        func_unit_cord=_unit_lat_16000,
        func_multiplier=lat_multiplier_lv)

    mesh_16000_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_16000_default_lon,
        func_unit_cord=_unit_lon_16000,
        func_multiplier=lon_multiplier_lv)

    mesh_lv2_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv2_default_lat,
        func_unit_cord=_unit_lat_lv2,
        func_multiplier=lat_multiplier_lv)

    mesh_lv2_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv2_default_lon,
        func_unit_cord=_unit_lon_lv2,
        func_multiplier=lon_multiplier_lv)

    mesh_8000_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_8000_default_lat,
        func_unit_cord=_unit_lat_8000,
        func_multiplier=lat_multiplier_lv)

    mesh_8000_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_8000_default_lon,
        func_unit_cord=_unit_lon_8000,
        func_multiplier=lon_multiplier_lv)

    mesh_5000_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_5000_default_lat,
        func_unit_cord=_unit_lat_5000,
        func_multiplier=lat_multiplier_lv)

    mesh_5000_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_5000_default_lon,
        func_unit_cord=_unit_lon_5000,
        func_multiplier=lon_multiplier_lv)

    mesh_4000_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_4000_default_lat,
        func_unit_cord=_unit_lat_4000,
        func_multiplier=lat_multiplier_lv)

    mesh_4000_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_4000_default_lon,
        func_unit_cord=_unit_lon_4000,
        func_multiplier=lon_multiplier_lv)

    mesh_2500_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_2500_default_lat,
        func_unit_cord=_unit_lat_2500,
        func_multiplier=lat_multiplier_lv)

    mesh_2500_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_2500_default_lon,
        func_unit_cord=_unit_lon_2500,
        func_multiplier=lon_multiplier_lv)

    mesh_2000_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_2000_default_lat,
        func_unit_cord=_unit_lat_2000,
        func_multiplier=lat_multiplier_lv)

    mesh_2000_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_2000_default_lon,
        func_unit_cord=_unit_lon_2000,
        func_multiplier=lon_multiplier_lv)

    mesh_lv3_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv3_default_lat,
        func_unit_cord=_unit_lat_lv3,
        func_multiplier=lat_multiplier_lv)

    mesh_lv3_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv3_default_lon,
        func_unit_cord=_unit_lon_lv3,
        func_multiplier=lon_multiplier_lv)

    mesh_lv4_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv4_default_lat,
        func_unit_cord=_unit_lat_lv4,
        func_multiplier=lat_multiplier_lv)

    mesh_lv4_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv4_default_lon,
        func_unit_cord=_unit_lon_lv4,
        func_multiplier=lon_multiplier_lv)

    mesh_lv5_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv5_default_lat,
        func_unit_cord=_unit_lat_lv5,
        func_multiplier=lat_multiplier_lv)

    mesh_lv5_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv5_default_lon,
        func_unit_cord=_unit_lon_lv5,
        func_multiplier=lon_multiplier_lv)

    mesh_lv6_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv6_default_lat,
        func_unit_cord=_unit_lat_lv6,
        func_multiplier=lat_multiplier_lv)

    mesh_lv6_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv6_default_lon,
        func_unit_cord=_unit_lon_lv6,
        func_multiplier=lon_multiplier_lv)

    mesh_lv7_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv7_default_lat,
        func_unit_cord=_unit_lat_lv7,
        func_multiplier=lat_multiplier_lv)

    mesh_lv7_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv7_default_lon,
        func_unit_cord=_unit_lon_lv7,
        func_multiplier=lon_multiplier_lv)

    mesh_lv8_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv8_default_lat,
        func_unit_cord=_unit_lat_lv8,
        func_multiplier=lat_multiplier_lv)

    mesh_lv8_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv8_default_lon,
        func_unit_cord=_unit_lon_lv8,
        func_multiplier=lon_multiplier_lv)

    mesh_lv9_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv9_default_lat,
        func_unit_cord=_unit_lat_lv9,
        func_multiplier=lat_multiplier_lv)

    mesh_lv9_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv9_default_lon,
        func_unit_cord=_unit_lon_lv9,
        func_multiplier=lon_multiplier_lv)

    mesh_lv10_lat = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv10_default_lat,
        func_unit_cord=_unit_lat_lv10,
        func_multiplier=lat_multiplier_lv)

    mesh_lv10_lon = _functools.partial(
        mesh_cord,
        func_higher_cord=mesh_lv10_default_lon,
        func_unit_cord=_unit_lon_lv10,
        func_multiplier=lon_multiplier_lv)

    level = to_meshlevel(meshcode)

    if level == 1:
        return mesh_lv1_lat(), mesh_lv1_lon()

    if level == 40000:
        return mesh_40000_lat(), mesh_40000_lon()

    if level == 20000:
        return mesh_20000_lat(), mesh_20000_lon()

    if level == 16000:
        return mesh_16000_lat(), mesh_16000_lon()

    if level == 2:
        return mesh_lv2_lat(), mesh_lv2_lon()

    if level == 8000:
        return mesh_8000_lat(), mesh_8000_lon()

    if level == 5000:
        return mesh_5000_lat(), mesh_5000_lon()

    if level == 4000:
        return mesh_4000_lat(), mesh_4000_lon()

    if level == 2500:
        return mesh_2500_lat(), mesh_2500_lon()

    if level == 2000:
        return mesh_2000_lat(), mesh_2000_lon()

    if level == 3:
        return mesh_lv3_lat(), mesh_lv3_lon()

    if level == 4:
        return mesh_lv4_lat(), mesh_lv4_lon()

    if level == 5:
        return mesh_lv5_lat(), mesh_lv5_lon()

    if level == 6:
        return mesh_lv6_lat(), mesh_lv6_lon()

    if level == 7:
        return mesh_lv7_lat(), mesh_lv7_lon()

    if level == 8:
        return mesh_lv8_lat(), mesh_lv8_lon()

    if level == 9:
        return mesh_lv9_lat(), mesh_lv9_lon()

    if level == 10:
        return mesh_lv10_lat(), mesh_lv10_lon()

    raise ValueError("the level is unsupported.")

def _make_envelope(lat_s, lon_w, lat_n, lon_e, to_level, astype):
    to_unit_lat = unit_lat(to_level)
    to_unit_lon = unit_lon(to_level)
    to_lats = _np.arange(lat_s, lat_n, to_unit_lat)
    to_lons = _np.arange(lon_w, lon_e, to_unit_lon)

    for to_lat in to_lats:
        for to_lon in to_lons:
            yield to_meshcode(to_lat, to_lon, to_level, astype)

def to_envelope(meshcode_sw, meshcode_ne):
    level_sw = to_meshlevel(meshcode_sw)
    level_ne = to_meshlevel(meshcode_ne)
    if level_sw != level_ne:
        raise ValueError("the level must be the same for meshcode_sw and meshcode_ne.")

    mergin_lat = 0.5
    mergin_lon = 0.5

    lat_s, lon_w = to_meshpoint(meshcode_sw, 0+mergin_lat, 0+mergin_lon)
    lat_n, lon_e = to_meshpoint(meshcode_ne, 1, 1)

    return _make_envelope(lat_s, lon_w, lat_n, lon_e, level_sw, type(meshcode_sw))

def to_intersects(meshcode, to_level):
    to_unit_lat = unit_lat(to_level)
    to_unit_lon = unit_lon(to_level)

    from_level = to_meshlevel(meshcode)
    from_unit_lat = unit_lat(from_level)
    from_unit_lon = unit_lon(from_level)

    mergin_lat = (to_unit_lat/from_unit_lat)/2 if to_unit_lat <= from_unit_lat else 0.5
    mergin_lon = (to_unit_lon/from_unit_lon)/2 if to_unit_lon <= from_unit_lon else 0.5

    from_lat_s, from_lon_w = to_meshpoint(meshcode, 0+mergin_lat, 0+mergin_lon)
    from_lat_n, from_lon_e = to_meshpoint(meshcode, 1, 1)

    return _make_envelope(from_lat_s, from_lon_w, from_lat_n, from_lon_e, to_level, type(meshcode))

def is_nonstandard(level):
    return level in _nonstandard_levels