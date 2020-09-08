from graphene_django import DjangoObjectType
import graphene

from .models import Book as BookModel


class Book(DjangoObjectType):
    class Meta:
        model = BookModel


class Query(graphene.ObjectType):
    books = graphene.List(Book)

    def resolve_books(self, info):
        return BookModel.objects.all()


schema = graphene.Schema(query=Query)
