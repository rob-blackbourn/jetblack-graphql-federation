from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    GraphQLDirective,
    NameNode,
)


ShareableDirective = GraphQLDirective(
    name="shareable",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
    ),
    description="Federation @shareable directive",
)

# directive @shareable repeatable on FIELD_DEFINITION | OBJECT
ShareableDirectiveNode = DirectiveDefinitionNode(
    name=NameNode(value="shareable"),
    arguments=(),
    repeatable=True,
    locations=(
        NameNode(value='FIELD_DEFINITION'),
        NameNode(value='OBJECT'),
    )
)
