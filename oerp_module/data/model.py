from openerp.osv import fields, osv, orm
from openerp.tools.translate import _
from openerp import tools

class __OERPMODULE_CLASS_NAME__(osv.Model):
    """
    Need to set the model description
    """

    _name = '__OERPMODULE_MODEL_NAME__'
    _description = 'Need to set the model name'
    _columns = {
        'name': fields.char(
            'Name',
            required=True,
            size=64,
            help='help string'),
    }

    _defaults = {
    }
