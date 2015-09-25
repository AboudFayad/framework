#!/usr/bin/env python

import re

#  "coding[:=]\s*([-\w.]+)"

p = re.compile("(GPI|gpi)\s+v([\d.]+).*[Nn]et.*v([\d]+)")

hdr = "# This comment was generated by GPI v0.6.0 for network v3"
hdr = "# This newtowrk was written by GPI v0.6.0-dev, network v3."
#hdr = "# This newtowrk was written by v0.6.0, network v3."
#hdr = "# This comment was generated by GPI v0.6.0 for Network v3"
#hdr = "# vim: set fileencoding=utf8 :"


m = p.search(hdr)

if m:
    try:
        print('match: ', m.group(0))
        print('GPI version: ', m.group(2))
        print('Network version: ', m.group(3))
    except:
        pass