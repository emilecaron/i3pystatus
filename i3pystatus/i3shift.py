# -*- coding:utf-8 -*-

from i3pystatus import IntervalModule
from pythonscripts.i3shiftworkspaces import shift_workspaces, leftshift_possible

class i3shift(IntervalModule):
    """
    Simple shortcut to i3shiftworkspaces module.
    """

    def run(self):
        possible = leftshit_possible()
        self.output= {
            "full_text": "<<<<" if possible else "<gap<",
            "color": "#ff0000" if possible else "#ffffff",
        }


    def on_leftclick(self):
        shift_workspaces(9,False)
        self.run()

