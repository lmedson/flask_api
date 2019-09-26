from flask import Blueprint, current_app, request, jsonify
from ..Models.Product import Product
from ..serializer import ProductSchema

bp_products = Blueprint('products', __name__)

@bp_products.route('/mostrar', methods=['GET'])
def mostrar():
    ps = ProductSchema(many=True)
    result = Product.query.all()
    return ps.jsonify(result), 200


@bp_products.route('/cadastrar', methods=['POST'])
def cadastrar():
    ps = ProductSchema()
    product = ps.load(request.json)

    current_app.db.session.add(product)
    current_app.db.session.commit()

    return ps.jsonify(product), 201



@bp_products.route('/modificar/<identificador>', methods=['PATCH'])
def modificar(identificador):
    ps = ProductSchema()
    query = Product.query.filter(Product.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()

    return ps.jsonify(query.first())



@bp_products.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    Product.query.filter(Product.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')
