from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
)

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
