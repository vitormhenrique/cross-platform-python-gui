from kivy.properties import ListProperty, StringProperty

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

import os
import sys
import django
from django.apps import apps




class RallyOverviewScreen(MDScreen):
    
    def test(self):

        BASE_DIR = '/Users/vitormhenrique/dev/lancium_smart_response'
        sys.path.append(BASE_DIR)
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

        django.setup()

        DataCenter = apps.get_model('datacenter', 'DataCenter')

        dc = DataCenter.objects.get(is_main_server=True)

        self.ids.md_label_title.text = dc.name



class OverviewBox(MDBoxLayout):
    title = StringProperty()
    money = StringProperty()
    text = ListProperty(["", "", ""])
    secondary_text = ListProperty(["", "", ""])
    tertiary_text = ListProperty(["", "", ""])
    bar_color = ListProperty([(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)])
