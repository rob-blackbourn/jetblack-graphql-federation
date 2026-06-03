from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLList,
)

from ..scalars import Scope
from .v2_4 import get_directives as get_directives_v2_4


authenticated_directive = GraphQLDirective(
    name="authenticated",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
        DirectiveLocation.SCALAR,
        DirectiveLocation.ENUM,
    ),
    description="Federation @authenticated directive",
)

requires_scope_directive = GraphQLDirective(
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


# No Change, Added Subscription Support
def get_directives() -> dict[str, GraphQLDirective]:
    directives = get_directives_v2_4()
    directives.update(
        {
            directive.name: directive
            for directive in [authenticated_directive, requires_scope_directive]
        }
    )
    return directives
