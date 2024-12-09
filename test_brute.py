import pytest
import string
import time
from brute import Brute

@pytest.fixture
def simple_brute():
    return Brute("test123")

@pytest.fixture
def complex_brute():
    return Brute("Complex!@#$123")

class TestBruteForce:
    def test_initialization(self, simple_brute):
        assert len(simple_brute.target) == 128  
        assert all(c in string.hexdigits for c in simple_brute.target)

    def test_hash_consistency(self, simple_brute):
        hash1 = simple_brute.hash("password")
        hash2 = simple_brute.hash("password")
        assert hash1 == hash2

    def test_hash_uniqueness(self, simple_brute):
        hash1 = simple_brute.hash("password1")
        hash2 = simple_brute.hash("password2")
        assert hash1 != hash2

    def test_random_guess_length(self, simple_brute):
        for _ in range(100):
            guess = simple_brute.randomGuess()
            assert 1 <= len(guess) <= 8


    def test_brute_once_success(self, simple_brute):
        assert simple_brute.bruteOnce("test123") is True

    def test_brute_once_failure(self, simple_brute):
        assert simple_brute.bruteOnce("wrong") is False

    def test_brute_many_simple(self):
        brute = Brute("a")
        result = brute.bruteMany(limit=100000)
        assert result > 0 

    def test_brute_many_timeout(self, complex_brute):
        result = complex_brute.bruteMany(limit=100)
        assert result == -1 

    def test_limit_validation(self, simple_brute):
        """Test bruteMany with various limits"""
        assert simple_brute.bruteMany(limit=0) == -1
        assert simple_brute.bruteMany(limit=1) == -1
        assert isinstance(simple_brute.bruteMany(limit=100), (float, int))