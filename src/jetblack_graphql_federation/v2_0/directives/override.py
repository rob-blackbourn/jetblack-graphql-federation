from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
)


OverrideDirective = GraphQLDirective(
    name="override",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "from": GraphQLArgument(GraphQLNonNull(GraphQLString)),
    },
    description="Federation @override directive",
)
