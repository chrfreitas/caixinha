from marshmallow import Schema, fields

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()

class CategoryArgsSchema(Schema):
    name = fields.String()