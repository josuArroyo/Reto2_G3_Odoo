

from odoo import models, fields, api
from odoo import exceptions

class Event(models.Model):
    _name = 'grupo3c.event'

    eventType = fields.Char(string = "Event Type", required = True)
    description = fields.Text(string = "Description", required = True)
    numPart = fields.Integer(string= "Number of Participants", required = True)
    date = fields.Date(string = "Date", required = True)
    
    
    admins = fields.Many2one('res.users',string="Organizer")
    customer_id = fields.Many2many('res.users', string = "Customers")
    place_id = fields.Many2one('grupo3c.place', string= "Place")
    
    
    @api.constrains('date')
    def _validate_date(self):
        for event in self:
            if fields.Date.from_string(event.date) < fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("Date cannot be lower than the actual one")       
    
    
    @api.onchange('description')
    def _onchange_description(self):
        if len(str(self.description)) > 100:
            return{
        'warning' : {
            'title' : "Something bad happened",
            'message' : "You have reached the maximun characters allowed: 100"
            }
        }
            
    @api.onchange('eventType')
    def _onchange_eventType(self):
        if len(str(self.eventType)) > 100:
            return{
        'warning' : {
            'title' : "Something bad happened",
            'message' : "You have reached the maximun characters allowed: 100"
            }
        }