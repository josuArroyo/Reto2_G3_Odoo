# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.



from odoo import models, fields, api

class Training(models.Model):
    _name = 'grupo3c.training'
     
    trainingId = fields.Integer( )
    description = fields.Text()
    duration = fields.Float()
    periodTime = fields.Float()
    intensity = fields.Integer()
    repeats = fields.Integer()
    objectiveId = fields.Many2one("grupo3c.objective", string= "Objective Id")
    admin_ids = fields.Many2one ("res.Users", string= "Admin ids")

    

