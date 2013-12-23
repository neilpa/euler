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
    "images/symbol_le.gif": "<=",
    "images/symbol_gt.gif": ">",
    "images/symbol_ge.gif": ">=",
    "images/symbol_maps.gif": " --> ",
}

#TODO: clean-up this function
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

    # TODO: formatter stack??

    s = ''
    if tn in ('p', 'b', 'i', 'sup', 'sub', 'div', 'dfn', 'var', 'span', 'a', 'blockquote'):
        if tag.string:
            s = tag.string.replace('\n', ' ')
        else:
            # Recursively convert the inner tags to ascii
            s = textify(tag)

        if tn == 'sup':
            # Do 1st instead of 1^st, etc.
            if tag.string not in ('st', 'nd', 'rd', 'th'):
                s = '^' + s
        elif tn == 'sub':
            s = '_' + s
        elif tn in ('p', 'div', 'blockquote'):
            # TODO: Need a way to mark sections as already formattted
            # i.e. <p>some text<br/><div align='center'>centered text</div>end</p>
            # better idea, change the markup to <p>...</p><div>...</div><p>...</p>
            if tn == 'blockquote' or 'text-align:center;' in tag.get('style', '').lower():
                s = format_text(s, indent=8)
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
            else:
                print "Unrecognized image: %s" % tag

    else:
        # TODO: li, table
        # TODO: auto-download text files
        print "Unrecognized tag: %s" % tag

    return s

def textify(soup):
    # Remove comments before processing
    return "".join([handle_tag(t) for t in soup.contents if not isinstance(t, Comment)])
    #return [handle_tag(t) for t in soup.contents if not isinstance(t, Comment)]

def format_text(text, indent=0, col=80):

    def format(text, indent, col): 
        lines = [[]]
        pos = indent

        for word in [w for w in text.split() if w.strip()]:
            pos += len(word) + 1
            if pos > col+1:
                lines.append([word])
                pos = indent + len(word) + 1
            else:
                lines[-1].append(word)

        return '\n'.join(indent*' ' + ' '.join(l) for l in lines)

    return '\n'.join(format(l, indent, col) for l in text.split('\n') if l.strip())


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
    print "Answer: %%s" %% solve()

'''

def get_problem(num):
    url = "http://projecteuler.net/index.php?section=problems&id=%d" % num
    name = "%03d.py" % num
#    with contextlib.closing(urllib2.urlopen(url)) as page:
    with open("html/p%03d.html" % num) as page:
        # TODO: another replace dict
        html = page.read().replace('&nbsp;', ' ').replace('&sup2;', '^2')

    # TODO: regex to remove var, span 
    for t in ('<b>', '</b>', '<i>', '</i>'):
        html = html.replace(t, '')

    soup = BeautifulSoup(html)

    #i.e. <div style="color:#666;font-size:80%;">05 October 2001</div>
    date = textify(soup.find('div', style="color:#666;font-size:80%;"))
    desc = textify(soup.find('div', 'problem_content')).strip()

    # Create a file from the template
    header = template % (num, date, desc)
    print header,
    
    if raw_input("Save file as %s? ([y]/n): " % name).lower() in ('', 'y'):
        if not os.path.isfile(name) or raw_input("File exists, are you sure (y/[n])?").lower() == 'y':
            with open(name, 'w') as f:
                f.write(header)
            # FIXME: should use os.chmod
            os.system('chmod +x %s' % name)
            print "Created file %s" % name


if __name__ == "__main__":
    import sys
    for problem in sys.argv[1:]:
        get_problem(int(problem))

