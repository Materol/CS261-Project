"""Calculates the number of overdue asana tasks and the number of github issues for a specified project"""

from lxml import html
from datetime import datetime
import requests, asana

class CodeBaseMetrics():

    def __init__(self):
        # Log into the asana API
        self.client = asana.Client.access_token('1/1204064128867214:db689f86d743d811b8a3c0d32571aaa9')
        self.me = self.client.users.get_user('me')

    def github_issues(self, github_repo):
        page = requests.get('https://github.com/' + github_repo)
        content = html.fromstring(page.content)
        # Finds the span element with the specified id and selects the title
        issues = content.xpath('//span[@id="issues-repo-tab-count"]/@title')

        print('This repo has', issues[0], 'issues.')
        return issues[0]

    def asana_tasks(self, search_project):
        # Find the Workspaces for user 'me'
        workspace_id = self.me['workspaces'][0]['gid']
        # Find the projects in this workspace
        projects = self.client.projects.get_projects(workspace=workspace_id)

        overdue_tasks = 0
        today = datetime.today().strftime('%Y-%m-%d')

        for project in projects:
            if project['name'] == search_project:
                tasks = self.client.tasks.get_tasks(project=project['gid'], opt_fields=['due_on', 'name', 'completed'])
                # Count the number of overdue tasks
                for task in tasks:
                    if task['due_on'] is not None and task['completed'] == False and task['due_on'] < today:
                        overdue_tasks += 1
        
        print('This project has', overdue_tasks, 'overdue tasks.')
        return overdue_tasks

if __name__ == '__main__':
    stats = CodeBaseMetrics()

    # The GitHub repo must be public
    stats.github_issues('microsoft/WSL')
    stats.asana_tasks('WSL')






