import time
import ipywidgets as widgets
from IPython.display import display
import threading

from abm.spm.task import Task

class taskStatusWidget():

    def __init__(self, tasks):
        self.tasks = tasks
        self.thread = threading.Thread(target=self.monitor_tasks)
        self.running = False

        button_layout = widgets.Layout(width="5%")

        # main_vbox = widgets.VBox()
        self.buttons = []
        for i in range(0, len(tasks)):
            self.buttons += [widgets.Button(description=str(i + 1), button_style='info', layout=button_layout)]

        hboxes = []
        for i in range(0, len(self.buttons) + 1, 10):

            buttons_tmp = []
            to = i + 10 if len(self.buttons) - i > 10 else len(self.buttons)

            for j in range(i, to):
                button = self.buttons[j]

                buttons_tmp += [button]

            hboxes += [widgets.HBox(children=buttons_tmp)]

        main_Vbox = widgets.VBox(children=hboxes)
        display(main_Vbox)

    def start(self):
        self.running = True
        self.thread.start()

    def stop(self):
        self.running = False

    def monitor_tasks(self):
        while self.running:

            for i in range(0, len(self.tasks)):
                if self.tasks[i].state == Task.STATES["IN_PROGRESS"]:
                    self.buttons[i].button_style = 'warning'
                if self.tasks[i].state == Task.STATES["CLOSED"]:
                    self.buttons[i].button_style = 'danger'

            time.sleep(1)


