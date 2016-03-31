from openerp import api, fields, models, _


class __OERPMODULE_CLASS_NAME__(models.Model):
    """
    Need to set the model description
    """

    _name = '__OERPMODULE_MODEL_NAME__'
    _description = 'Need to set the model name'

    name = fields.Char(
            'Name',
            required=True,
            size=64,
            help='help string')
