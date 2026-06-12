from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
)

from .v2_6 import get_directives as get_directives_v2_6

OverrideDirective = GraphQLDirective(
    name="override",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "from": GraphQLArgument(GraphQLNonNull(GraphQLString)),
        "label": GraphQLArgument(GraphQLString),
    },
    description="Federation @override directive",
)


# @override Change, Added label argument
def get_directives() -> dict[str, GraphQLDirective]:
    directives = get_directives_v2_6()
    directives.update(
        {directive.name: directive for directive in [OverrideDirective]})
    return directives
