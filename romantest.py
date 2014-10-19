#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: romantest.py
'''roman.py 的单元测试

This program is part of 'Dive Into Python 3', a free Python book for
experienced programmers.  Visit http://diveintopython3.org/ for the
latest version.
'''

import roman
import unittest

class KnownValues(unittest.TestCase):
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values(self):
        '''to_roman 已知结果测试'''
        for integer, numeral in self.known_values:
            result = roman.to_roman(integer)
            self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        '''from_roman 已知结果测试'''
        for integer, numeral in self.known_values:
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)

class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman 超过最大值应报错'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 4000)
    
    def test_zero(self):
        '''to_roman 不能为零'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 0)

    def test_negative(self):
        '''to_roman 不能为负数'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, -1)
    
    def test_non_integer(self):
        '''to_roman 必须为整数'''
        self.assertRaises(roman.NotIntegerError, roman.to_roman, 0.5)

class FromRomanBadInput(unittest.TestCase):
    def test_too_many_repeated_numerals(self):
        '''from_roman 数字不能重复太多次'''
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)

    def test_repeated_pairs(self):
        '''from_roman 检查某些未被重复的模式'''
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)

    def test_malformed_antecedents(self):
        '''from_roman 测试应当检测数字是否以正确顺序出现'''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)

    def test_blank(self):
        '''from_roman 空字符串异常'''
        self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, '')

    def test_non_string(self):
        '''from_roman 必须为字符串'''
        self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, 1)

class RoundtripCheck(unittest.TestCase):
    def test_roundtrip(self):
        '''from_roman 当 n = 1...3999 时 from_roman(to_roman(n))==n'''
        for integer in range(1, 4000):
            numeral = roman.to_roman(integer)
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)

if __name__ == '__main__':
    unittest.main()

# Copyright (c) 2009, Mark Pilgrim, All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.