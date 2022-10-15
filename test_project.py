import pytest

import project
from project import Person


# data for testing person aged < 56 years
@pytest.fixture
def p1() -> Person:
    p1 = Person()
    setattr(p1, 'name', 'Alex')
    setattr(p1, 'age', 53)
    setattr(p1, 'initial_test', 30)
    setattr(p1, 'w2d3_test1', 56)
    setattr(p1, 'w4d3_test2', 67)
    setattr(p1, 'w5d3_test3', 97)
    setattr(p1, 'final_test', 126)
    p1.calculate_rank('initial_test')
    p1.calculate_rank('test1')
    p1.calculate_rank('test2')
    p1.calculate_rank('test3')
    p1.calculate_rank('final_test')
    return p1


# data for testing person aged < 40 years
@pytest.fixture
def p2() -> Person:
    p2 = Person()
    setattr(p2, 'name', 'Simon')
    setattr(p2, 'age', 21)
    setattr(p2, 'initial_test', 15)
    setattr(p2, 'w2d3_test1', 56)
    setattr(p2, 'w4d3_test2', 98)
    setattr(p2, 'w5d3_test3', 100)
    setattr(p2, 'final_test', 151)
    p2.calculate_rank('initial_test')
    p2.calculate_rank('test1')
    p2.calculate_rank('test2')
    p2.calculate_rank('test3')
    p2.calculate_rank('final_test')
    return p2


# data for testing person aged > 56 years
@pytest.fixture
def p3() -> Person:
    p3 = Person()
    setattr(p3, 'name', 'Rachel')
    setattr(p3, 'age', 72)
    setattr(p3, 'initial_test', 4)
    setattr(p3, 'w2d3_test1', 12)
    setattr(p3, 'w4d3_test2', 34)
    setattr(p3, 'w5d3_test3', 45)
    setattr(p3, 'final_test', 93)
    p3.calculate_rank('initial_test')
    p3.calculate_rank('test1')
    p3.calculate_rank('test2')
    p3.calculate_rank('test3')
    p3.calculate_rank('final_test')
    return p3


#  tests the import works, it's callable, and can be called.
def test_init(p1):
    assert 'Alex' == p1.name
    assert 53 == p1.age
    assert 30 == p1.initial_test
    assert 56 == p1.w2d3_test1
    assert 67 == p1.w4d3_test2
    assert 97 == p1.w5d3_test3
    assert 126 == p1.final_test


# calculate rank for Person instance < 56 years
def test_calculate_rank_age_under_56(p1):
    assert 4 == p1.initial_test_rank
    assert 5 == p1.test1_rank
    assert 5 == p1.test2_rank
    assert 6 == p1.test3_rank
    assert 7 == p1.final_test_rank


# calculate rank for Person instance < 40 years
def test_calculate_rank_age_under_40(p2):
    assert 3 == p2.initial_test_rank
    assert 5 == p2.test1_rank
    assert 5 == p2.test2_rank
    assert 6 == p2.test3_rank
    assert 7 == p2.final_test_rank


# calculate rank for Person instance > 55 years
def test_calculate_rank_age_over_55(p3):
    assert 1 == p3.initial_test_rank
    assert 3 == p3.test1_rank
    assert 4 == p3.test2_rank
    assert 5 == p3.test3_rank
    assert 6 == p3.final_test_rank


def test_name():
    assert project.name() == ''


def test_age():
    assert project.age() == 0


def test_initial_test_rank(p1):
    assert project.initial_test_rank() == 0
