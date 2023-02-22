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
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


# Characteristics of the process
budget = SuccessMetric(
    name='budget',
    description=('To what extent did the project finish on budget?'),
)
schedule = SuccessMetric(
    name='schedule',
    description=('To what extent did the project finish on schedule/time?'),
)
scope = SuccessMetric(
    name='scope',
    description=('To what extent did the project conform to the '
                 'initially-defined scope (features)?'),
)
team_building_and_dynamics = SuccessMetric(
    name='team_building_and_dynamics',
    description=('To what extent has the project been influential in positive '
                 'team building, team dynamics, and enhancing team members\' '
                 'opinions about each other?'),
)

# Characteristics of the resulting product/service
overall_quality = SuccessMetric(
    name='overall_quality',
    description=('What was the overall quality of software product/service '
                 'delivered?'),
)
business_and_revenue = SuccessMetric(
    name='business_and_revenue_generated',
    description=('To what extent has the software product/service been able to '
                 'generate revenues for the organization?'),
)
functional_suitability = SuccessMetric(
    name='functional_suitability',
    description=('What was the functional suitability of the software/service '
                 'delivered?'),
)
reliability = SuccessMetric(
    name='reliability',
    description=('What was the reliability of the software/service delivered?'),
)
performance_efficiency = SuccessMetric(
    name='performance_efficiency',
    description=('What was the performance/efficiency of the software/service '
                 'delivered?'),
)
operability = SuccessMetric(
    name='operability',
    description=('What was the usability of the software/service delivered?'),
)
security = SuccessMetric(
    name='security',
    description=('What was the security-related quality of software/service '
                 'delivered?'),
)
compatibility = SuccessMetric(
    name='compatibility',
    description=('What was the compatibility of the software/service '
                 'delivered?'),
)
maintainability = SuccessMetric(
    name='maintainability',
    description=('What was the maintainability of the software/service '
                 'delivered?'),
)
transferability = SuccessMetric(
    name='transferability',
    description=('What was the transferability of the software/service '
                 'delivered?'),
)
user_satisfaction = SuccessMetric(
    name='user_satisfaction',
    description=('What was the user satisfaction with the software/service '
                 'delivered?'),
)
team_satisfaction = SuccessMetric(
    name='team_satisfaction',
    description=('What was the team satisfaction with the software/service '
                 'delivered?'),
)
top_management_satisfaction = SuccessMetric(
    name='top_management_satisfaction',
    description=('What was the top-management satisfaction with the '
                 'software/service delivered?'),
)

# Overall success
overall_success = SuccessMetric(
    name='overall_success',
    description=('Mean of all success metrics'),
)
