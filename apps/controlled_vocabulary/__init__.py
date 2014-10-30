from .category import CategoryResource, CategoryService
import superdesk


def init_app(app):
    endpoint_name = 'categories'
    service = CategoryService(endpoint_name, backend=superdesk.get_backend())
    CategoryResource(endpoint_name, app=app, service=service)