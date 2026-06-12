from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
)

from ..scalars import _FieldSet

KEY_NAME = "key"
FIELDS_NAME = "fields"

KeyDirective = GraphQLDirective(
    name=KEY_NAME,
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    args={FIELDS_NAME: GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @key directive",
    is_repeatable=True,
)
