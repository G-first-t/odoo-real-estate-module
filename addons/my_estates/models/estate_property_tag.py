from odoo import models,fields


class EstatePropertyTag(models.Model):
    _name="property.tag"

    name=fields.Char('Name',required=True)