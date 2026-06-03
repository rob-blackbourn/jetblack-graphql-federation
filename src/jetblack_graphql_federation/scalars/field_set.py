from graphql import (
    GraphQLScalarType,
)

_FieldSet = GraphQLScalarType(
    name="_FieldSet",
    description=(
        "A string serialized scalar represent a set of fields that's passes to "
        "a federated directive, such as @key, @requires, or @provides"
    )
)

FieldSet = GraphQLScalarType(
    name="FieldSet",
    description=(
        "A string serialized scalar represent a set of fields that's passes to "
        "a federated directive, such as @key, @requires, or @provides"
    )
)
