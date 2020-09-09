from gi.repository import Gtk, Gio, GLib

from todoGTK.todo_list_row_box import TodoListRowBox


@Gtk.Template(filename="todoGTK/ui/todo_window.glade")
class TodoWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "TodoWindow"

    listBoxTodo = Gtk.Template.Child()
    entryTodoNew = Gtk.Template.Child()

    def __init__(self, app):
        super(TodoWindow, self).__init__(title="Shapes TODO", application=app)

        show_action = Gio.SimpleAction.new_stateful(
            "show", None, GLib.Variant.new_boolean(False)
        )
        show_action.connect("change-state", self.on_show)
        self.add_action(show_action)

    def on_show(self, action, param):
        print("show")

    @Gtk.Template.Callback()
    def on_add_clicked(self, widget):
        self.listBoxTodo.add(TodoListRowBox(self.entryTodoNew.get_text()))
        self.listBoxTodo.show_all()
        print("add")