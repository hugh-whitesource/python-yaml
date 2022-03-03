#!/usr/bin/env python
# coding: utf-8
# pylint: disable=C0111
# pylint: disable=R0904
# pylint: disable=W0621
"""
Run unit tests for YAML file processing example.
"""

import os

import pytest

from employees.employees import Employees


@pytest.fixture
def test_file():
    return "tests/test.yaml"


@pytest.fixture
def employees(test_file):
    return Employees(test_file)


def test_can_read_file(test_file):
    test_file = os.path.join(os.getcwd(), test_file)
    assert os.access(test_file, os.R_OK)


def test_load_infile(test_file):
    with open(test_file, "r", encoding="UTF-8") as _fh:
        assert Employees(_fh)


def test_dump(employees):
    dump = employees.dump()
    assert "frank:" in dump
    assert "jo:" in dump


def test_name(employees):
    assert employees.get_name(3) == "frank"
    assert employees.get_name(4) == "jo"


def test_by_name(employees):
    assert employees.get_by_name("frank") == 440000
    assert employees.get_by_name("jo") == 560000


def test_by_turnover_by_id(employees):
    assert employees.get_by_id(3) == 440000
    assert employees.get_by_id(4) == 560000


def test_for_name_by_year(employees):
    assert employees.get_for_name_by_year(name="frank", year=2011) == 100000
    assert employees.get_for_name_by_year(name="frank", year=2012) == 140000
    assert employees.get_for_name_by_year(name="frank", year=2013) == 200000
    assert employees.get_for_name_by_year(name="jo", year=2012) == 130000
    assert employees.get_for_name_by_year(name="jo", year=2013) == 220000
    assert employees.get_for_name_by_year(name="jo", year=2014) == 210000


def test_by_year(employees):
    assert employees.get_by_year(2011) == 100000
    assert employees.get_by_year(2012) == 270000
    assert employees.get_by_year(2013) == 420000
    assert employees.get_by_year(2014) == 210000


def test_list_by_id(employees):
    turnovers = list(employees.list_by_id(3))
    assert len(turnovers) == 3
    assert turnovers == [100000, 140000, 200000]
    assert 220000 not in turnovers


def test_list_by_name(employees):
    turnovers = list(employees.list_by_name("frank"))
    assert len(turnovers) == 3
    assert turnovers == [100000, 140000, 200000]
    assert 220000 not in turnovers


def test_list_by_year(employees):
    turnovers = list(employees.list_by_year(2013))
    assert len(turnovers) == 2
    assert turnovers == [200000, 220000]
    assert 2013 not in turnovers


def test_bad_id(employees):
    assert not employees.get_by_id(999)


def test_bad_by_id(employees):
    assert not employees.get_by_id(1)


def test_bad_by_name_(employees):
    assert not employees.get_by_name("badname")


def test_bad_by_year(employees):
    assert employees.get_by_year(1999) == 0


def test_bad_for_name_by_year(employees):
    assert not employees.get_for_name_by_year("frank", 1999)
    assert not employees.get_for_name_by_year("jo", 1999)
    assert not employees.get_for_name_by_year("badname", 2011)
    assert not employees.get_for_name_by_year("badname", 2012)
    assert not employees.get_for_name_by_year("badname", 2013)
    assert not employees.get_for_name_by_year("badname", 2014)


def test_bad_list_by_id(employees):
    assert not employees.list_by_id(1)


def test_bad_list_by_name(employees):
    assert not employees.list_by_name("badname")


def test_bad_list_by_year(employees):
    assert not employees.list_by_year(1999)
