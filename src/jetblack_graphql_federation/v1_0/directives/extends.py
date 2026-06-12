from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    GraphQLDirective,
    NameNode,
)

EXTENDS_NAME = "extends"

ExtendsDirective = GraphQLDirective(
    name=EXTENDS_NAME,
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    description="Federation @extends directive",
)

# directive @extends on OBJECT | INTERFACE
ExtendsDirectiveNode = DirectiveDefinitionNode(
    name=NameNode(value="shareable"),
    arguments=(),
    repeatable=False,
    locations=(
        NameNode(value='OBJECT'),
        NameNode(value='INTERFACE'),
    )
)
