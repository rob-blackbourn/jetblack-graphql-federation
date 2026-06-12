from abc import ABCMeta, abstractmethod

from graphql import (
    DirectiveDefinitionNode,
    DirectiveNode,
    GraphQLDirective,
)


class AbstractDirective(metaclass=ABCMeta):

    Type: GraphQLDirective

    # directive @shareable repeatable on OBJECT | FIELD_DEFINITION
    DefinitionNode: DirectiveDefinitionNode

    @abstractmethod
    @classmethod
    def Node(cls, *args, **kwargs) -> DirectiveNode:
        ...
