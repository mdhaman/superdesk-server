# further refactoring is required after we define more vocab.

from superdesk.resource import Resource
from superdesk.services import BaseService


category_schema = {
    'code': {
        'type': 'string',
        'unique': True,
        'required': True,
        'regex': '^[a-zA-Z]{1}$'
    },
    'name': {
        'type': 'string',
        'unique': True,
        'required': True,
        'minlength': 2
    },
    'description': {
        'type': 'string'
    }
}


class CategoryResource(Resource):
    schema = category_schema
    datasource = {'default_sort': [('name', -1)]}


class CategoryService(BaseService):
    pass
