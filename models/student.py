from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class StudentStudent(models.Model):
    _name = "student.student"
    _order = "name"
    _description = "Student"

    roll = fields.Char(string="Roll Number", required=True)
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(required=True)
      
        
    Number1 = fields.Integer(string='Number1')
    Number2 = fields.Integer(string='Number2')

    is_pass = fields.Boolean(compute = "_compute_name", store=True)
    is_fail = fields.Boolean(compute = "_compute_name", store=True)

    teacher_id = fields.Many2one('teacher.teacher', string="Teacher")
    management_id = fields.Many2one('management.management', string="Management")

    @api.depends('Number1','Number2')    
    def _compute_name(self):
        self.is_pass = False
        self.is_fail = False
       

        if self.Number1 + self.Number2 > 40 :            
            self.is_pass = True
        else:
            self.is_fail = True

    @api.onchange('age')
    def _onchange_age(self):
        if self.age > 30:
            raise ValidationError(_("Age must be less than 30"))
        
    @api.constrains('age')
    def _age_check(self):
        if self.age<0:
            raise ValidationError(_("Age can't be Negative"))

       
        
