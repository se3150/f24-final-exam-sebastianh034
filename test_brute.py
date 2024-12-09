import pytest
from pytest import fixture
import string
import time
from brute import Brute

@fixture
def simple_brute():
    return Brute("test123")

@fixture
def complex_brute():
    return Brute("Complex!@#$123")

def describe_brute_force():
    def describe_initialization():
        def it_creates_correct_length_hash(simple_brute):
            assert len(simple_brute.target) == 128
            
        def it_creates_valid_hex_hash(simple_brute):
            assert all(c in string.hexdigits for c in simple_brute.target)

    def describe_hashing():
        def it_produces_consistent_hashes(simple_brute):
            hash1 = simple_brute.hash("password")
            hash2 = simple_brute.hash("password")
            assert hash1 == hash2

        def it_produces_unique_hashes_for_different_inputs(simple_brute):
            hash1 = simple_brute.hash("password1")
            hash2 = simple_brute.hash("password2")
            assert hash1 != hash2

    def describe_random_guessing():
        def it_generates_valid_length_guesses(simple_brute):
            for _ in range(100):
                guess = simple_brute.randomGuess()
                assert 1 <= len(guess) <= 8

    def describe_brute_force_attempts():
        def describe_single_attempts():
            def it_succeeds_with_correct_password(simple_brute):
                assert simple_brute.bruteOnce("test123") is True

            def it_fails_with_wrong_password(simple_brute):
                assert simple_brute.bruteOnce("wrong") is False

        def describe_multiple_attempts():
            def it_succeeds_with_simple_password():
                brute = Brute("a")
                result = brute.bruteMany(limit=100000)
                assert result > 0

            def it_times_out_with_complex_password(complex_brute):
                result = complex_brute.bruteMany(limit=100)
                assert result == -1

            @pytest.mark.parametrize("limit,expected", [
                (0, -1),
                (1, -1),
                (100, "number")
            ])
            def it_validates_attempt_limits(simple_brute, limit, expected):
                result = simple_brute.bruteMany(limit=limit)
                if expected == "number":
                    assert isinstance(result, (float, int))
                else:
                    assert result == expected