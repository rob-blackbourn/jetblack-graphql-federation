from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLScalarType,
    NameNode,
    ScalarTypeDefinitionNode,
    StringValueNode,
)


_FIELD_SET_DESCRIPTION = (
    "A string serialized scalar represent a set of fields that's passes to "
    "a federated directive, such as @key, @requires, or @provides"
)

_FIELD_SET_NAME = "_FieldSet"

_FieldSet = GraphQLScalarType(
    name=_FIELD_SET_NAME,
    description=_FIELD_SET_DESCRIPTION
)

_FieldSetNode = ScalarTypeDefinitionNode(
    name=NameNode(value=_FIELD_SET_NAME),
    description=StringValueNode(value=_FIELD_SET_DESCRIPTION),
)

KEY_NAME = "key"
FIELDS_NAME = "fields"

KeyDirective = GraphQLDirective(
    name=KEY_NAME,
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    args={FIELDS_NAME: GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @key directive",
    is_repeatable=True,
)

REQUIRES_NAME = "requires"

RequiresDirective = GraphQLDirective(
    name=REQUIRES_NAME,
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @requires directive",
)

PROVIDES_NAME = "provides"

ProvidesDirective = GraphQLDirective(
    name=PROVIDES_NAME,
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @provides directive",
)

EXTERNALS_NAME = "external"

ExternalDirective = GraphQLDirective(
    name=EXTERNALS_NAME,
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    description="Federation @external directive",
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


def get_directives() -> dict[str, GraphQLDirective]:
    return {
        directive.name: directive
        for directive in [
            KeyDirective,
            RequiresDirective,
            ProvidesDirective,
            ExternalDirective,
            ExtendsDirective,
        ]
    }
