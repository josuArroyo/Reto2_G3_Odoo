# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.



from odoo import models, fields, api

class Training(models.Model):
     _name = 'grupo3c.Training'
     
     trainingId = fields.Integer(required=True, string= "trainingId")
     description = fields.Text(required=True, string= "description")
     duration = fields.Float(required=True, string= "duration")
    periodTime = fields.Float(required=True, string= "periodTime")
    intensity = fields.Integer(required=True, string= "intensity")
    repeats = fields.Integer(required=True, string= "repeats")
    objectiveId = fields.Many2One("grupo3c.objective", string= "objectiveId")
    admin_ids = fields.Many2One ("res.Users", string= "admin_ids")

    

