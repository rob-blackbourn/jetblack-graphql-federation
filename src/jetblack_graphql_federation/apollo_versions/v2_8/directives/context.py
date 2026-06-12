from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
)

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
