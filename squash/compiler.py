from .patterns import SELECTOR_PATTERN
from .classes import AttributeSet, Selector


class Compiler(object):
    def __init__(self, code):
        self.code = code
        self.selectors = {}
        self.attributes = AttributeSet()

    def _parse(self):
        for selector_list, attributes in SELECTOR_PATTERN.findall(self.code):
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

        self.attributes.parse()

    def _combine(self):
        new_selectors = []

        for _, attribute in self.attributes.iteritems():
            attribute_selector = None
            for __, selector in self.selectors.iteritems():
                if selector.attributes.has_attribute(attribute):
                    selector = Selector(selector.name, attribute.as_set())

                    if attribute_selector is None:
                        attribute_selector = selector
                    else:
                        attribute_selector += selector

            try:
                new_selectors[new_selectors.index(attribute_selector)] += attribute_selector
            except ValueError:
                new_selectors.append(attribute_selector)

        return new_selectors

    def compile(self):
        self._parse()
        combined = self._combine()

        return '\n'.join(map(Selector.compile, combined))