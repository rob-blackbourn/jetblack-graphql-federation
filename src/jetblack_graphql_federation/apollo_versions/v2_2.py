from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)

from .v2_1 import get_directives as get_directives_v2_1

shareable_directive = GraphQLDirective(
    name="shareable",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
    ),
    description="Federation @shareable directive",
)


def get_directives() -> dict[str, GraphQLDirective]:
    directives = get_directives_v2_1()
    directives.update(
        {directive.name: directive for directive in [shareable_directive]}
    )
    return directives
