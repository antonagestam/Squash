import re

SELECTOR_PATTERN = re.compile(
    r'(?P<selector>[\w|#|_|\.|\-|\s|,|>]+?)(?:\s*){(?P<attributes>.*?)}',
    re.I | re.S)
ATTRIBUTE_PATTERN = re.compile(
    r'(?P<name>[\w|\-]+?):(?P<value>[\w|\d|#|\-|,|%|\s]+?);', re.I)