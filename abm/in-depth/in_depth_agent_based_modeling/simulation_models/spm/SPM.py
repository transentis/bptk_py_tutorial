from BPTK_Py import Model
from BPTK_Py.widgets import WidgetLoader
from .staffMember import StaffMember
from .task import Task
from .controlling import Controlling

class SPM(Model):


    def instantiate_model(self):

        # register the agent factories

        self.register_agent_factory("staff_member", lambda agent_id, model, properties: StaffMember(agent_id, model, properties))
        self.register_agent_factory("task", lambda agent_id, model, properties: Task(agent_id, model, properties))
        self.register_agent_factory("controlling", lambda agent_id, model, properties: Controlling(agent_id, model, properties))

        # initialize some internal variables

        self._productivity=1
        self._schedule_pressure=1

    def begin_round(self, time, sim_round, step):
        # schedule pressure and productivity are updated once at the beginning of each round
        # this ensures that they are constant within each round
        # and thus the same for all staff members

        remaining_effort = 0

        # calculate the remaining effort for all open tasks

        task_ids = self.agent_ids("task")

        for task_id in task_ids:
            task = self.agent(task_id)

            if task.state == "open":
                remaining_effort += task.effort

        # now add the remaining effort for the tasks currently being worked on

        staff_ids = self.agent_ids("staff_member")

        for staff_id in staff_ids:
            task_in_progress = self.agent(staff_id).task
            if task_in_progress is not None:
                remaining_effort += task_in_progress.remaining_effort

        remaining_time = self.deadline - self.scheduler.current_time
        num_staff_members = self.agent_count("staff_member")

        if remaining_time > 0:
            self._schedule_pressure = min(remaining_effort/(remaining_time * num_staff_members), 2.5)
        elif remaining_effort > 0:
            self._schedule_pressure = min(remaining_effort/(self.dt * num_staff_members), 2.5)
        else:
            self._schedule_pressure = 1

        productivity_lookup = self.get_property("productivity")

        self._productivity = self._lookup(
                self._schedule_pressure,
                productivity_lookup["value"])



    @property
    def productivity(self):

        return self._productivity

    @property
    def schedule_pressure(self):

        return self._schedule_pressure


    def build_widget(self):
        widget_loader = WidgetLoader()
        states = {1: "in_progress", 2: "closed"}
        agents = [agent for agent in self.agents if agent.agent_type == "task"]
        
        widget_loader.create_widget("AgentStatusWidget", states=states, agents=agents)
        
        return widget_loader

