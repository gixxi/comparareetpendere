'''
This piece of source demonstrates the MultisourceHtmlFormatter that takes three quicksort implementations (python, haskell, java) into account
and produces html output of all implementations side-by-side. The output gets writen to stdout and file output.html

:copyright: Copyright 2013 by christian.meichsner@informatik.tu-chemnitz.de, see AUTHORS.
:license: BSD, see LICENSE for details.
'''
from MultisourceHtmlFormatter import CodeLexerTuple, highlightMultiSource,\
    MultiSourceFormatter
from pygments.lexers.agile import PythonLexer
from pygments.lexers.functional import HaskellLexer
from pygments.lexers.jvm import JavaLexer

if __name__ == "__main__":
    python = open('test/resources/Quicksort.py')
    haskell = open('test/resources/Quicksort.hs')
    java = open('test/resources/Quicksort.java')
    
    tupel1 = CodeLexerTuple(python.read(), PythonLexer(), 'Python Quicksort');
    tupel2 = CodeLexerTuple(haskell.read(), HaskellLexer(stripnl=False), 'Haskell Quicksort');
    tupel3 = CodeLexerTuple(java.read(), JavaLexer(), 'Java Quicksort');
    result = highlightMultiSource((tupel1,tupel2,tupel3), MultiSourceFormatter(linenos=True, cssclass="source", noclasses=True, showtitles=True))
    print(result)
    open('output.html','w').write("<html><body>" + result + "</body></html>")
    java.close()   
    haskell.close()    