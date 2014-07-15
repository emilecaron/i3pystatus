from i3pystatus import Module
from pythonscripts import i3

class I3Focus(Module):
    """
    Module to display focused window

    Available formatters:

    {name}
    ...
    """
    format = "{name:20}"
    color = "#00ff00"

    output= {
        "full_text": "",
        "color": color,
    }

    
    def __init__(self):
        """ 
        Register a handler on window focus events
        """
        super().__init__()
        self.sub = i3.Subscription(self.windowHandler, 'window', 'focus', daemon=True)

        #TODO add a call to i3 to get currently focused window


    def windowHandler(self, event, data, suscription):

        try :
            # TODO: add other formatting options

            #print("window name={}".format(event['container']['name']))
            #print("window focus={}".format(event['container']['focus']))
            #print("window focused={}".format(event['container']['focused']))
            #print("window id={}".format(event['container']['id']))
            #print("window nodes={}".format(event['container']['nodes']))

            container = event['container']
            name = container.get('name', '')

            self.output['full_text']=self.format.format(
                name= name 
            )
        except Exception as e: #TODO check error types
            self.output['full_text']='Error (Socket going down)'
            self.sub.close()
