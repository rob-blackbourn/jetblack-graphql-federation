from graphql import build_schema, print_schema


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
    print(print_schema(schema_from_text1))

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
    print(print_schema(schema_from_text3))


if __name__ == "__main__":
    main()
