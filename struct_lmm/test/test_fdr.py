from numpy import array
from numpy.testing import assert_allclose

from struct_lmm import fdr_bh


def test_fdr():
    pv = array([0.1, 0.5, 0.9])
    qv = fdr_bh(pv)
    assert_allclose(qv, [0.3, 0.75, 0.9])
