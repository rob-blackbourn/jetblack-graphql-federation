from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
)

from ..scalars import _FieldSet

FIELDS_NAME = "fields"

REQUIRES_NAME = "requires"

RequiresDirective = GraphQLDirective(
    name=REQUIRES_NAME,
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @requires directive",
)
