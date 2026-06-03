from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLList,
)

from ..scalars import Policy
from .v2_5 import get_directives as get_directives_v2_5

policy_directive = GraphQLDirective(
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


# No Change, Added Subscription Support
def get_directives() -> dict[str, GraphQLDirective]:
    directives = get_directives_v2_5()
    directives.update(
        {directive.name: directive for directive in [policy_directive]})
    return directives
