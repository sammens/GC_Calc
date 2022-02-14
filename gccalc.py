#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:58:00 2022

@author: samuel
"""


def calc_gc_content(seq):
    if len(seq) == 0:
        return 0.0
    gc_content = ((seq.count("C") + seq.count("G"))/len(seq)) * 100
    return gc_content

def show_length(seq):
    length = len(seq)
    return length