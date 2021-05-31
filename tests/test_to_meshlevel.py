# -*- coding: utf-8 -*-
import numpy as np
from nose.tools import raises, timed, eq_
from jismesh import utils as ju

def _data_scalar():
    return [
        ({'meshcode': 5339},            1),
        ({'meshcode': 53392},           40000),
        ({'meshcode': 5339235},         20000),
        ({'meshcode': 5339467},         16000),
        ({'meshcode': 533935},          2),
        ({'meshcode': 5339476},         8000),
        ({'meshcode': 5339354},         5000),
        ({'meshcode': 533947637},       4000),
        ({'meshcode': 533935446},       2500),
        ({'meshcode': 533935885},       2000),
        ({'meshcode': 53393599},        3),
        ({'meshcode': 533935992},       4),
        ({'meshcode': 5339359921},      5),
        ({'meshcode': 53393599212},     6),
        ({'meshcode': 533935992121},    7),
        ({'meshcode': 5339359921211},   8),
        ({'meshcode': 53393599212113},  9),
        ({'meshcode': 533935992121134}, 10),
        ({'meshcode': 5235},            1),
        ({'meshcode': 52352},           40000),
        ({'meshcode': 5235245},         20000),
        ({'meshcode': 5235467},         16000),
        ({'meshcode': 523536},          2),
        ({'meshcode': 5235476},         8000),
        ({'meshcode': 5235363},         5000),
        ({'meshcode': 523547647},       4000),
        ({'meshcode': 523536336},       2500),
        ({'meshcode': 523536805},       2000),
        ({'meshcode': 52353680},        3),
        ({'meshcode': 523536804},       4),
        ({'meshcode': 5235368041},      5),
        ({'meshcode': 52353680412},     6),
        ({'meshcode': 523536804122},    7),
        ({'meshcode': 5235368041222},   8),
        ({'meshcode': 52353680412222},  9),
        ({'meshcode': 523536804122224}, 10),
        ({'meshcode': 5},               -1),
    ]

def _data_vector(num_elements=10):
    return [
        ({'meshcode': np.array([53393599212]*num_elements)},     np.array([6]*num_elements)),
    ]

# テストヘルパ
def _eq_scalars(actual, expect, input):
    eq_(actual, expect, msg='{} as {} but expectes {} as {} when {} is given.'.format(actual, type(actual), expect, type(expect), input))

def _eq_vectors(actual, expect, input):
    np.testing.assert_array_equal(actual, expect, err_msg='{} as {} but expectes {} as {} when {} is given.'.format(actual, type(actual), expect, type(expect), input))

def _eq_test_helper(expect, input, eq, target=ju.to_meshlevel):
    actual = target(**input)
    eq(actual, expect, input)

def test_normal_scalar_default():
    for input, expect in _data_scalar():
        _eq_test_helper(expect, input, eq=_eq_scalars)

def test_normal_vector_default():
    for input, expect in _data_vector():
        _eq_test_helper(expect, input, eq=_eq_vectors)

@timed(2)
def test_performance_vector():
    for input, expect in _data_vector(num_elements=1000000):
        _eq_test_helper(expect, input, eq=_eq_vectors)
