import pytest
from brute import Brute

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce(self, attempt)):
        
        assert 

    def describe_bruteMany():
        # write your test cases here
        pass



        