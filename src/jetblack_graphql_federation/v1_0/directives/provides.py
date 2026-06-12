from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
)

from ..scalars import _FieldSet

FIELDS_NAME = "fields"

PROVIDES_NAME = "provides"

ProvidesDirective = GraphQLDirective(
    name=PROVIDES_NAME,
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @provides directive",
)
