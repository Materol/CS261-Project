"""A data model for the Critical Success Factors (CSFs) of a project.

The CSFs used are the ones as defined in:

Garousi, V., Tarhan, A., Pfahl, D., Coşkunçay, A., & Demirörs, O. (2019, 03).
Correlation of critical success factors with success of software projects: an
empirical investigation. Software Quality Journal, 27, 429-493.
10.1007/s11219-018-9419-5 (https://doi.org/10.1007/s11219-018-9419-5)
"""


class CSF:

    def __init__(self, name: str, description: str, question: str):
        self.name = name
        self.description = description
        self.question = question

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


# Organizational Factors
OF1 = CSF(
    name="OF.01",
    description="Top-level management support",
    question=("What was the support level of top-level management?"),
)
OF2 = CSF(
    name="OF.02",
    description="Organizational culture and management style",
    question=("What was the type of organizational culture and management "
              "style when the project under study was conducted?"),
)
OF3 = CSF(
    name="OF.03",
    description="Vision and mission",
    question=("How well defined is/was the organizational and project vision "
              "and mission?"),
)
OF4 = CSF(
    name="OF.04",
    description="Project planning",
    question=("What was the level of organizational maturity in terms project "
              "planning in the project under study?"),
)
OF5 = CSF(
    name="OF.05",
    description="Project monitoring and controlling",
    question=("What was the level of project monitoring and controlling?"),
)
OF6 = CSF(
    name="OF.06",
    description="Organization-wide change management practices",
    question=("What was the level of Organization-wide change management "
              "practices?"),
)

# Team Factors
TF1 = CSF(
    name="TF.01",
    description="Project team commitment",
    question=("What was the level of project team commitment in the project "
              "under study?"),
)
TF2 = CSF(
    name="TF.02",
    description="Internal project communication",
    question=("What was the extent of internal project communication during the"
              " project under study?"),
)
TF3 = CSF(
    name="TF.03",
    description="Project team empowerment",
    question=("What was the level of project team empowerment in the project "
              "under study?"),
)
TF4 = CSF(
    name="TF.04",
    description="Project team's composition",
    question=("How well was the project team's composition made?"),
)
TF5 = CSF(
    name="TF.05",
    description=("Project team's general expertise (e.g., in general software "
                 "engineering concepts and project management)"),
    question=("What was the average level of team members' general expertise "
              "and competency in general software engineering concepts?"),
)
TF6 = CSF(
    name="TF.06",
    description="Project team's expertise with the task",
    question=("What was the average level of team members' expertise and "
              "competency with the tasks assigned within the project?"),
)
TF7 = CSF(
    name="TF.07",
    description=("Project team's experience with the software development "
                 "methodologies"),
    question=("What was the average level of team members' experience with the"
              " software development methodologies used in the project?"),
)

# Customer Factors
CF1 = CSF(
    name="CF.01",
    description="User (client) participation",
    question=("What was the level of User (client) participation/involvement in"
              " the project?"),
)
CF2 = CSF(
    name="CF.02",
    description="User (client) support",
    question=("What was the level of User (client) support in the project?"),
)
CF3 = CSF(
    name="CF.03",
    description="Customer skill, training and education in IT",
    question=("What was the level of customer skills, training and education in"
              " IT in general?"),
)
CF4 = CSF(
    name="CF.04",
    description="Customer (client) experience in their own business domain",
    question=("What was the level of customer (client) experience in their own "
              "business domain?"),
)

# Project Factors
PF1 = CSF(
    name="PF.01",
    description="Technological uncertainty",
    question=(
        "What was the level of technological uncertainty in the project?"),
)
PF2 = CSF(
    name="PF.02",
    description="Project complexity",
    question=("What was the level of project complexity?"),
)
PF3 = CSF(
    name="PF.03",
    description="Urgency",
    question=("What was the level of urgency during the project overall?"),
)
PF4 = CSF(
    name="PF.04",
    description="Relative project size",
    question=("What was the project size in terms of number of team members?"),
)
PF5 = CSF(
    name="PF.05",
    description="Specifications changes",
    question=("What was the level of requirement specification changes during "
              "the project?"),
)
PF6 = CSF(
    name="PF.06",
    description="Project criticality",
    question=("What was the level of project criticality?"),
)
PF7 = CSF(
    name="PF.07",
    description="Software development methodologies",
    question=("What type of software development methodologies was used in the "
              "project?"),
)

ALL_CSFS = [OF1, OF2, OF3, OF4, OF5, OF6]
ALL_CSFS += [TF1, TF2, TF3, TF4, TF5, TF6, TF7]
ALL_CSFS += [CF1, CF2, CF3, CF4]
ALL_CSFS += [PF1, PF2, PF3, PF4, PF5, PF6, PF7]
