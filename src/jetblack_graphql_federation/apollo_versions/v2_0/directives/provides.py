from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
)

from ..scalars import FieldSet

ProvidesDirective = GraphQLDirective(
    name="provides",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet))
    },  # Changed _FieldSet -> FieldSet
    description="Federation @provides directive",
)
