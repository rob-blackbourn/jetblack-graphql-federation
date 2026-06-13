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


class ContextDirective:
    """The @context directive

    directive @context(name: String!) on OBJECT | INTERFACE | UNION;
    """

    NAME = "context"
    ARG_NAME = 'name'

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
            DirectiveLocation.UNION,
        ),
        args={
            ARG_NAME: GraphQLArgument(GraphQLNonNull(GraphQLString)),
        },
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
            NameNode(value='OBJECT'),
            NameNode(value='INTERFACE'),
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
