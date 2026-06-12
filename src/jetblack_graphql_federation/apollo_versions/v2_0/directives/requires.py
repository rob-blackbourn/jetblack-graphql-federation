from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
)

from ..scalars import FieldSet

RequiresDirective = GraphQLDirective(
    name="requires",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet))
    },  # Changed _FieldSet -> FieldSet
    description="Federation @requires directive",
)
