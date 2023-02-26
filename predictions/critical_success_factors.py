"""A data model for the Critical Success Factors (CSFs) of a project.

The CSFs used are the ones as defined in:

Garousi, V., Tarhan, A., Pfahl, D., Coşkunçay, A., & Demirörs, O. (2019, 03).
Correlation of critical success factors with success of software projects: an
empirical investigation. Software Quality Journal, 27, 429-493.
10.1007/s11219-018-9419-5 (https://doi.org/10.1007/s11219-018-9419-5)
"""


class CSF:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)


# Organizational Factors
OF1 = CSF("OF.01", "Top-level management support")
OF2 = CSF("OF.02", "Organizational culture and management style")
OF3 = CSF("OF.03", "Vision and mission")
OF4 = CSF("OF.04", "Project planning")
OF5 = CSF("OF.05", "Project monitoring and controlling")
OF6 = CSF("OF.06", "Organization-wide change management practices")

# Team Factors
TF1 = CSF("TF.01", "Project team commitment")
TF2 = CSF("TF.02", "Internal project communication")
TF3 = CSF("TF.03", "Project team empowerment")
TF4 = CSF("TF.04", "Project team's composition")
TF5 = CSF(
    "TF.05",
    ("Project team's general expertise (e.g., in general software engineering "
     "concepts and project management)"),
)
TF6 = CSF("TF.06", "Project team's expertise with the task")
TF7 = CSF(
    "TF.07",
    "Project team's experience with the software development methodologies",
)

# Customer Factors
CF1 = CSF("CF.01", "User (client) participation")
CF2 = CSF("CF.02", "User (client) support")
CF3 = CSF("CF.03", "Customer skill, training and education in IT")
CF4 = CSF("CF.04", "Customer (client) experience in their own business domain")

# Project Factors
PF1 = CSF("PF.01", "Technological uncertainty")
PF2 = CSF("PF.02", "Project complexity")
PF3 = CSF("PF.03", "Urgency")
PF4 = CSF("PF.04", "Relative project size")
PF5 = CSF("PF.05", "Specifications changes")
PF6 = CSF("PF.06", "Project criticality")
PF7 = CSF("PF.07", "Software development methodologies")

ALL_CSFS = [OF1, OF2, OF3, OF4, OF5, OF6]
ALL_CSFS += [TF1, TF2, TF3, TF4, TF5, TF6, TF7]
ALL_CSFS += [CF1, CF2, CF3, CF4]
ALL_CSFS += [PF1, PF2, PF3, PF4, PF5, PF6, PF7]
