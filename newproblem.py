#!/usr/bin/env python
"""Downlad problems from Project Euler"""

from __future__ import with_statement

import os
import urllib2
from BeautifulSoup import BeautifulSoup, Comment
import contextlib

#TODO: Finish this
tags = {
    'p': '%s\n\n',
    'sup': '^%s',
    'sub': '_%s',
}

img_txt = { 
    "images/symbol_minus.gif": "-",
    "images/symbol_times.gif": "*",
    "images/symbol_ne.gif": "!=",
}

def handle_tag(tag):
    try:
        tn = tag.name.lower()
    except AttributeError:
        # Not a tag, just a string 
        return tag.strip()

    if tn in ('p', 'b', 'i', 'sup', 'sub', 'div'):
        if tag.string:
            s = tag.string.strip()
        else:
            # Recursively convert the inner tags to ascii
            s = textify(tag)

        if tn == 'sup':
            s = '^' + s
        elif tn == 'sub':
            s = '_' + s
        elif tn == 'p':
            if tag.get('style') == 'text-align:center;':
                # TODO: use format_text + indent
                s = '    ' + s
            else:
                s = format_text(s)
            s += '\n\n'

    elif tn == 'br':
        s = '\n'

    elif tn == 'img':
        s = img_txt.get(tag.src, '<IMG %S>' % tag.src)

    else:
        s = "<WTF tag=%s>" % tn

    # TODO: a, td, tr, table, blockquote
    return s

def textify(soup):
    # Remove comments before processing
    return "".join([handle_tag(t) for t in soup.contents if not isinstance(t, Comment)])

def format_text(text, col=80, indent=0, join=True):
    # TODO: Handle indent and join=False
    text.replace('\n', ' ')
    lines = [[]]
    pos = 0

    for word in [w for w in text.split() if w.strip()]:
        pos += len(word) + 1
        if pos > col+1:
            lines.append([word])
            pos = len(word) + 1
            print lines
        else:
            #print lines
            lines[-1].append(word)

    return '\n'.join([' '.join(l) for l in lines])

template = \
'''#!/usr/bin/env python
"""
Problem %d
%s
 
%s

Answer: ?????
"""

'''

def get_problem(num):
    url = "http://projecteuler.net/index.php?section=problems&id=%d" % num
#    with contextlib.closing(urllib2.urlopen(url)) as page:
    with open("html/p%03d.html" % num) as page:
        soup = BeautifulSoup(page)

    #<div style="color:#666;font-size:80%;">05 October 2001</div><br />
    date = textify(soup.find('div', style="color:#666;font-size:80%;"))

    desc = textify(soup.find('div', 'problem_content')).strip()

    print template % (num, date, desc),


    #name = "p%03d.py" % num
    #with open(name, 'w') as f:
    #    f.write(template)

if __name__ == "__main__":
    import sys
    for problem in sys.argv[1:]:
        get_problem(int(problem))

