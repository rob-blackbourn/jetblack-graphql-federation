from graphql import (
    GraphQLScalarType,
    NameNode,
    ScalarTypeDefinitionNode,
    StringValueNode,
)


_FIELD_SET_DESCRIPTION = (
    "A string serialized scalar represent a set of fields that's passes to "
    "a federated directive, such as @key, @requires, or @provides"
)

_FIELD_SET_NAME = "_FieldSet"

_FieldSet = GraphQLScalarType(
    name=_FIELD_SET_NAME,
    description=_FIELD_SET_DESCRIPTION
)

_FieldSetNode = ScalarTypeDefinitionNode(
    name=NameNode(value=_FIELD_SET_NAME),
    description=StringValueNode(value=_FIELD_SET_DESCRIPTION),
)
