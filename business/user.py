from repositories import user
from utils.query_builder import build as build_query


def get(args):
    query = build_query(args)
    return user.get(query)
