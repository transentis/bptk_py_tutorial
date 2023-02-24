from BPTK_Py import sd_functions as sd
from BPTK_Py import Module

class Projects(Module):
    def __init__(self, model, name):
        super().__init__(model, name)

        # Exports
        
        self.projects = self.stock("projects")
        self.deliveringProjects = self.flow("deliveringProjects")
        self.prospectingEffort = self.converter("prospectingEffort")
        self.projectVolume = self.converter("projectVolume")
    
    def initialize(self,staff):
        proposals = self.stock("proposals")
        prospectingProjects = self.flow("prospectingProjects")
        winningProjects = self.flow("winningProjects")
        proposalRate = self.converter("proposalRate")
        projectAcquisitionDuration = self.converter("projectAcquisitionDuration")
        projectDeliveryRate = self.converter("projectDeliveryRate")

        self.projects.initial_value = 320.0
        self.projects.equation = -self.deliveringProjects+winningProjects
        self.deliveringProjects.equation = sd.min(projectDeliveryRate,self.projects)
        projectDeliveryRate.equation = staff.projectDeliveryCapacity

        proposals.initial_value = 320.0
        proposals.equation=prospectingProjects-winningProjects

        self.prospectingEffort.equation = 4.0
        self.projectVolume.equation = 16.0
        proposalRate.equation = self.projectVolume * (staff.businessDevelopmentCapacity/self.prospectingEffort)
        prospectingProjects.equation = proposalRate
        projectAcquisitionDuration.equation = 6.0
        winningProjects.equation = sd.min(sd.delay(self.model,prospectingProjects,projectAcquisitionDuration,160.0),proposals)