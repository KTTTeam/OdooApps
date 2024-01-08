# -*- coding: utf-8 -*-
{
    'name': "Telegram Integration",
    'summary': """
        KTT telegram integration with project module.
    """,
    'description': """
    KTT telegram module help not
    """,
    'author': "KTT Team",
    'maintainer': 'Mai Văn Khai',
    'website': "https://kkt.io.vn",
    "license": "OPL-1",
    'images': ['images/demo.gif'],
    'category': 'KTT/KTT',
    'version': '17.1.0.1',

    # DEPENDS MODULES
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # ============================================================================================================
        # DATA
        # ============================================================================================================
        # SECURITY SETTING - GROUP - PROFILE

        # ============================================================================================================
        # WIZARD
        # ============================================================================================================
        # VIEWS
        'views/project_project_views.xml',
        'views/project_task_views.xml',
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
    'price': 9.99,
    'currency': 'USD'
}
