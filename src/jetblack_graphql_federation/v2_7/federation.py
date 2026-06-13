from typing import ClassVar

from ..v2_6 import Federation as Federation_v2_6

from .directives import OverrideDirective

type OverrideDirectiveType = type[OverrideDirective]


class Federation:
    """Federation v2.7

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v27
    """

    VERSION = "v2.7"

    # Scalars
    FieldSetScalar = Federation_v2_6.FieldSetScalar

    # Directives
    AuthenticatedDirective = Federation_v2_6.AuthenticatedDirective
    ComposeDirective = Federation_v2_6.ComposeDirective
    ExtendsDirective = Federation_v2_6.ExtendsDirective
    ExternalDirective = Federation_v2_6.ExternalDirective
    InaccessibleDirective = Federation_v2_6.InaccessibleDirective
    InterfaceObjectDirective = Federation_v2_6.InterfaceObjectDirective
    KeyDirective = Federation_v2_6.KeyDirective
    OverrideDirective: ClassVar[OverrideDirectiveType] = OverrideDirective
    PolicyDirective = Federation_v2_6.PolicyDirective
    ProvidesDirective = Federation_v2_6.ProvidesDirective
    RequiresScopesDirective = Federation_v2_6.RequiresScopesDirective
    ShareableDirective = Federation_v2_6.ShareableDirective
    TagDirective = Federation_v2_6.TagDirective
