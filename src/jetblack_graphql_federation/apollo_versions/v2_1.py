from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
)

from .v2_0 import get_directives as get_directives_v2_0

ComposeDirective = GraphQLDirective(
    name="composeDirective",
    locations=(
        DirectiveLocation.SCHEMA,
    ),
    args={
        "name": GraphQLArgument(GraphQLNonNull(GraphQLString)),
    },
    description="Federation @composeDirective directive",
)


def get_directives() -> dict[str, GraphQLDirective]:
    directives = get_directives_v2_0()
    directives.update(
        {directive.name: directive for directive in [ComposeDirective]})
    return directives
