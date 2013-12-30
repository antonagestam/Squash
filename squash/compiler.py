import re
import hashlib

SELECTOR_PATTERN = re.compile(
    r'(?P<selector>[\w|#|_|\.|\-|\s|,]+?)(?:\s*){(?P<attributes>.*?)}',
    re.I | re.S)
ATTRIBUTE_PATTERN = re.compile(
    r'(?P<name>[\w|\-]+?):(?P<value>[\w|\d|#|\-|,|%|\s]+?);', re.I)


class Attribute(object):
    def __init__(self, name, value):
        self.name = name.strip()
        self.value = value.strip()
        self.hash = self._set_hash()

    def _set_hash(self):
        m = hashlib.md5()
        m.update(self.name)
        m.update(self.value)
        return m.hexdigest()

    def compile(self):
        return "%s: %s;" % (self.name, self.value)

    def as_set(self):
        attributes = AttributeSet()
        attributes._code = self.compile()
        attributes._attributes = {self.hash: self}
        return attributes


class AttributeSet(object):
    def __init__(self, code=None):
        self._code = code if code is not None else ""
        self._attributes = None

    def _parse(self):
        self._attributes = {}
        attributes = ATTRIBUTE_PATTERN.findall(self._code)
        for name, value in attributes:
            attribute = Attribute(name, value)
            self._attributes[attribute.hash] = attribute

    def __iter__(self):
        if self._attributes is None:
            self._parse()
        return self._attributes.__iter__()

    def __add__(self, other):
        return AttributeSet(self._code + "\n" + other._code)

    def has_attribute(self, attribute):
        if self._attributes is None:
            self._parse()
        return attribute.hash in self._attributes.keys()

    def iteritems(self):
        return self._attributes.iteritems()

    def compile(self):
        code = ""
        for _, attribute in self.iteritems():
            code += attribute.compile()
        return code


class Selector(object):
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def compile(self):
        return "%s {%s}" % (self.name, self.attributes.compile())

    def __add__(self, other):
        if self.name != other.name:
            new_name = "%s,%s" % (self.name, other.name)
        else:
            new_name = self.name
        return Selector(new_name, self.attributes + other.attributes)


class Compiler(object):
    def __init__(self, code):
        self.code = code
        self.selectors = {}
        self.attributes = AttributeSet()

    def _parse(self):
        selectors = SELECTOR_PATTERN.findall(self.code)

        for selector_list, attributes in selectors:
            attributes = AttributeSet(attributes)
            self.attributes += attributes
            selectors = selector_list.split(',')
            for selector_string in selectors:
                selector_string = selector_string.strip()
                selector = Selector(selector_string, attributes)
                if not selector_string in self.selectors:
                    self.selectors[selector_string] = selector
                else:
                    self.selectors[selector_string] += selector

        self.attributes._parse()

    def _combine(self):
        # 1. loop over all attributes and create a set of selectors for each
        # 2. loop over all new selectors and see if they can be combined
        new_selectors = []

        for _, attribute in self.attributes.iteritems():
            selectors = []
            for selector in self.selectors.itervalues():
                if selector.attributes.has_attribute(attribute):
                    selectors.append(Selector(selector.name, attribute.as_set()))
            new_selectors += selectors

        for s in new_selectors:
            #print s.compile()

        #print self.code

        #print new_selectors

    def compile(self):
        self._parse()
        self._combine()
