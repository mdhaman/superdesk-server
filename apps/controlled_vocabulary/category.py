# further refactoring is required after we define more vocab.

from superdesk.resource import Resource
from superdesk.services import BaseService
import superdesk

category_schema = {
    'code': {
        'type': 'string',
        'unique': True,
        'required': True,
        'minlength': 1,
        'maxlength': 1
    },
    'name': {
        'type': 'string',
        'unique': True,
        'required': True,
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


def init_app(app):
    endpoint_name = 'categories'
    service = CategoryService(endpoint_name, backend=superdesk.get_backend())
    CategoryResource(endpoint_name, app=app, service=service)