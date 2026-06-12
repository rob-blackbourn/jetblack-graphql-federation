from abc import ABCMeta, abstractmethod
from typing import Any, Mapping, Unpack, TypedDict, ParamSpecKwargs

from graphql import (
    DirectiveDefinitionNode,
    DirectiveNode,
    GraphQLDirective,
)


class AbstractDirective[NodeKwargs: Mapping](metaclass=ABCMeta):

    Type: GraphQLDirective

    # directive @shareable repeatable on OBJECT | FIELD_DEFINITION
    DefinitionNode: DirectiveDefinitionNode

    @abstractmethod
    @classmethod
    def Node(cls, **kwargs: NodeKwargs) -> DirectiveNode:
        ...
