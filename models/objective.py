# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Objective(models.Model):
     _name = 'grupo3c.objective'
     
     name = fields.Char(String = "Objective", required=True)
     description = fields.Text(String = "Description", required=True)
     paramValue = fields.Char(String="Objective´s value", required=True)
     paramDesc = fields.Text(String = "Objective´s description", required=True)
     objectiveId = fields.Integer(String="objective_code", required = True)
     
     training_id = fields.One2many("grupo3c.Objective", "grupo3c.Training", String="Training_code")
     admin = fields.Many2one("res.Users", String="Trainer_identification")
     clients = fields.Many2many("res.Users", "grupo3c.Objective", String="Client_identification")