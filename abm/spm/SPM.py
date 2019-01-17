from BPTK_Py import Model
from BPTK_Py.widgets import WidgetLoader
from .staffMember import StaffMember
from .task import Task

class SPM(Model):

    @property
    def productivity(self):

        productivity_lookup = self.get_property("productivity")

        productivity = self.dt * self.lookup(
                x=self.schedule_pressure,
                points=productivity_lookup["value"])

        return productivity

    @property
    def schedule_pressure(self):
        remaining_time = self.deadline - self.scheduler.current_time
        num_staff_members = self.agent_count("staffMember")
        remaining_effort = 0

        # calculate the remaining effort for all open tasks

        task_ids = self.agent_ids("task")

        for task_id in task_ids:
            task = self.agent(task_id)

            if task.state == "open":
                remaining_effort += task.effort

        # now add the remaining effort for the tasks currently being worked on

        staff_ids = self.agent_ids("staffMember")

        for staff_id in staff_ids:
            task_in_progress = self.agent(staff_id).task
            remaining_effort += task_in_progress.remaining_effort

        schedule_pressure = remaining_effort/(remaining_time * num_staff_members) if remaining_time > 0 else 2.5

        return schedule_pressure


    def instantiate_model(self):
        self.register_agent_factory("staffMember", lambda agent_id, model, properties: StaffMember(agent_id, model, properties))
        self.register_agent_factory("task", lambda agent_id, model, properties: Task(agent_id, model, properties))


    def build_widget(self):
        widget_loader = WidgetLoader()
        states = {1: "inProgress", 2: "closed"}
        agents = [agent for agent in self.agents if isinstance(agent, Task)]
        
        widget_loader.create_widget("AgentStatusWidget", states=states, agents=agents)
        
        return widget_loader

