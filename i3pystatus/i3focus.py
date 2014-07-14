from i3pystatus import Module
import i3

# Poney patching > Monkey patching
i3.EVENT_TYPES.append('window')
i3.MSG_TYPES.append('get_window')
i3.Subscription.type_translation['window']='get_window'
i3.Subscription.daemon=True

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

    # TODO alive flag, wont change if script 'frozen'
    it = 0
    
    def __init__(self):
        """ 
        Register a handler on window focus events
        """
        super().__init__()
        self.sub = i3.Subscription(self.windowHandler, 'window', 'focus')
        #TODO add a call to i3 to get currently focused window


    def windowHandler(self, event, data, suscription):
        #TODO remove it
        self.it += 1
        
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
                name= name + ' (' + str(self.it%10) + ')'
            )
        except : #TODO check error types
            self.output['full_text']='Error (Socket going down)'
            self.sub.close()
