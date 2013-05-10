from StringIO import StringIO

from pybtex.plugin import find_plugin
from pybtex.style import FormattedBibliography

from htmldiv import clean

INPUT_ENCODING = 'utf8'
OUTPUT_ENCODING = 'utf8'
BIB_STYLE = 'plain'  # this may also be 'unsrt'
HTML_CLASS = 'bibentry'

buf = StringIO()

# get the required objects:
# - parser (to read the bibtex file),
# - style (to format the entry as "richtext"),
# - backend (to write the "richtext" as html)

parser = find_plugin('pybtex.database.input', 'bibtex')(encoding = INPUT_ENCODING)
style = find_plugin('pybtex.style.formatting', BIB_STYLE)()
backend = find_plugin('pybtex.backends', 'htmldiv')(OUTPUT_ENCODING, HTML_CLASS)

# read the bib file and extract the wanted entry

biblio = parser.parse_file('example.bib')
entry = biblio.entries['key']

# format the entry as unsrt and using htmldiv backend

formatted_entry = style.format_entries((entry,))
formatted_bibliography = FormattedBibliography(formatted_entry, style)
backend.write_to_stream(formatted_bibliography, buf)

print clean(buf.getvalue())
