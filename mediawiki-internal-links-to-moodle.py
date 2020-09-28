#!/usr/bin/env python

"""
Pandoc filter to convert CodiMDs [name=] tags
to dokuwiki links
"""

from panflute import *
import re

nametag_re = r"\[name=([a-zA-Z0-9]+)\]"

def replace_wikilinks(elem, doc):
    if isinstance(elem, Link):
        if elem.title == 'wikilink':
            debug(stringify(elem))

            return Str('[['+stringify(elem)+']]')

def main(doc=None):
   return run_filter(replace_wikilinks, doc=doc) 

if __name__ ==  '__main__':
    main()
    
