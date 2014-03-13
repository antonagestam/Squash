#!./bin/python

from squash import squash
from squash.benchmark import benchmark


source = """
.foo {
  background: red;
}
.bar {
  background: red;
  font-size: 12px;
}
"""
result = squash(source)

print result

benchmark(source)
