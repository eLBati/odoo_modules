from openerp import fields, models, api

class DeliveryGrid(models.Model):
    _inherit = 'delivery.grid'

    default_courier = fields.Boolean(string="Default courier")

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_default_carrier(self):
        res = self.pool.get('delivery.grid').search(self._cr, self._uid, [('default_courier', '=', True)], context=None)
        if res:
            grid = self.pool.get('delivery.grid').browse(self._cr, self._uid, res, context=None)
            if grid:

                return grid[0].carrier_id.id if grid[0].carrier_id else None
        return None

    carrier_id = fields.Many2one('delivery.carrier', string="Carrier", default=lambda self: self._get_default_carrier())
