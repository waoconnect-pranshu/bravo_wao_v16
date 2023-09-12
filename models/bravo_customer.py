from odoo import api, fields, models, tools

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_number = fields.Char(string='Customer Number*')
    account_closed = fields.Boolean(string='Account Closed*')
    advertising_material = fields.Boolean(string='Customer dose not wish to receive accounting material*')
    credit_limit = fields.Integer(string='Credit Limit*')
    credit_terms_id = fields.Many2one('credit.terms', string='Credit Terms*')
    stop_account = fields.Boolean(string='Do not Offer any further Credit on this account Stop the Account*')
    warn_at = fields.Float(
        string='Warn At*',
        digits=(6, 2),  # 6 total digits with 2 decimal places (adjust as needed)
        help='Enter a percentage value.'
    )
    trading_name = fields.Char(string='Trading Name*')
    current_status = fields.Char(string='Current Status*')
    first_registered_date = fields.Date(string='First Registered Date*', help='Date of first registration')
    located_us_by = fields.Selection(
        [
            ('manufacturer', 'Manufacturer'),
            ('option2', 'Option 2'),
            ('option3', 'Option 3'),
        ],
        string='Located Us By*',
        help='Select an option from the list.', )
    managed_by = fields.Char(string='Managed By*')
    created_by = fields.Char(string='Created By*')
    created_date = fields.Date(string='Created Date*', help='Date of created date')
    manufacturer_vs_service_agent = fields.Boolean(string='This customer is manaufacturer or service agent*')
    sell_stock = fields.Boolean(string='Sell Stock*')
    sell_stock_percentage = fields.Selection(
        [
            ('5', '5%'),
            ('10', '10%'),
            ('15', '15%'),
            ('20', '20%'),
        ],
        string='Percentage*',
        help='Select the percentage for selling stock.',)
    send_changing_status = fields.Boolean(string='Sell Stock*')
    start_repair = fields.Boolean(string='Sell Stock*')
    send_contact_log = fields.Boolean(string='Sell Stock*')
    start_repair_in = fields.Date(string='Start Repair In*', help='Date of created date')
    start_sale_in = fields.Date(string='Start Sale In*', help='Date of created date')
    expiry = fields.Date(string='Expiry*', help='Date of created date')
    cvv = fields.Integer(string='CVV*')
    name_on_card = fields.Char(string='Name On Card*')
    payment_method = fields.Char(string='Payment Method*')
    use_this_account= fields.Char(string='Use this Account*')
    proforma_tax = fields.Boolean(string='When printing a sale, use Proforma invoice instead of tax invoice*')
    group_invoice = fields.Boolean(string='When printing a repair group by invoice number*')
    invoice_picking_slip = fields.Boolean(string='When printing an invoice for a sale in picking slips - print a delivery docket.*')
    warning_message = fields.Text(string="Warning Message When Account is Stopped*")
    warning_message_always = fields.Text(string="Warning Message (Always Displayed)*")