# -*- coding:utf-8 -*-

from i3pystatus import Module
from pythonscripts.i3shiftworkspaces import shift_workspaces

class i3shift(Module):
    """
    Simple shortcut to i3shiftworkspaces module.
    """

    output= {
        "full_text": "<<<<",
    }

    def on_leftclick(self):
        shift_workspaces(9,False)

