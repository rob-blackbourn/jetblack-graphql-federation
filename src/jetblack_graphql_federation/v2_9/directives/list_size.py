from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLDirective,
    GraphQLInt,
    GraphQLList,
    GraphQLNonNull,
    GraphQLString,
)


ListSizeDirective = GraphQLDirective(
    name="listSize",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "assumed_size": GraphQLArgument(GraphQLInt),
        "slicing_arguments": GraphQLArgument(
            GraphQLList(GraphQLNonNull(GraphQLString))
        ),
        "sized_fields": GraphQLArgument(GraphQLList(GraphQLNonNull(GraphQLString))),
        "require_one_slicing_argument": GraphQLArgument(GraphQLBoolean),
    },
    description="Federation @listSize directive",
)
