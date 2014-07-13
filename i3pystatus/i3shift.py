# -*- coding:utf-8 -*-

from i3pystatus import IntervalModule
from pythonscripts.i3shiftworkspaces import shift_workspaces, leftshift_possible

class i3shift(IntervalModule):
    """
    Simple shortcut to i3shiftworkspaces module.
    """

    def run(self):
        self.output= {
            "full_text": "<<<<",
            "color": "#ff0000" if leftshift_possible() else "#ffffff",
        }


    def on_leftclick(self):
        shift_workspaces(9,False)
        self.run()

