from odoo import models, fields, api


class KttProject(models.Model):
    _inherit = 'project.project'
    
    # Fields for telegram api
    telelegram_token = fields.Char(string="Telegram Token")
    chat_id = fields.Char(string="Chanel/Group Telegram")
    is_nof_telegram_task_created = fields.Boolean(string="Notification Task Created", default=False, help="When task is created send notification to telegram.")
    is_nof_telegram_task_edited = fields.Boolean(string="Notification Task Edited", default=False, help="When task is edited send notification to telegram.")
    is_nof_telegram_task_deleted = fields.Boolean(string="Notification Task Deleted", default=False, help="When task is deleted send notification to telegram.")