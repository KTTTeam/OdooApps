# -*- coding: utf-8 -*-
# 1 : imports of python lib
import base64
import io
import logging
from io import BytesIO
import random
from PIL import Image, ImageDraw, ImageFont
from requests import post,put,patch,delete
import string
from json import dumps
from datetime import datetime, timedelta
# 2 : imports of odoo
import odoo
from odoo import api, fields, models, modules, _
from odoo.tools.safe_eval import safe_eval as eval
from odoo.tools.misc import file_path
# 3 : imports from odoo addons


_logger = logging.getLogger(__name__)


class Task(models.Model):
    
    _inherit = ['project.task']

    google_workspace_webhook = fields.Char(
        string="Webhook",
        related='project_id.google_workspace_webhook'
    )
    thread_message_id = fields.Char(
        string="Thread Key",
        default="".join(random.choice(string.ascii_letters) for char in range(16)),
        readonly=True,
    )
    card_message_id = fields.Char(
        string="Card",
        readonly=True,
        default="".join(random.choice(string.ascii_letters) for char in range(16)),
    )
    def create(self, vals_list):
        task =  super(Task,self).create(vals_list)
        if task.google_workspace_webhook and task.project_id.is_created_task:
            task._send_messages_to_google_workspace(info={'title':'Create new task','content': ''})
        return task

    def write(self, vals):
        self._send_messages_to_google_workspace(info={'title':'Task updated','content': 'Newly updated task'})
        return super(Task,self).write(vals)
    
    def unlink(self):
        return super(Task,self).unlink()

    def _get_url(self, view='form'):
        """
            # ** Description **
            # - Prepare path direction to form view task
            # - Combine params (menu,action,view,model,self)
            # @return: url
        """
        action = self.env.ref('project.act_project_project_2_project_task_all')
        menu = self.env.ref("project.menu_main_pm")
        active = self._context.get('active_id')
        if not active:
            active = 1
        return "%s/web#id=%s&menu_id=%s&cids=1&action=%s&model" \
              "=%s&view_type=%s&active_id=%s" \
              % (
                  self.env['ir.config_parameter'].sudo(
                  ).get_param('web.base.url'),
                  self.id,
                  menu.id,
                  action.id,
                  self._name,
                  view,
                  active,
              )

    def _get_avatar(self):
        user = self.env.user
        if user.image_128:
            stream = io.BytesIO()
            Image.open(io.BytesIO(base64.b64decode(user.avatar_128))).resize((64, 64)).save(stream, format='PNG')
            img = str(base64.b64encode(stream.getvalue()))
            return f"data:image/png;base64,{img[2:-1]}"
        # If end-user not set avatar so we must be get avatar default
        avatar = Image.open(file_path('ktt_google_workspace_project/static/src/img/avatar.png',filter_ext=('.png','jpg')))
        buffered = BytesIO()
        avatar.save(buffered, format="PNG")
        bytes_i = str(base64.b64encode(buffered.getvalue()))
        return f"data:image/png;base64,{bytes_i[2:-1]}"

    def _get_card_message(self,info):
        """
            # ** Description **
            # - Prepare card message updated
            # - Purpose: use by send request
            # @returns: headers, and message card.
        """
        user = self.env.user
        message = {
            "cardsV2": [
                {
                    "cardId": self.card_message_id,
                    "card": {
                        "header": {
                            "title": info.get('title'),
                            "subtitle": user.partner_id.name or False,
                            "imageUrl": self._get_avatar(),
                            "imageType": "CIRCLE",
                            "imageAltText": f"Avatar for "
                                            f"{user.name}",
                        },
                        "sections": [
                            {
                                "header": f"<font color=\"#00000\"><strong>{self.name}</strong></font>",
                                "collapsible": True,
                                "uncollapsibleWidgetsCount": 3,
                                "widgets": [
                                    {
                                        "decoratedText": {
                                            "text": info.get('content'),
                                        }
                                    },
                                    {
                                        "buttonList": {
                                            "buttons": [
                                                {
                                                    "text": "Xem",
                                                    "onClick": {
                                                        "openLink": {
                                                            "url": self._get_url()
                                                        }
                                                    }
                                                },
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
        }
        return headers, message
    

    @api.model
    def _send_messages_to_google_workspace(self,info):
        """
            # ** Description **
            # - Send request from odoo to google workspace via request
            # - Purpose: Send card message
            # - Conditional occur: networking available, webhook, and task current,
            #   opposite raise Validation message
        """
        try:
            headers,message = self._get_card_message(info)
            uri = self._format_uri(self.google_workspace_webhook)
            response = post(url=uri,data=dumps(message),headers=headers)
            return response
        except Exception as error:
            _logger.error(msg=error)
    
    @api.model
    def _format_uri(self,webhook):
        l = webhook.split("?")
        return f"{l[0]}?threadKey={self.thread_message_id}&{l[1]}&messageReplyOption=REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD"
