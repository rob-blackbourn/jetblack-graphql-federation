from graphql import (
    GraphQLScalarType,
    NameNode,
    ScalarTypeDefinitionNode,
    StringValueNode
)

from ...types import AbstractScalar


class ContextFieldValueScalar[AbstractScalar]:
    """The federation__ContextFieldValue scalar"""

    NAME = "federation__ContextFieldValue"
    DESCRIPTION = (
        "Contains the name of a defined context and a selection of a field "
        "from the context's type"
    )

    # Reference:
    # https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives#fromcontext
    # https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/use-contexts
    Type = GraphQLScalarType(
        name=NAME,
        description=DESCRIPTION,
    )

    DefinitionNode = ScalarTypeDefinitionNode(
        name=NameNode(value=NAME),
        description=StringValueNode(value=DESCRIPTION),
    )
