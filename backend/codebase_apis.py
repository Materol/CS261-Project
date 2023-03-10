"""Calculates the normalised number of overdue asana tasks and the number of github issues (taged as bugs) for a specified project"""

from lxml import html
from datetime import datetime
import requests, asana, re


class CodeBaseMetrics():

    def __init__(self):
        # Log into the asana API
        self.client = asana.Client.access_token(
            '1/1204064128867214:db689f86d743d811b8a3c0d32571aaa9')
        self.me = self.client.users.get_user('me')

    def github_issues(self, github_repo):
        page = requests.get('https://github.com/' + github_repo +
                            '/issues?q=is%3Aopen+is%3Aissue+label%3Abug')
        content = html.fromstring(page.content)
        # Finds the text content of the link element
        issues = content.xpath('//a[@class="btn-link selected"]/text()')
        # The number of open issues tagged as bugs
        bugs = int(re.findall(r'\d+', str(issues))[0])

        print('This repo has', bugs, 'bugs.')
        return bugs

    def asana_tasks(self, search_project):
        # Find the Workspaces for user 'me'
        workspace_id = self.me['workspaces'][0]['gid']
        # Find the projects in this workspace
        projects = self.client.projects.get_projects(workspace=workspace_id)

        overdue_tasks = 0
        total_tasks = 0
        today = datetime.today().strftime('%Y-%m-%d')

        for project in projects:
            if project['name'] == search_project:
                tasks = self.client.tasks.get_tasks(
                    project=project['gid'],
                    opt_fields=['due_on', 'name', 'completed'])
                # Count the number of overdue tasks
                for task in tasks:
                    if task['due_on'] is not None and task['completed'] == False:
                        total_tasks += 1
                        if task['due_on'] < today:
                            overdue_tasks += 1

        print('This project has', overdue_tasks / total_tasks,
              'overdue tasks (normalised).')
        return overdue_tasks / total_tasks


if __name__ == '__main__':
    stats = CodeBaseMetrics()

    # The GitHub repo must be public
    stats.github_issues('microsoft/WSL')
    stats.asana_tasks('WSL')
