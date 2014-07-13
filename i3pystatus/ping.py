# -*- coding:utf-8 -*-

from i3pystatus import IntervalModule
from subprocess import Popen, PIPE
from re import search

class Ping(IntervalModule):
    """
    Module to display ping
    Linux only

    Available formatters:

    {pingtime}

    """

    format = "{pingtime:4.0f}ms"
    settings = (
        ("target", "server to ping"),
        ("interval", "interval between pings"),
        ("warning_limit", "pingtime above which warning_color is used")
    )

    color   = "#ffffff"
    target  = "8.8.8.8"
    interval= 6

    warning_color = "#ffa500"
    error_color = "#ff0000"
    warning_limit = 100



    def run(self):

        pingtime = -1
        color = self.color
    
        # Command and output not portable, unix only
        ping = Popen(
                ["ping", "-c", "1", "-W", "1",  self.target],
                stdout = PIPE,
                stderr = PIPE
        )
        out, _ = ping.communicate()
        
        regex= '= '+'/'.join(['([0-9\.]+)'] * 4)
        values=search(regex, out.decode('utf-8')) if out else None

        if values:
            # Values are truncated to ms
            pingtime = int(values.group(1).split('.')[0])
            if pingtime > self.warning_limit :
                color = self.warning_color
        else :
            color = self.error_color

        self.output = {
            "full_text": self.format.format(pingtime=pingtime) if values else "ping",
            "color": color,
        }
    

    # Allow users to ping manually by clicking
    on_leftclick=run    
