from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)

from .v2_2 import get_directives as get_directives_v2_2

interface_object_directive = GraphQLDirective(
    name="interfaceObject",
    locations=(
        DirectiveLocation.OBJECT,
    ),
    description="Federation @interfaceObject directive",
)


def get_directives() -> dict[str, GraphQLDirective]:
    directives = get_directives_v2_2()
    directives.update(
        {directive.name: directive for directive in [
            interface_object_directive]}
    )
    return directives
