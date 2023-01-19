# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Objective(models.Model):
    _name = 'grupo3c.objective'
     
    name = fields.Char(string = "Objective", required=True)
    description = fields.Text(string = "Description", required=True)
    paramValue = fields.Char(string="Objectives value", required=True)
    paramDesc = fields.Text(string = "Objectives description", required=True)
     
    training_id = fields.One2many("grupo3c.training", "objectiveId", string="Training_code")
    admin = fields.Many2one("res.users", string="Trainer_identification")
    clients = fields.Many2many("res.users", string="Client_identification")