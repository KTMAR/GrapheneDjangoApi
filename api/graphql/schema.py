import graphene
from .query import Query
from api.graphql.mutations.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
