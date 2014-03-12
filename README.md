Squash
======

Squash is a next-step CSS minifier. It parses your stylesheets and finds selectors that has the same attributes and then batches them together. This way it's possible make your stylesheets even smaller than with standard space-removing tools.

The goal is for this project to evolve into an easy-to-use command line tool.

Usage
-----

```python
from squash import squash


print squash("""
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

.noselect {
  wtf: yes;
  color: green;
  hello: goodbye;
}
""")
```
