from abc import ABCMeta, abstractmethod
from typing import ClassVar, Mapping

from graphql import (
    DirectiveDefinitionNode,
    DirectiveNode,
    GraphQLDirective,
    GraphQLScalarType,
    ScalarTypeDefinitionNode
)


class AbstractDirective[NodeKwargs: Mapping](metaclass=ABCMeta):
    """Abstract class for directives"""

    Type: ClassVar[GraphQLDirective]

    # directive @shareable repeatable on OBJECT | FIELD_DEFINITION
    DefinitionNode: ClassVar[DirectiveDefinitionNode]

    @abstractmethod
    @classmethod
    def Node(cls, **kwargs: NodeKwargs) -> DirectiveNode:
        ...


class AbstractScalar(metaclass=ABCMeta):
    """Abstract class for scalars"""

    Type: ClassVar[GraphQLScalarType]

    DefinitionNode: ClassVar[ScalarTypeDefinitionNode]
