"""Define success metrics for software projects.

Projects are considered good if the values of success metrics are high. We use
CSFs to predict the values of success metrics. Failed projects are those that
have low values of success metrics. Risky projects are projects that are
*predicted* to have low values of success metrics.

We use the success metrics as defined in:

Garousi, V., Tarhan, A., Pfahl, D., Coşkunçay, A., & Demirörs, O. (2019, 03).
Correlation of critical success factors with success of software projects: an
empirical investigation. Software Quality Journal, 27, 429-493.
10.1007/s11219-018-9419-5 (https://doi.org/10.1007/s11219-018-9419-5)
"""


class SuccessMetric:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)


# Characteristics of the process
PROCESS_1 = SuccessMetric(
    name='budget',
    description=('To what extent did the project finish on budget?'),
)
PROCESS_2 = SuccessMetric(
    name='schedule',
    description=('To what extent did the project finish on schedule/time?'),
)
PROCESS_3 = SuccessMetric(
    name='scope',
    description=('To what extent did the project conform to the '
                 'initially-defined scope (features)?'),
)
PROCESS_4 = SuccessMetric(
    name='team_building_and_dynamics',
    description=('To what extent has the project been influential in positive '
                 'team building, team dynamics, and enhancing team members\' '
                 'opinions about each other?'),
)

# Characteristics of the resulting product/service
PRODUCT_1 = SuccessMetric(
    name='overall_quality',
    description=('What was the overall quality of software product/service '
                 'delivered?'),
)
PRODUCT_2 = SuccessMetric(
    name='business_and_revenue_generated',
    description=('To what extent has the software product/service been able to '
                 'generate revenues for the organization?'),
)
PRODUCT_3 = SuccessMetric(
    name='functional_suitability',
    description=('What was the functional suitability of the software/service '
                 'delivered?'),
)
PRODUCT_4 = SuccessMetric(
    name='reliability',
    description=('What was the reliability of the software/service delivered?'),
)
PRODUCT_5 = SuccessMetric(
    name='performance_efficiency',
    description=('What was the performance/efficiency of the software/service '
                 'delivered?'),
)
PRODUCT_6 = SuccessMetric(
    name='operability',
    description=('What was the usability of the software/service delivered?'),
)
PRODUCT_7 = SuccessMetric(
    name='security',
    description=('What was the security-related quality of software/service '
                 'delivered?'),
)
PRODUCT_8 = SuccessMetric(
    name='compatibility',
    description=('What was the compatibility of the software/service '
                 'delivered?'),
)
PRODUCT_9 = SuccessMetric(
    name='maintainability',
    description=('What was the maintainability of the software/service '
                 'delivered?'),
)
PRODUCT_10 = SuccessMetric(
    name='transferability',
    description=('What was the transferability of the software/service '
                 'delivered?'),
)
STAKEHOLDER_1 = SuccessMetric(
    name='user_satisfaction',
    description=('What was the user satisfaction with the software/service '
                 'delivered?'),
)
STAKEHOLDER_2 = SuccessMetric(
    name='team_satisfaction',
    description=('What was the team satisfaction with the software/service '
                 'delivered?'),
)
STAKEHOLDER_3 = SuccessMetric(
    name='top_management_satisfaction',
    description=('What was the top-management satisfaction with the '
                 'software/service delivered?'),
)

# Overall success
OVERALL = SuccessMetric(
    name='overall_success',
    description=('Mean of all success metrics'),
)

ALL_SUCCESS_METRICS = [PROCESS_1, PROCESS_2, PROCESS_3, PROCESS_4]
ALL_SUCCESS_METRICS += [
    PRODUCT_1, PRODUCT_2, PRODUCT_3, PRODUCT_4, PRODUCT_5, PRODUCT_6, PRODUCT_7,
    PRODUCT_8, PRODUCT_9, PRODUCT_10
]
ALL_SUCCESS_METRICS += [STAKEHOLDER_1, STAKEHOLDER_2, STAKEHOLDER_3]
ALL_SUCCESS_METRICS += [OVERALL]
