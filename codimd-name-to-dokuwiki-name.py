#!/usr/bin/env python

"""
Pandoc filter to convert CodiMDs [name=] tags
to dokuwiki links
"""

from panflute import *
import re

nametag_re = r"\[name=([a-zA-Z0-9]+)\]"

def replace_nametags(elem, doc):
    if isinstance(elem, Str):
        matches = re.search(nametag_re, elem.text)
        if matches:
            name = matches.group(1)
            if isinstance(elem.parent, Header):
                return Str('({})'.format(name))

            return Link(Str(name), url = 'name:' + name)

def main(doc=None):
   return run_filter(replace_nametags, doc=doc) 

if __name__ ==  '__main__':
    main()
    
