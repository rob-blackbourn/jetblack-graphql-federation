from ..v2_1 import Federation as v2_1

from .directives import ShareableDirective


class Federation(v2_1):

    ShareableDirective = ShareableDirective
