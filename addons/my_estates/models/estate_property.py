from odoo import fields,models

class Property(models.Model):
      _name="property.type"

      name=fields.Char(string="Name",required=True)
      