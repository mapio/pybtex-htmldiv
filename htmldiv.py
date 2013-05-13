# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (c) 2013 Massimo Santini <santini@di.unimi.it>

import re

from pybtex.backends.html import Backend as HtmlBackend

file_extension = 'html'

RE_SUBST = (
        ( re.compile( r'([0-9]+)--([0-9]+)' ), r'\1&minus;\2' ),
        ( re.compile( r"\{(([\\'`0-9$()]|\w)+)\}" ), r'\1' ),
        ( re.compile( r'%\s*\n\s*' ), '' ),
)

SUBST = (
        ( r'---', '&mdash;' ),
        ( r'--', '&minus;' ),
        ( r'``', '&ldquo;' ),
        ( r"''", '&rdquo;' ),
        ( r'{\~n}', u'ñ' ),
        ( r"\'a", u'á' ),
        ( r'\`a', u'à' ),
        ( r'\`e', u'è' ),
        ( r"\'e", u'é' ),
        ( r'\`i', u'ì' ),
        ( r'\`u', u'ù' ),
        ( r"\'u", u'ú' ),
        ( r'\`o', u'ò' ),
        ( r"\'o", u'ö' ),
        ( r"\'u", u'ü' ),
        ( r'.~', '.&nbsp;' ),
        ( r'\ ', ' ' ),
        ( r'\&', '&amp;' ),
)

def regex_escape( text ):
    for s in RE_SUBST: text = s[ 0 ].sub( s[ 1 ], text )
    for s in SUBST: text = text.replace( *s )
    return text

class Backend(HtmlBackend):
    name = 'htmldiv'
    suffixes = '.html',

    def __init__(self, encoding = None, html_class = None, html_element = None, escape = None):
        super(Backend, self).__init__(encoding)
        self.html_class = u' class ="%s"' % html_class if html_class else u''
        self.html_element = html_element if html_element else 'div'
        self.escape = escape if escape else regex_escape

    def write_prologue(self):
        pass

    def write_epilogue(self):
        pass

    def format_text(self, text):
        return self.escape(text)

    def write_entry(self, key, label, text):
        self.output(u'<%s id="%s"%s>%s</%s>' % (self.html_element, key, self.html_class, text, self.html_element))
