# -*- coding: utf-8 -*-
# 1 : imports of python lib
import base64
import io
import logging
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import httplib2
from json import dumps
from datetime import datetime, timedelta
# 2 : imports of odoo
import odoo
from odoo import api, fields, models, modules, _
from odoo.tools.safe_eval import safe_eval as eval
# 3 : imports from odoo addons

class Project(models.Model):

    _inherit = ['project.project']

    is_created_task = fields.Boolean(
        string="Task Created",
        default = False
    )  

    is_edited_task = fields.Boolean(
        string="Task Edited",
        default = False
    )  

    is_removed_task = fields.Boolean(
        string="Task Removed",
        default = False
    ) 
    google_workspace_webhook = fields.Char(
        string="Webhook"
    )

    
