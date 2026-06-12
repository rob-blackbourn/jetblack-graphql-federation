from graphql import (
    build_ast_schema,
    build_schema,
    parse,
    print_schema,
    DirectiveNode,
    DocumentNode,
    FieldDefinitionNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
    ObjectTypeDefinitionNode,
)

from jetblack_graphql_federation.v2_11 import Federation


def main() -> None:
    subgraph_text1 = """\
scalar FieldSet
directive @key(fields: FieldSet!, resolvable: Boolean = true) repeatable on OBJECT | INTERFACE
directive @shareable repeatable on FIELD_DEFINITION | OBJECT

type User @key(fields: "id") {
  id: ID!
  username: String! @shareable
}

type Query {
  me: User
}
"""
    schema_from_text1 = build_schema(subgraph_text1)
    ast1 = parse(subgraph_text1)
    schema1 = build_ast_schema(ast1)
    print("# Subgraph 1")
    # for type_ in schema_from_text1.type_map.values():
    #     if type_.ast_node is not None:
    #         print(print_ast(type_.ast_node))
    print(print_schema(schema_from_text1))

    subgraph_ast1 = DocumentNode(
        definitions=(
            # scalar FieldSet
            Federation.FieldSetNode,
            # directive @key(fields: FieldSet!, resolvable: Boolean = true) repeatable on OBJECT | INTERFACE
            Federation.KeyDirective.DefinitionNode,
            # directive @shareable repeatable on FIELD_DEFINITION | OBJECT
            Federation.ShareableDirective.DefinitionNode,
            # type User @key(fields: "id") {
            #   id: ID!
            #   username: String! @shareable
            # }
            ObjectTypeDefinitionNode(
                name=NameNode(value='User'),
                directives=(
                    Federation.KeyDirective.Node(fields="id")
                ),
                fields=(
                    FieldDefinitionNode(
                        name=NameNode(value='id'),
                        arguments=(),
                        type=NonNullTypeNode(
                            type=NamedTypeNode(
                                name=NameNode(value='ID')
                            )
                        ),
                    ),
                    FieldDefinitionNode(
                        name=NameNode(value='username'),
                        type=NonNullTypeNode(
                            type=NamedTypeNode(
                                name=NameNode(value='String')
                            )
                        ),
                        directives=(
                            DirectiveNode(
                                name=NameNode(value='shareable'),
                                arguments=(),
                            ),
                        ),
                    ),
                )
            ),
            ObjectTypeDefinitionNode(
                name=NameNode(value='Query'),
                fields=(
                    FieldDefinitionNode(
                        name=NameNode(value='me'),
                        type=NamedTypeNode(
                            name=NameNode(value='User')
                        )
                    ),
                )
            )
        )
    )
    s1 = build_ast_schema(subgraph_ast1)

    subgraph_text2 = """\
scalar FieldSet
directive @key(fields: FieldSet!, resolvable: Boolean = true) repeatable on OBJECT | INTERFACE

type Product @key(fields: "upc") {
  upc: String!
  name: String!
  price: Int
}

type Query {
  topProducts(first: Int = 5): [Product]
}
"""
    schema_from_text2 = build_schema(subgraph_text2)
    print("# Subgraph 2")
    print(print_schema(schema_from_text2))

    subgraph_text3 = """\
scalar FieldSet
directive @key(fields: FieldSet!, resolvable: Boolean = true) repeatable on OBJECT | INTERFACE
directive @external on FIELD_DEFINITION | OBJECT
directive @provides(fields: FieldSet!) on FIELD_DEFINITION

type Review {
  body: String
  author: User @provides(fields: "username")
  product: Product
}

type User @key(fields: "id") {
  id: ID!
  username: String! @external
  reviews: [Review]
}

type Product @key(fields: "upc") {
  upc: String!
  reviews: [Review]
}
"""
    schema_from_text3 = build_schema(subgraph_text3)
    print("# Subgraph 3")
    print(print_schema(schema_from_text3))


if __name__ == "__main__":
    main()
