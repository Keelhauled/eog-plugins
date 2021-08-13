from gi.repository import GObject, Eog, GLib

class AutoFullscreen(GObject.Object, Eog.WindowActivatable):
    
    window = GObject.property(type=Eog.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self.window.connect('draw', self.test)

    def do_deactivate(self):
        pass

    def test(self, window, state):
        self.window.disconnect_by_func(self.test)
        self.fullscreen()

    def fullscreen(self):
        self.window.change_action_state("view-fullscreen", GLib.Variant("b", True))
