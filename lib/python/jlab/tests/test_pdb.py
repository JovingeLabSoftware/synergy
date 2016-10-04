import os
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
from ..jlpdb import Splitter


class TestSplitter(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_init(self):
        a = Splitter()
        assert(isinstance(a, Splitter))

    def test_splitter(self):
        a = Splitter("tests")
        p = os.path.join(os.getcwd(), "tests/test.pdb")
        a.make_pdb(p, "A", True)
        assert True
