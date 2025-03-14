from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.category import CategoryModel
from schemas.category import CategoryArgsSchema, CategorySchema

blp = Blueprint("Categories", "categories", description="Opetations on categories")

@blp.route('/category')
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()
    
    @blp.arguments(CategoryArgsSchema)
    @blp.response(201, CategorySchema)
    def post(self, args):
        category = CategoryModel(**args)

        try:
            db.session.add(category)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the category.")


