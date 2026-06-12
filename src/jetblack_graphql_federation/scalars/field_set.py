from graphql import (
    GraphQLScalarType,
    NameNode,
    ScalarTypeDefinitionNode,
    StringValueNode
)

_DESCRIPTION = (
    "A string serialized scalar represent a set of fields that's passes to "
    "a federated directive, such as @key, @requires, or @provides"
)

_NAME = "FieldSet"

FieldSet = GraphQLScalarType(
    name=_NAME,
    description=_DESCRIPTION
)

FieldSetNode = ScalarTypeDefinitionNode(
    name=NameNode(value=_NAME),
    description=StringValueNode(value=_DESCRIPTION),
)
