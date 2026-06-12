from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
)

from ..scalars import ContextFieldValue


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
