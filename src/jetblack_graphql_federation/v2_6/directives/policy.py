from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLList,
)

from ..scalars import Policy

PolicyDirective = GraphQLDirective(
    name="policy",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
        DirectiveLocation.SCALAR,
        DirectiveLocation.ENUM,
    ),
    args={
        "policies": GraphQLArgument(
            GraphQLNonNull(
                GraphQLList(GraphQLNonNull(
                    GraphQLList(GraphQLNonNull(Policy))))
            )
        ),
    },
    description="Federation @policy directive",
)
