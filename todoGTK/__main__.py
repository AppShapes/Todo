import gi
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from todoGTK.todo_application import TodoApplication


def main():
    app = TodoApplication()
    app.run(sys.argv)


if __name__ == "__main__":
    main()