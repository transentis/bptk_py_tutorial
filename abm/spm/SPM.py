from BPTK_Py import ABModel
from .staffMember import StaffMember
from .task import Task


class SPM(ABModel):

    def effort_per_task(self):
        return self.get_property("effortPerTask")["value"]

    def deadline(self):
        return self.get_property("deadline")["value"]

    def productivity(self):

        productivity_lookup = self.get_property("productivity")

        productivity = self.dt * self.lookup(
                x=self.schedule_pressure(),
            points=productivity_lookup["value"])

        return productivity

    def schedule_pressure(self):

        remaining_time = self.deadline() - self.scheduler.current_time
        num_open_tasks = self.agent_count_per_state(Task.TYPE, Task.STATES["OPEN"])
        effort_per_task = self.effort_per_task()
        num_staff_members = self.agent_count(StaffMember.TYPE)
        remaining_effort_tasks_in_progress = 0

        agent_ids = self.agent_ids(StaffMember.TYPE)

        for agent_id in agent_ids:

            task_in_progress = self.agent(agent_id).current_task()

            remaining_effort_tasks_in_progress += task_in_progress.remaining_effort()

        remaining_effort = effort_per_task * num_open_tasks+remaining_effort_tasks_in_progress

        schedule_pressure = remaining_effort/(remaining_time*num_staff_members) if remaining_time > 0 else 2.5

        return schedule_pressure


    def instantiate_model(self):
        self.register_agent_factory(StaffMember.TYPE, lambda agent_id, scenario: StaffMember(agent_id, scenario))
        self.register_agent_factory(Task.TYPE, lambda agent_id, scenario: Task(agent_id, scenario))
