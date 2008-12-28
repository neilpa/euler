#!/usr/bin/env python
"""Downlad problems from Project Euler"""

from __future__ import with_statement

import os
import urllib2
from BeautifulSoup import BeautifulSoup, Comment
import contextlib

images = { 
    "images/symbol_minus.gif": "-",
    "images/symbol_times.gif": "*",
    "images/symbol_ne.gif": "!=",
    "images/symbol_lt.gif": "<",
}

def handle_tag(tag):
    try:
        tn = tag.name.lower()
    except AttributeError:
        # Not a tag, just a string 
        return tag.strip() and tag or ""

    # TODO: Figure out what the 'dfn' tag is about (problem 5)
    #<dfn title="divisible with no remainder">evenly divisible</dfn> 

    # TODO: Handle better problem 6, 9
    # <p>Some text<br><div align='center'>more stuff</div></p>

    s = ''
    if tn in ('p', 'b', 'i', 'sup', 'sub', 'div', 'dfn', 'var'):
        if tag.string:
            s = tag.string.replace('\n', ' ')
            #s = tag.string.strip()
        else:
            # Recursively convert the inner tags to ascii
            s = textify(tag)

        if tn == 'sup':
            # Do 1st instead of 1^st, etc.
            if tag.string not in ('st', 'nd', 'rd', 'th'):
                s = '^' + s
        elif tn == 'sub':
            s = '_' + s
        elif tn == 'p':
            # TODO: Add div and need a way to mark already formatted sections
            if tag.get('style') == 'text-align:center;':
                s = format_text(s, indent=6)
            else:
                s = format_text(s)
            s += '\n\n'
        elif tn == 'dfn':
            s = ' ' + s + ' '

    elif tn == 'br':
        s = '\n'

    elif tn == 'img': 
        if tag['src']:
            if tag['src'] in images:
                s = images[tag['src']]
            #TODO: try the 'alt' attribute
            else:
                print "Unrecognized image: %s" % tag

    else:
        print "Unrecognized tag: %s" % tag

    # TODO: a, td, tr, table, blockquote
    return s

def textify(soup):
    # Remove comments before processing
    return "".join([handle_tag(t) for t in soup.contents if not isinstance(t, Comment)])

def format_text(text, indent=0, col=80):
    lines = [[]]
    pos = indent

    for word in [w for w in text.split() if w.strip()]:
        pos += len(word) + 1
        if pos > col+1:
            lines.append([word])
            pos = indent + len(word) + 1
        else:
            lines[-1].append(word)

    return '\n'.join([indent*' ' + ' '.join(l) for l in lines])


template = \
r'''#!/usr/bin/env python
"""
Problem %d
%s
 
%s

Answer: ?????
"""

def solve():
    pass

if __name__ == '__main__':
    print "Answer: ", solve()

'''

def get_problem(num):
    url = "http://projecteuler.net/index.php?section=problems&id=%d" % num
    name = "%03d.py" % num
#    with contextlib.closing(urllib2.urlopen(url)) as page:
    with open("html/p%03d.html" % num) as page:
        soup = BeautifulSoup(page)

    #i.e. <div style="color:#666;font-size:80%;">05 October 2001</div>
    date = textify(soup.find('div', style="color:#666;font-size:80%;"))
    desc = textify(soup.find('div', 'problem_content')).strip()

    # Create a file from the template
    header = template % (num, date, desc)
    print header,
    input = raw_input("Save file as %s? ([y]/n): " % name)

    if input.lower() in ('', 'y', 'yes'):
        with open(name, 'w') as f:
            f.write(header)
        # FIXME: should use os.chmod
        os.system('chmod +x %s' % name)


if __name__ == "__main__":
    import sys
    for problem in sys.argv[1:]:
        get_problem(int(problem))

