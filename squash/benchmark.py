from decimal import Decimal

from .compiler import squash


def benchmark(source):
    source_size = len(source)
    squashed_size = len(squash(source))
    loss = Decimal(source_size - squashed_size)
    percentage = 100 * (loss / Decimal(source_size))

    print """
------------------------------------
Source code size was: %i characters
Squashed code size is: %i characters
Size loss: %i characters (%i%%)
------------------------------------
""" % (source_size, squashed_size, loss, percentage)