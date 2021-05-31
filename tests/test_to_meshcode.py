# -*- coding: utf-8 -*-
import numpy as np
from nose.tools import raises, timed, eq_
from jismesh import utils as ju

# テストデータ

## 東京タワー緯度 (度) 経度 (度) 世界測地系
_lat_tokyo_tower = 35.658581
_lon_tokyo_tower = 139.745433

## 京都タワー緯度 (度) 経度 (度)世界測地系
_lat_kyoto_tower = 34.987574
_lon_kyoto_tower = 135.759363

def _data_scalar():
    return [
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':1},        '5339'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':40000},    '53392'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':20000},    '5339235'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':16000},    '5339467'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':2},        '533935'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':8000},     '5339476'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':5000},     '5339354'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':4000},     '533947637'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':2500},     '533935446'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':2000},     '533935885'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':3},        '53393599'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':4},        '533935992'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':5},        '5339359921'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':6},        '53393599212'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':7},        '533935992121'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':8},        '5339359921211'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':9},        '53393599212113'),
        ({'lat':_lat_tokyo_tower, 'lon':_lon_tokyo_tower, 'level':10},       '533935992121134'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':1},        '5235'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':40000},    '52352'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':20000},    '5235245'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':16000},    '5235467'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':2},        '523536'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':8000},     '5235476'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':5000},     '5235363'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':4000},     '523547647'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':2500},     '523536336'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':2000},     '523536805'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':3},        '52353680'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':4},        '523536804'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':5},        '5235368041'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':6},        '52353680412'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':7},        '523536804122'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':8},        '5235368041222'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':9},        '52353680412222'),
        ({'lat':_lat_kyoto_tower, 'lon':_lon_kyoto_tower, 'level':10},       '523536804122224'),
    ]

def _data_vector(num_elements=10):
    return [
        ({'lat':np.array([_lat_tokyo_tower]*num_elements), 'lon':np.array([_lon_tokyo_tower]*num_elements), 'level':1},         np.array(['5339']*num_elements)),
        ({'lat':np.array([_lat_tokyo_tower]*num_elements), 'lon':np.array([_lon_tokyo_tower]*num_elements), 'level':40000},     np.array(['53392']*num_elements)),
        ({'lat':np.array([_lat_tokyo_tower]*num_elements), 'lon':_lon_tokyo_tower, 'level':1},                                  np.array(['5339']*num_elements)),
        ({'lat':np.array([_lat_tokyo_tower]*num_elements), 'lon':_lon_tokyo_tower, 'level':40000},                              np.array(['53392']*num_elements)),
        ({'lat':_lat_tokyo_tower, 'lon':np.array([_lon_tokyo_tower]*num_elements), 'level':1},                                  np.array(['5339']*num_elements)),
        ({'lat':_lat_tokyo_tower, 'lon':np.array([_lon_tokyo_tower]*num_elements), 'level':40000},                              np.array(['53392']*num_elements)),
    ]

def _data_performance(num_elements=1000000):
    return [
        ({'lat':np.array([_lat_tokyo_tower]*num_elements), 'lon':np.array([_lon_tokyo_tower]*num_elements), 'astype':np.int64, 'level':6}, np.array([53393599212]*num_elements)),
    ]

# テストヘルパ
def _eq_scalars(actual, expect, input):
    eq_(actual, expect, msg='{} as {} but expectes {} as {} when {} is given.'.format(actual, type(actual), expect, type(expect), input))

def _eq_vectors(actual, expect, input):
    np.testing.assert_array_equal(actual, expect, err_msg='{} as {} but expectes {} as {} when {} is given.'.format(actual, type(actual), expect, type(expect), input))

def _eq_test_helper(expect, input, eq, target=ju.to_meshcode):
    actual = target(**input)
    eq(actual, expect, input)

# テストケース
@raises(ValueError)
def test_error_unsupported_level():
    ju.to_meshcode(lat=_lat_tokyo_tower, lon=_lon_tokyo_tower, level=0)

@raises(ValueError)
def test_error_scalar_invalid_latitude_min():
    ju.to_meshcode(lat=-0.1, lon=_lon_tokyo_tower, level=1)

@raises(ValueError)
def test_error_scalar_invalid_latitude_max():
    ju.to_meshcode(lat=66.66, lon=_lon_tokyo_tower, level=1)

@raises(ValueError)
def test_error_scalar_invalid_longitude_min():
    ju.to_meshcode(lat=_lat_tokyo_tower, lon=99.99, level=1)

@raises(ValueError)
def test_error_scalar_invalid_longitude_max():
    ju.to_meshcode(lat=_lat_tokyo_tower, lon=180, level=1)

@raises(ValueError)
def test_error_vector_invalid_latitude_min():
    ju.to_meshcode(lat=np.array([-0.1]*10), lon=_lon_tokyo_tower, level=1)

@raises(ValueError)
def test_error_vector_invalid_latitude_max():
    ju.to_meshcode(lat=np.array([66.66]*10), lon=_lon_tokyo_tower, level=1)

@raises(ValueError)
def test_error_vector_invalid_longitude_min():
    ju.to_meshcode(lat=_lat_tokyo_tower, lon=np.array([99.99]*10), level=1)

@raises(ValueError)
def test_error_vector_invalid_longitude_max():
    ju.to_meshcode(lat=_lat_tokyo_tower, lon=np.array([180]*10), level=1)

def test_normal_scalar_default():
    for input, expect in _data_scalar():
        _eq_test_helper(expect, input, eq=_eq_scalars)

def test_normal_scalar_astype_str():
    for input, expect in _data_scalar():
        input['astype'] = str
        expect = str(expect)
        _eq_test_helper(expect, input, eq=_eq_scalars)

def test_normal_scalar_astype_int():
    for input, expect in _data_scalar():
        input['astype'] = int
        expect = int(expect)
        _eq_test_helper(expect, input, eq=_eq_scalars)

def test_normal_scalar_astype_numpyint64():
    for input, expect in _data_scalar():
        input['astype'] = np.int64
        expect = np.int64(expect)
        _eq_test_helper(expect, input, eq=_eq_scalars)

def test_normal_vector_default():
    for input, expect in _data_vector():
        _eq_test_helper(expect, input, eq=_eq_vectors)

def test_normal_vector_astype_str():
    for input, expect in _data_vector():
        input['astype'] = str
        expect = expect.astype(str)
        _eq_test_helper(expect, input, eq=_eq_vectors)

def test_normal_vector_astype_int():
    for input, expect in _data_vector():
        input['astype'] = int
        expect = expect.astype(int)
        _eq_test_helper(expect, input, eq=_eq_vectors)

def test_normal_vector_astype_numpyint64():
    for input, expect in _data_vector():
        input['astype'] = np.int64
        expect = expect.astype(np.int64)
        _eq_test_helper(expect, input, eq=_eq_vectors)

@timed(2)
def test_performance_vector():
    for input, expect in _data_performance():
        _eq_test_helper(expect, input, eq=_eq_vectors)
