from graphql import (
    ArgumentNode,
    BooleanValueNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLDirective,
    GraphQLInt,
    GraphQLList,
    GraphQLNonNull,
    GraphQLString,
    InputValueDefinitionNode,
    IntValueNode,
    ListTypeNode,
    ListValueNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
    StringValueNode,
)


class ListSizeDirective:
    """The @listSize directive

    directive @listSize(
      assumedSize: Int
      slicingArguments: [String!]
      sizedFields: [String!]
      requireOneSlicingArgument: Boolean = true
    )
    on FIELD_DEFINITION;
    """

    NAME = 'listSize'
    ARG_NAME_ASSUMED_SIZE = 'assumedSize'
    ARG_NAME_SLICING_ARGUMENTS = 'slicingArguments'
    ARG_NAME_SIZED_FIELDS = 'sizedFields'
    ARG_NAME_REQUIRE_ONE_SLICING_ARGUMENT = 'requireOneSlicingArgument'

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
        ),
        args={
            ARG_NAME_ASSUMED_SIZE: GraphQLArgument(GraphQLInt),
            ARG_NAME_SLICING_ARGUMENTS: GraphQLArgument(
                GraphQLList(GraphQLNonNull(GraphQLString))
            ),
            ARG_NAME_SIZED_FIELDS: GraphQLArgument(GraphQLList(GraphQLNonNull(GraphQLString))),
            ARG_NAME_REQUIRE_ONE_SLICING_ARGUMENT: GraphQLArgument(GraphQLBoolean),
        },
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME_ASSUMED_SIZE),
                type=NamedTypeNode(name=NameNode(value=GraphQLInt.name))
            ),
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME_SLICING_ARGUMENTS),
                type=ListTypeNode(
                    type=NonNullTypeNode(
                        type=NamedTypeNode(
                            name=NameNode(value=GraphQLString.name)
                        )
                    )
                )
            ),
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME_SIZED_FIELDS),
                type=ListTypeNode(
                    type=NonNullTypeNode(
                        type=NamedTypeNode(
                            name=NameNode(value=GraphQLString.name)
                        )
                    )
                )
            ),
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME_REQUIRE_ONE_SLICING_ARGUMENT),
                type=NamedTypeNode(name=NameNode(value=GraphQLBoolean.name)),
                default_value=True
            ),
        ),
        repeatable=False,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
        )
    )

    @classmethod
    def Node(
        cls,
        assumed_size: int | None,
        slicing_arguments: list[str] | None,
        sized_fields: list[str] | None,
        require_one_slicing_argument: bool | None = True

    ) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME_ASSUMED_SIZE),
                    value=IntValueNode(
                        value=str(assumed_size)
                    ),
                ),
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME_SLICING_ARGUMENTS),
                    value=ListValueNode(
                        values=tuple(
                            StringValueNode(
                                value=value
                            )
                            for value in slicing_arguments or []
                        )
                    ),
                ),
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME_SIZED_FIELDS),
                    value=ListValueNode(
                        values=tuple(
                            StringValueNode(
                                value=value
                            )
                            for value in sized_fields or []
                        )
                    ),
                ),
                ArgumentNode(
                    name=NameNode(
                        value=cls.ARG_NAME_REQUIRE_ONE_SLICING_ARGUMENT
                    ),
                    value=BooleanValueNode(
                        value=require_one_slicing_argument
                    ),
                ),
            )
        )
