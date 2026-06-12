from .directives import (
    ExtendsDirective,
    ExternalDirective,
    KeyDirective,
    ProvidesDirective,
    RequiresDirective,
)
from .scalars import (
    _FieldSet,
    _FieldSetNode
)


class Federation:

    # Scalars
    FieldSet = _FieldSet
    FieldSetNode = _FieldSetNode

    # Directives
    KeyDirective = KeyDirective
    RequiresDirective = RequiresDirective
    ProvidesDirective = ProvidesDirective
    ExternalDirective = ExternalDirective
    ExtendsDirective = ExtendsDirective
