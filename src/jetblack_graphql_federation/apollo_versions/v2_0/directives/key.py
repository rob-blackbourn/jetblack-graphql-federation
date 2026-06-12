from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLDirective,
    GraphQLNonNull,
)

from ..scalars import FieldSet

KeyDirective = GraphQLDirective(
    name="key",
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet)),
        # Changed from v1.0
        "resolvable": GraphQLArgument(GraphQLBoolean, default_value=True),
    },
    description="Federation @key directive",
    is_repeatable=True,
)
