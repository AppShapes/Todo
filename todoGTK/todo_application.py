from gi.repository import Gtk, Gio
from todoGTK.todo_window import TodoWindow


class TodoApplication(Gtk.Application):
    def __init__(self):
        super(TodoApplication, self).__init__()
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = TodoWindow(self)

        self.window.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # Actions
        open_action = Gio.SimpleAction.new("open", None)
        open_action.connect("activate", self.on_open)
        self.add_action(open_action)

        new_action = Gio.SimpleAction.new("new", None)
        new_action.connect("activate", self.on_new)
        self.add_action(new_action)

    def on_open(self, action, param):
        print("open")

    def on_new(self, action, param):
        print("new")