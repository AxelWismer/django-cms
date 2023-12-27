from graphene import relay, ObjectType

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Product, Service

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class Query(ObjectType):
    product = relay.Node.Field(ProductType)
    all_products = DjangoFilterConnectionField(ProductType)
    service = relay.Node.Field(ServiceType)
    all_services = DjangoFilterConnectionField(ServiceType)

