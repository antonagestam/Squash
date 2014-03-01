#!/usr/local/bin/python

from squash.compiler import Compiler

c = Compiler("""
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

print c.compile()
