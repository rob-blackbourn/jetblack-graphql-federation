from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
)

from ..scalars import ContextFieldValue

from .v2_7 import get_directives as get_directives_v2_7

ContextDirective = GraphQLDirective(
    name="context",
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
        DirectiveLocation.UNION,
    ),
    args={
        "name": GraphQLArgument(GraphQLNonNull(GraphQLString)),
    },
    description="Federation @context directive",
)

FromContextDirective = GraphQLDirective(
    name="from_context",
    locations=[
        DirectiveLocation.ARGUMENT_DEFINITION,
    ],
    args={
        "field": GraphQLArgument(ContextFieldValue),
    },
    description="Federation @fromContext directive",
)


# Added directives @context, @from_context
def get_directives() -> dict[str, GraphQLDirective]:
    directives = get_directives_v2_7()
    directives.update(
        {
            directive.name: directive
            for directive in [ContextDirective, FromContextDirective]
        }
    )
    return directives
