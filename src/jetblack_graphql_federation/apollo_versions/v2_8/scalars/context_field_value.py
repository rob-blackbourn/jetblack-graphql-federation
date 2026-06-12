from graphql import (
    GraphQLScalarType,
    NameNode,
    ScalarTypeDefinitionNode,
    StringValueNode
)

_NAME = "federation__ContextFieldValue"
_DESCRIPTION = (
    "Contains the name of a defined context and a selection of a field "
    "from the context's type"
)

# Reference:
# https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives#fromcontext
# https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/use-contexts
ContextFieldValue = GraphQLScalarType(
    name=_NAME,
    description=_DESCRIPTION,
)


FieldSetNode = ScalarTypeDefinitionNode(
    name=NameNode(value=_NAME),
    description=StringValueNode(value=_DESCRIPTION),
)
