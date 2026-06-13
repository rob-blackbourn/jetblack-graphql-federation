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


class OverrideDirective:
    """The @override directive

    directive @override(from: String!, label: String) on FIELD_DEFINITION
    """

    NAME = 'override'
    ARG_FROM = 'from'
    ARG_LABEL = 'label'

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
        ),
        args={
            ARG_FROM: GraphQLArgument(GraphQLNonNull(GraphQLString)),
            ARG_LABEL: GraphQLArgument(GraphQLString),
        },
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_FROM),
                type=NonNullTypeNode(
                    type=NamedTypeNode(
                        name=NameNode(
                            value='String'
                        )
                    )
                )
            ),
            InputValueDefinitionNode(
                name=NameNode(value=ARG_FROM),
                type=NamedTypeNode(
                    name=NameNode(
                        value='String'
                    )
                )
            ),
        ),
        repeatable=True,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
        )
    )

    @classmethod
    def Node(cls, from_: str, label: str) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_FROM),
                    value=StringValueNode(value=from_),
                ),
                ArgumentNode(
                    name=NameNode(value=cls.ARG_LABEL),
                    value=StringValueNode(value=label),
                ),
            )
        )
