'''

Unittest for Pygments Add-on MultisourceHtmlFormatter

:copyright: Copyright 2013 by christian.meichsner@informatik.tu-chemnitz.de, see AUTHORS.
:license: BSD, see LICENSE for details.

Usage:

    To run the tests herein goto the root directory of this project (.. from 
    the directory containing this file) and perform the subsequently given
    tasks. Make sure python points to a python e Executable
    
    (1) export PYTHONPATH=$PYTHONPATH:PATH_TO_THIS_DIRECTORY/MultisourceHtmlFormatter/
    (2) python test/TestMultisourceHtmlFormatter.py
    

'''
import unittest
from MultisourceHtmlFormatter import CodeLexerTuple, highlightMultiSource,\
    MultiSourceFormatter
from pygments.lexers.functional import HaskellLexer
import re
from re import MULTILINE
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.agile import PythonLexer

class MultisourceHtmlFormatterTest(unittest.TestCase):
    def test_just_one_file_with_title(self):
        tupel = CodeLexerTuple(open('test/resources/Quicksort.hs').read(), HaskellLexer(stripnl=False), 
                               'Haskell Quicksort');
        result = highlightMultiSource((tupel,), MultiSourceFormatter(
        linenos=True, cssclass="source", noclasses=True, showtitles=True))
        self.helper_just_one_file_title(result)
        self.assertFalse(re.search('<span>8</span>', result), "There must be only seven lines of code")
     
    def helper_just_one_file_title(self,result):   
        self.assertTrue(re.search('<span>Haskell Quicksort</span>', result, MULTILINE), "Result must contain title noting 'Haskell Quicksort'")
        self.assertTrue(re.search('<span>7</span>', result), "There must be seven lines of code")
        self.assertTrue(re.search('<span style="color: #0000FF">quicksort</span>', result), "There must be a function named quicksort highlighted")
    
    def test_just_one_file_without_title(self):
        tupel = CodeLexerTuple(open('test/resources/Quicksort.hs').read(), HaskellLexer(stripnl=False), 
                               'Haskell Quicksort');
        result = highlightMultiSource((tupel,), MultiSourceFormatter(
        linenos=True, cssclass="source", noclasses=True, showtitles=False))
        
        self.assertFalse(re.search('<span>Haskell Quicksort</span>', result), "Result must contain title noting 'Haskell Quicksort'")
        self.assertTrue(re.search('<span>7</span>', result), "There must be seven lines of code")
        self.assertFalse(re.search('<span>8</span>', result), "There must be only seven lines of code")
        self.assertTrue(re.search('<span style="color: #0000FF">quicksort</span>', result), "There must be a function named quicksort highlighted")

    def test_two_files_with_title(self):
        tupel = CodeLexerTuple(open('test/resources/Quicksort.hs').read(), HaskellLexer(stripnl=False), 
                               'Haskell Quicksort');
        tupel2 = CodeLexerTuple(open('test/resources/Quicksort.java').read(), JavaLexer(), 'Java Quicksort');
                               
        result = highlightMultiSource((tupel,tupel2), MultiSourceFormatter(
        linenos=True, cssclass="source", noclasses=True, showtitles=True))
        
        self.helper_just_one_file_title(result)
        
        self.assertTrue(re.search('<span>Java Quicksort</span>', result, MULTILINE), "Result must contain title noting 'Haskell Quicksort'")
        self.assertTrue(re.search('<span style="color: #0000FF; font-weight: bold">java.util.ArrayList</span>', result), "There must be an import java.util.ArrayList")
    
    def test_three_files_with_title(self):
        tupel = CodeLexerTuple(open('test/resources/Quicksort.hs').read(), HaskellLexer(stripnl=False), 
                               'Haskell Quicksort');
        tupel2 = CodeLexerTuple(open('test/resources/Quicksort.java').read(), JavaLexer(), 'Java Quicksort');
        tupel3 = CodeLexerTuple(open('test/resources/Quicksort.py').read(), PythonLexer(), 'Python Quicksort');
                               
        result = highlightMultiSource((tupel,tupel2,tupel3), MultiSourceFormatter(
        linenos=True, cssclass="source", noclasses=True, showtitles=True))
        
        #test invariant haskell source
        self.helper_just_one_file_title(result)
        
        #test java source
        self.assertTrue(re.search('<span>Java Quicksort</span>', result, MULTILINE), "Result must contain title noting 'Java Quicksort'")
        self.assertTrue(re.search('<span style="color: #0000FF; font-weight: bold">java.util.ArrayList</span>', result), "There must be an import java.util.ArrayList")

        #test python source
        self.assertTrue(re.search('<span>Python Quicksort</span>', result, MULTILINE), "Result must contain title noting 'Python Quicksort'")
        self.assertTrue(re.search('<span style="color: #008000; font-weight: bold">lambda</span>', result), "There must be an lambda keyword denoting an anonymous function")
       
if __name__ == "__main__":
    unittest.main() 