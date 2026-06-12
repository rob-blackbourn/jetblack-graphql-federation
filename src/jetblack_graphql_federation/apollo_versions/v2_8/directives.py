from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
)

from .scalars import ContextFieldValue

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
