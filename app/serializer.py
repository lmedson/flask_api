from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .Models.Product import Product

ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product