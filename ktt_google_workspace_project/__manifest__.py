# -*- coding: utf-8 -*-
{
    'name': "Google Workspace Integration",
    'summary': """
        KTT Google Workspace integration with project module.
    """,
    'description': """
        This module will be push notification to Google Workspace via webhook application.
        For examples: Created, Updated, Deleted each trigger event.
    """,
    'author': "KTT Team",
    'maintainer': 'Bùi Đức Tuấn',
    'website': "https://ktt.io.vn",
    "license": "OPL-1",
    'images': ['images/google_and_odoo.gif'],
    'category': 'KTT/Google Workspace',
    'version': '17.0.1.0.1',

    # DEPENDS MODULES
    'depends': ['base','project'],

    # ALWAYS LOADING...
    'data': [
        # ============================================================================================================
        # DATA
        # ============================================================================================================
        # GROUP - SECURITY SETTING - PROFILE

        # ============================================================================================================
        # WIZARD
        # ============================================================================================================
        # VIEWS
        'views/project_views.xml',
        'views/task_views.xml',
        # ============================================================================================================
        # REPORT
        # ============================================================================================================
        # MENU - ACTION
        # ============================================================================================================
        # FUNCTION USE TO UPDATE DATA LIKE POST OBJECT
        # ============================================================================================================
    ],
    'application': False,
    'installable': True,
    'price': 5.0,
    'currency': 'USD'
}
