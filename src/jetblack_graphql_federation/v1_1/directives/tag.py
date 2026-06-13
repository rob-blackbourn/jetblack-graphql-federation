from graphql import (
    ArgumentNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
    InputValueDefinitionNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
    StringValueNode,
)


class TagDirective:
    """The @tag directive

    directive @tag(name: String!) repeatable on
      | FIELD_DEFINITION
      | INTERFACE
      | OBJECT
      | UNION
    """

    NAME = 'tag'
    ARG_NAME = 'name'

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.INTERFACE,
            DirectiveLocation.OBJECT,
            DirectiveLocation.UNION,
        ),
        args={
            ARG_NAME: GraphQLArgument(GraphQLNonNull(GraphQLString)),
        },
        is_repeatable=True,
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME),
                type=NonNullTypeNode(
                    type=NamedTypeNode(
                        name=NameNode(
                            value='String'
                        )

                    )
                )
            )
        ),
        repeatable=True,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
            NameNode(value='INTERFACE'),
            NameNode(value='OBJECT'),
            NameNode(value='UNION'),
        )
    )

    @classmethod
    def Node(cls, name: str) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME),
                    value=StringValueNode(value=name),
                ),
            )
        )
