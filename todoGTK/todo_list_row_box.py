from gi.repository import Gtk


@Gtk.Template(filename="todoGTK/ui/todo_list_box_row.glade")
class TodoListRowBox(Gtk.ListBoxRow):
    __gtype_name__ = "TodoListRowBox"

    labelTodoTitle = Gtk.Template.Child()

    def __init__(self, data):
        super(TodoListRowBox, self).__init__()
        self.labelTodoTitle.set_label(data)
