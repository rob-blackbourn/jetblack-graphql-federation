from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLList,
)

from ..scalars import Scope


RequiresScopeDirective = GraphQLDirective(
    name="requiresScopes",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
        DirectiveLocation.SCALAR,
        DirectiveLocation.ENUM,
    ),
    args={
        "scopes": GraphQLArgument(
            GraphQLNonNull(
                GraphQLList(GraphQLNonNull(GraphQLList(GraphQLNonNull(Scope))))
            )
        ),
    },
    description="Federation @requiresScopes directive",
)
