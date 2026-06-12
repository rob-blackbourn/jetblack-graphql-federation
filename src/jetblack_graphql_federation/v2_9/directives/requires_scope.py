from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLInt,
    GraphQLNonNull,
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
