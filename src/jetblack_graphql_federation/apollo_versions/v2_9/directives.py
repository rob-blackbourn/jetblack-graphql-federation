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

RequiresScopeDirective = GraphQLDirective(
    name="cost",
    locations=(
        DirectiveLocation.ARGUMENT_DEFINITION,
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.INPUT_FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
        DirectiveLocation.SCALAR,
        DirectiveLocation.ENUM,
    ),
    args={
        "weight": GraphQLArgument(GraphQLNonNull(GraphQLInt)),
    },
    description="Federation @cost directive",
)
