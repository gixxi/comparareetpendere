'''
Created on 11.12.2012

:copyright: Copyright 2013 by christian.meichsner@informatik.tu-chemnitz.de, see AUTHORS.
:license: BSD, see LICENSE for details.
'''

#1. standard library imports

#2. related third party imports
from pygments import lex
from pygments.formatter import Formatter
from pygments.lexer import Lexer
from pygments.token import Token, STANDARD_TYPES 
from pygments.util import get_bool_opt, get_int_opt
from _pyio import StringIO, BytesIO

class CodeLexerTuple:
    """
    helper class. Wraps a lexer operating on a code snippet that has a certain 
    title which is displayed optionally
    """
    def __init__(self, code, lexer, title = None):
        self.code = code
        self.lexer = lexer
        self.title = title
        if not isinstance(code, str):
            raise TypeError('first CodeLexerTuple() arguments must be a \
            str instance')
        if not isinstance(lexer, Lexer):
            raise TypeError('second CodeLexerTuple() arguments must be a \
            Lexer instance')
        
class AspectStyle:
    """
    helper class. An aspect style is used for styling the backgrounds, and line
    numbers of the output generated by the MultiSourceFormatter rather than 
    tokens within the sources as per a token type. Aspect conceptually refers 
    here to Cross Cutting Concern.
    """
    def __init__(self, name, styles):
        self.name = name
        self.styles = styles       
    
def _get_ttype_class(ttype):
    fname = STANDARD_TYPES.get(ttype)
    if fname:
        return fname
    aname = ''
    while fname is None:
        aname = '-' + ttype[-1] + aname
        ttype = ttype.parent
        fname = STANDARD_TYPES.get(ttype)
    return fname + aname    
            
_escape_html_table = {
    ord('&'): '&amp;',
    ord('<'): '&lt;',
    ord('>'): '&gt;',
    ord('"'): '&quot;',
    ord("'"): '&#39;',
    ord(" "): '&nbsp;'
}

def escape_html(text, table=_escape_html_table):
    """
    Escape &, <, > as well as single and double quotes for HTML.
    """
    return text.translate(table)
       
CSSCLASS_TD_TITLE = "td-title"  
CSSCLASS_LINENO = "lineno"   
CSSCLASS_BGCOLOREVEN = "bgcoloreven"  
CSSCLASS_BGCOLORODD = "bgcolorodd"
            
class MultiSourceFormatter(Formatter):
    """
    Formatter for Pygments The Python syntax highlighter.
    Takes a set of tokenized sourcecodes into account
    and displays all these side by side.
    The Formatter formats the output as HTML table. 
    Use this formatter to compare several source code snippets.
    
    Glossary:
    
    source code - source code to format using this class
    
    Additional options accepted: 
        
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
    
    'fontsize'
        Default: 1.2em. Denotes the font size used for formatting any token.
        
    'fontfamily'
        Default: Courier. Denotes the font family used for formatting any token.
            
    Usage:
    
        (1) Provide code snippets like 

        code1:
            print "Hello World"
            a=[1,2,3,4]
    
        code2 =
            (1,2,3,4) ** 2
        
        code3 =
            public static void main(String[] args) {
                for(String arg : args) {
                    System.out.println(arg);
                
                    int senseless = 0;
                }
            }
            
        (2) Wrap them

        tupel1 = CodeLexerTuple(code1, PythonLexer(), 'Something');
        tupel2 = CodeLexerTuple(code2, PythonLexer(), 'Rapster');
        tupel3 = CodeLexerTuple(code3, JavaLexer(), 'Java Foo');
    
        (3) Do the formatting
        result = highlightMultiSource((tupel1, tupel2, tupel3), MultiSourceFormatter(linenos=True, cssclass="source", noclasses=True, showtitles=True))

        (4) Output the result
        open('output.html','w').write("<html><body>" + result + "<br/>" + result2 + "</body></html>")           
    
    """
    def __init__(self, **options):
        Formatter.__init__(self, **options)
        self.lineseparator = options.get('lineseparator', '\n')
        self.tabwidth = get_int_opt(options, 'tabwidth', 4)
        self.escapetable = _escape_html_table
        self.escapetable[ord('\t')] = '&nbsp;' * self.tabwidth
        self.noclasses = get_bool_opt(options, 'noclasses', False)
        self.classprefix = options.get('classprefix', '')
        self.cssclass = options.get('cssclass', 'highlight')        
        self.stylebg = get_bool_opt(options, 'stylebg', True)
        self.stylebgalternating = get_bool_opt(options, 'stylebgalternating', 
                                               True)
        self.fontfamily = options.get('fontfamily','Courier')
        self.fontsize = options.get('fontsize','1.2em')
        self._create_stylesheet();
        self.linecolwidth = options.get('linecolwidth', 3)
        self.tablewidth = options.get('tablewidth', '100%')
        self.showtitles = get_bool_opt(options, 'showtitles', False)
        self.titles = []
        self.additionalstyles = options.get('additionalstyles', (
            AspectStyle(name=CSSCLASS_LINENO, styles = dict(bgcolor="eeeeee", 
                                                     borderright="eeaaaa")),
            AspectStyle(name="bgcoloreven", styles = dict(bgcolor="fafafa")),
            AspectStyle(name="bgcoloreven2", styles = dict(bgcolor="fdfdfd")),
            AspectStyle(name="bgcolorodd", styles = dict(bgcolor="f5f5f5")),
            AspectStyle(name="bgcolorodd2", styles = dict(bgcolor="f8f8f8")),
            AspectStyle(name=CSSCLASS_TD_TITLE, styles = dict(bgcolor="eeaaaa", 
                                                       paddingleft="15px"))
            )
        )
        self._create_additional_styles()

    def _get_css_class(self, ttype):
        """
        Return the css class of this token type prefixed with the classprefix
        option.
        """
        ttypeclass = _get_ttype_class(ttype)
        if ttypeclass:
            return self.classprefix + ttypeclass
        return ''

    def _create_stylesheet(self):
        t2c = self.ttype2class = {Token: ''}
        c2s = self.class2style = {}
        for ttype, ndef in self.style:
            name = self._get_css_class(ttype)
            style = "font-family: '%s'; " % self.fontfamily
            style += "font-size: %s; " % self.fontsize
            if ndef['color']:
                style += 'color: #%s; ' % ndef['color']
            if ndef['bold']:
                style += 'font-weight: bold; '
            if ndef['italic']:
                style += 'font-style: italic; '
            if ndef['underline']:
                style += 'text-decoration: underline; '
            if ndef['bgcolor']:
                style += 'background-color: #%s; ' % ndef['bgcolor']
            if ndef['border']:
                style += 'border: 1px solid #%s; ' % ndef['border']
            if style:
                t2c[ttype] = name
                # save len(ttype) to enable ordering the styles by
                # hierarchy (necessary for CSS cascading rules!)
                c2s[name] = (style[:-2], ttype, len(ttype))
            
    def _create_additional_styles(self):
        """
        add additional styles specific for this multisource formatter.
        Additional styles can be set when instantiating the 
        MultiSourceFormatter with parameter additionalstyles, type tuple of
        AspectStyle instances.
        """
        c2s = self.class2style
        for additionalstyle in self.additionalstyles:
            if not isinstance(additionalstyle, AspectStyle):
                raise TypeError('additionalStyle arguments must be a tuple of \
AspectStyle instances')
            ndef = additionalstyle.styles
            style = ''
            if 'color' in ndef:
                style += 'color: #%s; ' % ndef['color']
            if 'bold' in ndef:
                style += 'font-weight: bold; '
            if 'italic' in ndef:
                style += 'font-style: italic; '
            if 'underline' in ndef:
                style += 'text-decoration: underline; '
            if 'bgcolor' in ndef:
                style += 'background-color: #%s; ' % ndef['bgcolor']
            if 'border' in ndef:
                style += 'border: 1px solid #%s; ' % ndef['border']
            if 'borderright' in ndef:
                style += 'border-right: 1px solid #%s; ' % ndef['borderright']
            if 'paddingleft' in ndef:
                style += 'padding-left: %s; ' % ndef['paddingleft']
            if style:
                # save len(ttype) to enable ordering the styles by
                # hierarchy (necessary for CSS cascading rules!)
                c2s[additionalstyle.name] = style
            else:
                c2s[additionalstyle.name] = additionalstyle.styles        
    
    def format_unencoded(self, tokensList, outfile):
        """
        overrides a function from the superclass
        """        
        for line in self._yield_table(tokensList):
            outfile.write(line)
            
    def _yield_table(self, tokensList):
        """
        yields a table with a columns for each formatted source code 
        """
        yield '<table cellpadding=1 cellspacing=0 width="%s" class="%stable">'\
        % (self.tablewidth , self.cssclass)
        yield '<tr>'
        yield '<th width="%d%%"/>' % (self.linecolwidth)
        #contains the space each column with a source line of an individual source has
        ratio, mod = divmod(100 - self.linecolwidth,len(tokensList))
        for i,_ in enumerate(tokensList):
            yield '<th width="%d%%"/>' % (ratio if (i < len(tokensList) \
                                                    or mod == 0) else mod)
        yield '</tr>'
            
        #contains titles of the individual sources
        if self.showtitles:
            yield '<tr>'
            for emptyLinenoPart in self._yield_lineno(''):
                        yield emptyLinenoPart
            for title in self.titles:
                for titlePart in self._yield_title(title):
                    yield titlePart          
            yield '</tr>'
        
        previousLine = None
        lastLineEmpty = True
        for lineEmpty, line in self._yield_lines(tokensList):
            if previousLine:
                yield previousLine
            previousLine = line
            lastLineEmpty = lineEmpty
        if previousLine and not lastLineEmpty:
            yield previousLine    
        
        yield '</table>'

    def _yield_title(self, title):
        """
        yields a title text wrapped by a <td> tag with css class td-title
        """
        c2s = self.class2style
        cclass = CSSCLASS_TD_TITLE
        nocls = self.noclasses
        if nocls:
            yield "<td style='%s'>" % c2s[cclass] if cclass in c2s else ''
        else:
            yield "<td class='%s'>" % cclass
        yield "<span>%s</span></td>" % title


    def _yield_lineno(self, index):
        """
        yields a linenumber wrapped by <td> tag with css class lineno
        """
        c2s = self.class2style
        cclass = CSSCLASS_LINENO
        nocls = self.noclasses
        if nocls:
            yield "<td style='%s'>" % c2s[cclass] if cclass in c2s else ''
        else:
            yield "<td class='%s'>" % cclass
        yield "<span>%s</span></td>" % index

    def _is_code_left(self, decoratedTokensList):
        """
        returns boolean, true iff any of the token lists contains tokens to 
        process
        """
        for elem in decoratedTokensList:
            if elem['notEmpty']:
                return True
        return False

    def _yield_lines(self, tokensList):
        """
        we iterate over all datasources as long as one is available hence 
        still contains tokens
        """
        lineno = 1
        decoratedTokensList = []
        for index, tokenSource in enumerate(tokensList):
            decoratedTokens = {'notEmpty': True, 'tokensource': tokenSource, 
                               'index': index,
        #this generator replaces temporally the generator returned by the lexer
        #in order to support lexers returning tokens that contain line feeds
        #within
                                'yieldTokenParts': None}
            
            decoratedTokensList.append(decoratedTokens)
        
        while self._is_code_left(decoratedTokensList):
            lineBuffer = StringIO()
            lineStarted = False
            lineEmpty = True
            for containsSomething, singleSourceLine in \
            self._yield_multisourceline(decoratedTokensList, lineno):
                if containsSomething:
                    lineEmpty = False
                if not lineStarted:
                    lineBuffer.write('<tr>')            
                    for linenoPart in self._yield_lineno(lineno):
                        lineBuffer.write(linenoPart)
                    lineno += 1                  
                lineStarted = True
                lineBuffer.write(singleSourceLine)
            if lineStarted: 
                lineBuffer.write('</tr>')
            yield lineEmpty, lineBuffer.getvalue()
            
    def _yield_multisourceline(self, decoratedTokensList, lineno):
        """
        yield tuple of 
        (1) boolean, denoting whether any tokenlist contains a non-empty text
        for the current line
        (2) formatted set of lines, each line represents a sourcecode line from
        a token list wrapped by a <td> tag 
        """
        c2s = self.class2style
        nocls = self.noclasses
        
        for elem in decoratedTokensList:
            cclass = CSSCLASS_BGCOLOREVEN if elem['index'] % 2 == 0 else CSSCLASS_BGCOLORODD
            if self.stylebgalternating and lineno % 2 == 1:
                cclass += '2'
            if nocls:
                yield False, "<td style='%s'>" % c2s[cclass] if cclass in c2s \
                else ''
            else:
                yield False, "<td class='%s'>" % cclass
            if elem['notEmpty']:
                (line, empty) = \
                self._get_singlesourceline(elem)
                if line: 
                    yield True if line else False, line
                if empty: 
                    elem['notEmpty'] = False
            yield False, "</td>"
                
    def _get_singlesourceline(self, decoratedTokens):
        """
        returns a tuple of
        (1) one line of a certain source as well as as a flag denoting 
        (2) boolean, True if no more tokens are available
        """
        escape_table = _escape_html_table
        line = '';
        nocls = self.noclasses
        getcls = self.ttype2class.get
        c2s = self.class2style
        while True:
            tokensource = decoratedTokens['tokensource'] \
            if decoratedTokens['yieldTokenParts'] == None \
            else decoratedTokens['yieldTokenParts']
            try:
                (ttype, value) = tokensource.__next__()
                
                if nocls:
                    cclass = getcls(ttype)
                    while cclass is None:
                        ttype = ttype.parent
                        cclass = getcls(ttype)
                    cspan = cclass and '<span style="%s">' % c2s[cclass][0] \
                    or ''
                else:
                    cls = self._get_css_class(ttype)
                    cspan = cls and '<span class="%s">' % cls or ''                
                
                #tokens might span multiple lines - this is a bit tricky - 
                #'\n'.split('\n') splits into ('','')
                #'\n\n'.split('\n) splits into ('','','') 
                #FAQ: when do a line break? whenever an empty part occurs!
                if decoratedTokens['yieldTokenParts'] == None:
                    parts = value.split(self.lineseparator)
                    for index, part in enumerate(parts):
                        if part:
                            line += cspan + part.translate(escape_table) + (cspan and '</span>')
                        else:
                            if index == len(parts) - 1:
                                #last part, nothing to do, return what we have
                                decoratedTokens['yieldTokenParts'] = None
                                return line, False
                            else:
                                #switch generator to parts of current token
                                #we yield all the parts subsequently to the current
                                #one, which is a line feed ('' is linefeed) 
                                decoratedTokens['yieldTokenParts'] = \
                                yieldTokenParts(ttype, parts[index:])
                                break
                else:
                    if value:
                        line += cspan + value.translate(escape_table) + (cspan and '</span>')
                    else:
                        return line, False
            except (GeneratorExit, StopIteration):
                if decoratedTokens['yieldTokenParts'] == None:                
                    return (line, True)
                else:
                    decoratedTokens['yieldTokenParts'] = None
                    tokensource = decoratedTokens['tokensource']              

def yieldTokenParts(ttype, parts):
    """
    anonymous generator functions - lambdas are enought sometimes
    """
    lineFeedToMiss = False
    for elem in parts:
        if elem or lineFeedToMiss == False:
            lineFeedToMiss = False if elem else True
            yield ttype, elem
        else:
            lineFeedToMiss = False
            
def highlightMultiSource(codeLexerTuples, multiSourceFormatter, outfile=None):
    """
    main function to create formatted output based on tuples of code and
    related metadata (lexing information and title to display)
    """
    if not isinstance(codeLexerTuples, tuple):
        raise TypeError('first highlight() argument must be a tupel of \
codeLexerTuple')
    if not isinstance(multiSourceFormatter, Formatter):
        raise TypeError('second highlight() argument must be a \
MultiSourceFormatter')
           
    tokensList = []
    for codeLexerTuple in codeLexerTuples:        
        tokensList.append(lex(codeLexerTuple.code, codeLexerTuple.lexer)) 
        multiSourceFormatter.titles.append(codeLexerTuple.title)         
    if not outfile:
        #print formatter, 'using', formatter.encoding
        realoutfile = multiSourceFormatter.encoding and BytesIO() or StringIO()
        multiSourceFormatter.format(tokensList, realoutfile)
        return realoutfile.getvalue()
    else:
        multiSourceFormatter.format(tokensList, outfile)
                                      
