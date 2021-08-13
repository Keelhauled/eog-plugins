from gi.repository import GObject, Eog, Gio

class FastClose(GObject.Object, Eog.WindowActivatable):
    
    window = GObject.property(type=Eog.Window)
    ACTION_NAME = 'close-now'

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        app = Eog.Application.get_instance()
        app.set_accels_for_action('win.' + self.ACTION_NAME, ['Escape', None])
        self.setup_action(self.ACTION_NAME, lambda x, y: self.window.close())

    def do_deactivate(self):
        pass

    def setup_action(self, name, cb):
        action = Gio.SimpleAction(name=name)
        action.connect("activate", cb)
        self.window.add_action(action)
        return action
