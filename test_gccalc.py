#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:58:00 2022

@author: samuel
"""

from gccalc import calc_gc_content
import pytest

def test_mid_gc():
    seq = "GCGCGCGCGCTATATATATA"
    exp = 50.0
    obs = calc_gc_content(seq)
    assert obs == exp
    
def test_high_gc():
    seq = "GCGCGCGCGCGCGCGCGCGC"
    exp = 100.0
    obs = calc_gc_content(seq)
    assert obs == exp
    
def test_low_gc():
    seq = "TATATATATATATATATATA"
    exp = 0.0
    obs = calc_gc_content(seq)
    assert obs == exp

def test_empty_seq():
    seq = ""
    exp = 0.0
    obs = calc_gc_content(seq)
    assert obs == exp

@pytest.mark.skip(reason="Cleaning not yet implemented")    
def test_invalid_characters():
    seq = "GGGGGCCCCCAAAAATTTTTXXXXX"
    exp = 50.0
    obs = calc_gc_content(seq)
    assert obs == exp