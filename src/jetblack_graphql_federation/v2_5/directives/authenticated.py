from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)


class AuthenticatedDirective:
    """The @authenticated directive

    directive @authenticated on
        FIELD_DEFINITION
      | OBJECT
      | INTERFACE
      | SCALAR
      | ENUM
    """

    NAME = "authenticated"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
            DirectiveLocation.SCALAR,
            DirectiveLocation.ENUM,
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
            NameNode(value='SCALAR'),
            NameNode(value='ENUM'),
        )
    )

    @classmethod
    def Node(cls) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(),
        )
