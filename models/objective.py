# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Objective(models.Model):
    _name = 'grupo3c.objective'
     
    name = fields.Char(string = "Objective", required=True)
    description = fields.Text(string = "Description", required=True)
    paramValue = fields.Char(string="Param value", required=True)
    paramDesc = fields.Text(string = "Parameters description", required=True)
     
    training_id = fields.One2many("grupo3c.training", "objectiveId", string="Training_code")
    admin = fields.Many2one("res.users", string="Trainer_identification")
    clients = fields.Many2many("res.users", string="Client_identification")
    
    @api.onchange('description')
    def _onchange_description(self):
        if len(str(self.description)) > 100:
            return{
        'warning' : {
            'title':"something bad happened",
            'message':"you have reached the maximum characters allowed"
            }
        }
    @api.constrains('paramValue')
    def _validate_paramvalue(self):
        for objective in self:
             if len(str(self.paramValue)) > 15:
                raise exceptions.ValidationError("you have reached the maximum characters allowed")