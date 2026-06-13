from typing import TypedDict

from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)

from ...types import AbstractDirective


class InaccessibleDirectiveKwargs(TypedDict):
    ...


class InaccessibleDirective(AbstractDirective[InaccessibleDirectiveKwargs]):
    """The @inaccessible directive

    directive @inaccessible on
      | FIELD_DEFINITION
      | OBJECT
      | INTERFACE
      | UNION
      | ARGUMENT_DEFINITION
      | SCALAR
      | ENUM
      | ENUM_VALUE
      | INPUT_OBJECT
      | INPUT_FIELD_DEFINITION
    """

    NAME = "inaccessible"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
            DirectiveLocation.UNION,
            DirectiveLocation.ENUM,
            DirectiveLocation.ENUM_VALUE,
            DirectiveLocation.SCALAR,
            DirectiveLocation.INPUT_OBJECT,
            DirectiveLocation.INPUT_FIELD_DEFINITION,
            DirectiveLocation.ARGUMENT_DEFINITION,
        ),
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(),
        repeatable=False,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
            NameNode(value='OBJECT'),
            NameNode(value='INTERFACE'),
            NameNode(value='UNION'),
            NameNode(value='ENUM'),
            NameNode(value='ENUM_VALUE'),
            NameNode(value='SCALAR'),
            NameNode(value='INPUT_OBJECT'),
            NameNode(value='INPUT_FIELD_DEFINITION'),
            NameNode(value='ARGUMENT_DEFINITION'),
        )
    )

    @classmethod
    def Node(cls, **kwargs: InaccessibleDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=()
        )
