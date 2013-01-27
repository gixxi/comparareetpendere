# Comparare et Pendere (lat. compare and weight) User Guide #

<table cellpadding=1 cellspacing=0 width="100%" class="sourcetable"><tr><th width="3%"/><th width="48%"/><th width="48%"/></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span></span></td><td style='background-color: #eeaaaa; padding-left: 15px; '><span>Haskell Quicksort</span></td><td style='background-color: #eeaaaa; padding-left: 15px; '><span>Python Quicksort</span></td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>1</span></td><td style='background-color: #fdfdfd; '><span style="color: #0000FF">quicksort</span>&nbsp;<span style="color: #AA22FF; font-weight: bold">::</span>&nbsp;(<span style="color: #B00040">Ord</span>&nbsp;a)&nbsp;<span style="color: #AA22FF; font-weight: bold">=&gt;</span>&nbsp;[a]&nbsp;<span style="color: #AA22FF; font-weight: bold">-&gt;</span>&nbsp;[a]</td><td style='background-color: #f8f8f8; '><span style="color: #008000; font-weight: bold">def</span>&nbsp;<span style="color: #0000FF">quicksort</span>(<span style="color: #008000">tuple</span>):</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>2</span></td><td style='background-color: #fafafa; '><span style="color: #0000FF">quicksort</span>&nbsp;<span style="color: #B00040">[]</span>&nbsp;<span style="color: #AA22FF; font-weight: bold">=</span>&nbsp;<span style="color: #B00040">[]</span></td><td style='background-color: #f5f5f5; '>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #008000; font-weight: bold">if</span>&nbsp;<span style="color: #008000">len</span>(<span style="color: #008000">tuple</span>)&nbsp;<span style="color: #666666">&lt;</span>&nbsp;<span style="color: #666666">2</span>:</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>3</span></td><td style='background-color: #fdfdfd; '><span style="color: #0000FF">quicksort</span>&nbsp;(x<span style="color: #B00040">:</span>xs)&nbsp;<span style="color: #AA22FF; font-weight: bold">=</span>&nbsp;smallerSorted&nbsp;<span style="color: #666666">++</span>&nbsp;[x]&nbsp;<span style="color: #666666">++</span>&nbsp;biggerSorted</td><td style='background-color: #f8f8f8; '>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #008000; font-weight: bold">return</span>&nbsp;<span style="color: #008000">tuple</span></td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>4</span></td><td style='background-color: #fafafa; '>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #008000; font-weight: bold">where</span>&nbsp;smallerSorted&nbsp;<span style="color: #AA22FF; font-weight: bold">=</span>&nbsp;quicksort&nbsp;(filter&nbsp;(<span style="color: #666666">&lt;=</span>x)&nbsp;xs)</td><td style='background-color: #f5f5f5; '>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #008000; font-weight: bold">else</span>:</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>5</span></td><td style='background-color: #fdfdfd; '>&nbsp;&nbsp;&nbsp;&nbsp;biggerSorted&nbsp;<span style="color: #AA22FF; font-weight: bold">=</span>&nbsp;quicksort&nbsp;(filter&nbsp;(<span style="color: #666666">&gt;</span>x)&nbsp;xs)</td><td style='background-color: #f8f8f8; '>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;<span style="color: #666666">=</span>&nbsp;<span style="color: #008000">tuple</span>[<span style="color: #666666">0</span>]</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>6</span></td><td style='background-color: #fafafa; '></td><td style='background-color: #f5f5f5; '>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xs&nbsp;<span style="color: #666666">=</span>&nbsp;<span style="color: #008000">tuple</span>[<span style="color: #666666">1</span>:]</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>7</span></td><td style='background-color: #fdfdfd; '><span style="color: #0000FF">print</span>&nbsp;(quicksort&nbsp;[<span style="color: #666666">10</span>,&nbsp;<span style="color: #666666">0</span>,&nbsp;<span style="color: #666666">0</span>,&nbsp;<span style="color: #666666">-</span><span style="color: #666666">1</span>,&nbsp;<span style="color: #666666">-</span><span style="color: #666666">2</span>,&nbsp;<span style="color: #666666">4</span>,&nbsp;<span style="color: #666666">4</span>,&nbsp;<span style="color: #666666">7</span>,&nbsp;<span style="color: #666666">4</span>,&nbsp;<span style="color: #666666">1</span>,&nbsp;<span style="color: #666666">100</span>,&nbsp;<span style="color: #666666">-</span><span style="color: #666666">1000</span>])</td><td style='background-color: #f8f8f8; '>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;smallerSorted&nbsp;<span style="color: #666666">=</span>&nbsp;quicksort(<span style="color: #008000">list</span>(<span style="color: #008000">filter</span>(<span style="color: #008000; font-weight: bold">lambda</span>&nbsp;elem:elem<span style="color: #666666">&lt;</span><span style="color: #666666">=</span>x,&nbsp;xs)))</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>8</span></td><td style='background-color: #fafafa; '></td><td style='background-color: #f5f5f5; '>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;biggerSorted&nbsp;<span style="color: #666666">=</span>&nbsp;quicksort(<span style="color: #008000">list</span>(<span style="color: #008000">filter</span>(<span style="color: #008000; font-weight: bold">lambda</span>&nbsp;elem:elem<span style="color: #666666">&gt;</span>x,&nbsp;xs)))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>9</span></td><td style='background-color: #fdfdfd; '></td><td style='background-color: #f8f8f8; '>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #008000; font-weight: bold">return</span>&nbsp;smallerSorted&nbsp;<span style="color: #666666">+</span>&nbsp;<span style="color: #008000">list</span>((x,))&nbsp;<span style="color: #666666">+</span>&nbsp;biggerSorted</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>10</span></td><td style='background-color: #fafafa; '></td><td style='background-color: #f5f5f5; '></td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>11</span></td><td style='background-color: #fdfdfd; '></td><td style='background-color: #f8f8f8; '><span style="color: #008000; font-weight: bold">if</span>&nbsp;__name__&nbsp;<span style="color: #666666">==</span>&nbsp;<span style="color: #BA2121">&quot;</span><span style="color: #BA2121">__main__</span><span style="color: #BA2121">&quot;</span>:</td></tr><tr><td style='background-color: #eeeeee; border-right: 1px solid #eeaaaa; '><span>12</span></td><td style='background-color: #fafafa; '></td><td style='background-color: #f5f5f5; '>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #008000; font-weight: bold">print</span>(quicksort((<span style="color: #666666">10</span>,&nbsp;<span style="color: #666666">0</span>,&nbsp;<span style="color: #666666">0</span>,&nbsp;<span style="color: #666666">-</span><span style="color: #666666">1</span>,&nbsp;<span style="color: #666666">-</span><span style="color: #666666">2</span>,&nbsp;<span style="color: #666666">4</span>,&nbsp;<span style="color: #666666">4</span>,&nbsp;<span style="color: #666666">7</span>,&nbsp;<span style="color: #666666">4</span>,&nbsp;<span style="color: #666666">1</span>,&nbsp;<span style="color: #666666">100</span>,&nbsp;<span style="color: #666666">-</span><span style="color: #666666">1000</span>)))</td></tr></table>

VERSION
=======

0.9 release date 2013/01/25 

SYNOPSIS
========

Comparare et Pendendere is a source code formatter that produces HTML output 
from a set of source codes in order to compare and analyse the individual 
source codes. This tools aims to ease highlighting source code in wikis, 
documentation or other applications. Comparare et Pendere is a Formatter on-top 
of pygments (The python syntax highlighter, http://pygments.org).

DEPENDENCIES
============

* Python version >= 3
* Pygments version >= 1.5

To install pygments enter on a debian-like system enter:
  
	sudo apt-get pygments

INSTALLATION 
============

Download the source archive ComparareEtPendere-0.9.tar.gz and extract it:

	tar -xf ComparareEtPendere-0.9.tar.gz

Change to the directory:

	cd ComparareEtPendere-0.9

Install the python package:

	sudo python3 setup.py install

USAGE
=====

Assuming you have several sourcecode files you want to compare in the current 
directory the the following python code generated a file output.html in the
current directory:


    from MultisourceHtmlFormatter import MultiSourceFormatter
    from MultisourceHtmlFormatter import CodeLexerTuple
    from pygments.lexers.functional import HaskellLexer
    from pygments.lexers.jvm import JavaLexer
    from MultisourceHtmlFormatter import highlightMultiSource
    
    tuple = CodeLexerTuple(open('Quicksort.hs').read(), HaskellLexer(stripnl=False),
                               'Haskell Quicksort')
    tuple2 = CodeLexerTuple(open('Quicksort.java').read(), JavaLexer(),
                         'Java Quicksort')
    result = highlightMultiSource((tuple,tuple2), MultiSourceFormatter(
        linenos=True, cssclass="source", noclasses=True, showtitles=True))
    open("output.html", mode="w").write("<html><body>" + result + "<body></html>")


The workhorse method `highlightMultiSource` takes a tuple of `CodeLexerTuple` 
instances as well as a `MultiSourceFormatter` into account. 
A `CodeLexerTuple` instance is needed for each sourcefile to display and 
contains the (1) actual sourcecode, (2) a lexer instance from Pygments, 
and (3) optionally the title of the sourcecode displayed above it.
The `MultiSourceFormatter` is instantiated using flags controlling the
output generation. Flags are:

    'lineseparator'
        Default '\n'. Lineseparator used in the source code.
    
    'tabwidth'
        Default 2. Denotes the number of spaces a tab is formatted as.
        
    'escapetable' 
        A map containing associations from characters to html encodings.
        
    'noclasses'
        Default False. If True then only class information are included in the
        generated tags and the html file containing the formatted output needs
        to import a css file with the needed css definitions.
        
    'classprefix'
        Default ''. Prefix for all used css class.
        
    'cssclass'
        Default 'highlight'. Prefix for the css class used for the top level
        <table> tag generated by this formatter.
    
    'stylebg'
        Default True. True denotes that the individual source codes' background
        is colored alternating using the css classes bgcoloreven, bgcolorodd.

    'stylebg'
        Default True. True and stylebg == True denote that the individual 
        source codes' background is colored alternating using the css classes 
        bgcoloreven, bgcolorodd, bgcoloreven2, bgcolorodd2.
        
    'linecolwidth'
        Default 3. Denotes percentage of space relative to table width, 
        the line number column is consuming.
        
    'tablewidth'
        Default 100%. Denotes the html-conform width the generated table
        consumes within the embedding element.
        
    'showtitles'
        Default False. True denotes that above every source code column a title
        is displayed with css class td-title wrapped in a <td> tag. the title
        is accompanied with the source code
        
    'additionalstyles'
        Formatting css classes for aspects solely related to this formatter 
        rather than tokens of the source code. Currently the following
        css classes are of interest:
            lineno, td-title, bgcoloreven, bgcoloreven2, bgcolorodd,
            bgcolorodd2

Authors
=======

Christian Meichsner (PoP Lucern, Switzerland) 
christian.meichsner@informatik.tu-chemnitz.de

Licensing
=========

This programm come licensed under the BSD license.

Copyright (c) 2006-2013 by the respective authors (see AUTHORS file).
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



