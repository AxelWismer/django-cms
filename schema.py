import graphene
import products 
import products.schema

class Query(
    products.schema.Query, # Add your Query objects here
    graphene.ObjectType
):
    pass
    
schema = graphene.Schema(query=Query)