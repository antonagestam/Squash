#!/usr/local/bin/python

from squash.compiler import squash

result = squash("""
.noselect {
  wtf: yes;
}

.noselect, .ellipsify {
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.ellipsify {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}""")

print result

assert result == (""".noselect,.ellipsify {-webkit-user-select: none;-moz-user-select: none;-webkit-touch-callout: none;-khtml-user-select: none;-ms-user-select: none;user-select: none;}
.ellipsify {white-space: nowrap;overflow: hidden;text-overflow: ellipsis;}
.noselect {wtf: yes;}""")