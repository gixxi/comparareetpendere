'''
This script parses the program arguments to construct information needed to 
generate HTML output, displaying multiple source code files using the 
MultisourceHtmlFormatter.

run python3 run.py -h for usage.

:copyright: Copyright 2013 by christian.meichsner@informatik.tu-chemnitz.de, see AUTHORS.
:license: BSD, see LICENSE for details.
'''
from MultisourceHtmlFormatter import CodeLexerTuple, highlightMultiSource,\
    MultiSourceFormatter
from optparse import OptionParser, Option, OptionValueError
from copy import copy
from pygments.lexers import guess_lexer_for_filename
from pygments.util import ClassNotFound
import sys

def check_readfile(option, opt, value):
    try:
        return open(value,"r")
    except IOError:
        raise OptionValueError(
            "option %s: cannot open file for reading with name: %s" % (opt, value))

def check_writefile(option, opt, value):
    try:
        return open(value,"w")
    except IOError:
        raise OptionValueError(
            "option %s: cannot open file for writing with name: %s" % (opt, value))

def yield_codelexertuples(options):
	for (index, readfile) in enumerate(options.i):
		#get content from file given by optparse
		fileContent = readfile.read()
		#guess the lexer
		try:
			lexer = guess_lexer_for_filename(readfile.name, fileContent)
			if options.o:
				print("%d: file %s lexer %s" % (index, readfile.name, lexer))
			yield CodeLexerTuple(fileContent, lexer, options.t[index] if options.t else None)
		except ClassNotFound:
			raise OptionValueError("option -i: cannot guess lexer for file with name: %s" % readfile.name)


class CustomOption(Option):
    TYPES = Option.TYPES + ("readfile", "writefile")
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER["readfile"] = check_readfile
    TYPE_CHECKER["writefile"] = check_writefile

if __name__ == "__main__":
	usage = "usage: python3 run.py [options]"
	desc = """
Comparare et Pendere - multisource html formatter based on pygments.
Refer to http://gixxi.github.com/comparareetpendere
"""
	parser = OptionParser(usage = usage, description = desc, option_class = CustomOption);
	parser.add_option('-o', metavar='output filename', action='store', type="writefile",
		help='output filename. output is printed to stdout if not given.')
	parser.add_option('-i', metavar='input filename', action='append', type="readfile",	
		help='input filename of the source code file. Repeat -i <FILENAME> for each file to be included in the formatting process.')
	parser.add_option('-t', metavar='title', action='append', type="string", help='title above the the input file included in the formatted output. Repreat -t <TITLE> for each file to be included in the formatting process. Use quotes \' to for titles containing spaces.')
	(options, args) = parser.parse_args()

	#constraint: one input file must be given at least
	if not options.i:
		raise OptionValueError("option -i: at least one input file must be provided")

	#constraint: if titles are given at all then their number must match number of input files
	if options.t and len(options.t) != len(options.i):
		raise OptionValueError("option -t: when providing titles at all, the number of titles must be equal to the number of input files given by option -i")

	codeLexerTuples = tuple(yield_codelexertuples(options))
	result = highlightMultiSource(codeLexerTuples, MultiSourceFormatter(
        	linenos=True, cssclass="source", noclasses=True, showtitles=True if options.t else False))
	result = '<html><body>' + result + '</body></html>'
	if options.o:
		options.o.write(result)
	else:
		print(result)
