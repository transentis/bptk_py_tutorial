

from BPTK_Py import Model
from BPTK_Py import sd_functions as sd

class simulation(Model):

    def __init__(self):

        # Never forget calling the super method to initialize the main parameters
        super().__init__(starttime=0,stoptime=120,dt=1,name ='SimpleProjectManagament_scenario80' )


        # Now we define the equations

        # Stocks
        openTasks = self.stock("openTasks")
        closedTasks = self.stock("closedTasks")
        staff = self.stock("staff")

        # Flows
        completionRate = self.flow("completionRate")


        # Converters
        currentTime = self.converter("currentTime")
        remainingTime = self.converter("remainingTime")
        schedulePressure = self.converter("schedulePressure")
        productivity = self.converter("productivity")

        # Constants
        deadline = self.constant("deadline")
        effortPerTask = self.constant("effortPerTask")
        initialStaff = self.constant("initialStaff")
        initialOpenTasks = self.constant("initialOpenTasks")

        # Actual Logic

        openTasks.initial_value = 100.0
        closedTasks.initial_value = 0.0  # not really necessary, but I like to be explicit

        staff.initial_value = initialStaff  # I prefer using constants to initialize non-zero stocks
        openTasks.initial_value = initialOpenTasks

        deadline.equation = 100.0
        effortPerTask.equation = 1.0
        initialStaff.equation = 1.0
        initialOpenTasks.equation = 80.0

        currentTime.equation = sd.time()

        remainingTime.equation = deadline - currentTime

        openTasks.equation = -completionRate
        closedTasks.equation = completionRate

        schedulePressure.equation = sd.min((openTasks * effortPerTask) / (staff * sd.max(remainingTime, 1.0)), 2.5)

        # Graphical function
        self.points["productivity"] = [[0.0, 0.4], [0.25, 0.444], [0.5, 0.506], [0.75, 0.594], [1, 1], [1.25, 1.119],
                                        [1.5, 1.1625], [1.75, 1.2125], [2, 1.2375], [2.25, 1.245], [2.5, 1.25]]

        productivity.equation = sd.lookup(schedulePressure, "productivity")

        completionRate.equation = sd.max(0, sd.min(openTasks, staff * (productivity / effortPerTask)))