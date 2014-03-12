from .patterns import SELECTOR_PATTERN
from .classes import AttributeSet, Selector


class Compiler(object):
    def __init__(self, source):
        self.source = source

    def _parse(self, source):
        selectors = {}
        attributes = AttributeSet()

        for selector_list, attribute_set in SELECTOR_PATTERN.findall(source):
            attribute_set = AttributeSet(attribute_set)
            attributes += attribute_set
            selector_list = selector_list.split(',')
            for selector_string in selector_list:
                selector_string = selector_string.strip()
                selector = Selector(selector_string, attribute_set)
                if not selector_string in selectors:
                    selectors[selector_string] = selector
                else:
                    selectors[selector_string] += selector

        attributes.parse()

        return selectors, attributes

    def _combine(self, selectors, attributes):
        new_selectors = []

        for _, attribute in attributes.iteritems():
            attribute_selector = None
            for __, selector in selectors.iteritems():
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
        combined = self._combine(*self._parse(self.source))
        return ''.join(map(Selector.compile, combined))


def squash(source):
    return Compiler(source).compile()
