import hashlib

from .patterns import ATTRIBUTE_PATTERN


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

    def parse(self):
        self._attributes = {}
        attributes = ATTRIBUTE_PATTERN.findall(self._code)
        for name, value in attributes:
            attribute = Attribute(name, value)
            self._attributes[attribute.hash] = attribute

    def __iter__(self):
        if self._attributes is None:
            self.parse()
        return self._attributes.__iter__()

    def __add__(self, other):
        new = AttributeSet(self._code + "\n" + other._code)
        new.parse()
        return new

    def has_attribute(self, attribute):
        if self._attributes is None:
            self.parse()
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

    def __eq__(self, other):
        return set(self.name.split(',')) == set(other.name.split(','))