from tkinter import Tk

from views.view import Application


def main():
    # Sets up the root widget
    root = Tk()
    app = Application(root)

    # Runs the event loop
    app.mainloop()


if __name__ == '__main__':
    main()