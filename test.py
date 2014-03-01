#!./bin/python

from squash import squash
from squash.benchmark import benchmark


source = """
.noselect {
  wtf: yes;
  color: green;
  hello: goodbye;
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
  color: green;
}

.ellipsify > .noselect {
  dimensions: infinite;
  pixels: five;
  hello: goodbye;
}

@

"""
result = squash(source)

print result

benchmark(source)