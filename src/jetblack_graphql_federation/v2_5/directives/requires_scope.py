from graphql import (
    ArgumentNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLList,
    GraphQLNonNull,
    InputValueDefinitionNode,
    ListTypeNode,
    ListValueNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
    StringValueNode,
)

from ..scalars import ScopeScalar


class RequiresScopesDirective:
    """The @requiresScopes directive

    directive @requiresScopes(scopes: [[federation__Scope!]!]!) on
        FIELD_DEFINITION
      | OBJECT
      | INTERFACE
      | SCALAR
      | ENUM
    """

    NAME = "requiresScopes"
    ARG_SCOPES = 'scopes'

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
            DirectiveLocation.SCALAR,
            DirectiveLocation.ENUM,
        ),
        args={
            ARG_SCOPES: GraphQLArgument(
                GraphQLNonNull(
                    GraphQLList(GraphQLNonNull(
                        GraphQLList(GraphQLNonNull(ScopeScalar.Type))))
                )
            ),
        },
        description=f"Federation @{NAME} directive",
    )
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_SCOPES),
                type=NonNullTypeNode(
                    type=ListTypeNode(
                        type=NamedTypeNode(
                            name=NameNode(
                                value=ScopeScalar.NAME
                            )
                        )
                    )
                )
            )
        ),
        repeatable=True,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
            NameNode(value='OBJECT'),
            NameNode(value='INTERFACE'),
            NameNode(value='SCALAR'),
            NameNode(value='ENUM'),
        )
    )

    @classmethod
    def Node(cls, scopes: list[str]) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_SCOPES),
                    value=ListValueNode(
                        values=tuple(
                            StringValueNode(value=scope)
                            for scope in scopes
                        )
                    ),
                ),
            )
        )
