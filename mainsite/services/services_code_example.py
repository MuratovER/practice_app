import requests
from bs4 import BeautifulSoup

from mainsite.models import CodeExamples


def find_projects():
    github = requests.get('https://github.com/MuratovER?tab=repositories')
    html = github.text
    HOST = 'https://github.com'
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='col-12 d-flex width-full py-4 border-bottom color-border-muted public source')
    projects = []
    for item in items:
        title = item.find('a', itemprop='name codeRepository')
        description = item.find('p', itemprop='description')
        link = HOST + title.get('href')
        if title is not None and description is not None:
            projects.append({
                'title': title.get_text(strip=True),
                'description': description.get_text(strip=True),
                'link': link
            })
        else:
            projects.append({
                'title': title.get_text(strip=True),
                'description':  '',
                'link': link
            })
    return projects


def check_for_project_list():
    projects = find_projects()
    projects_check = CodeExamples.objects.all()
    lstforcheck = []
    for project in projects_check:
        lstforcheck.append(project)

    if len(lstforcheck) != len(projects):
        CodeExamples.objects.all().delete()
        for element in projects:
            newtitle = element['title']
            newdescription = element['description']
            newlink = element['link']
            CodeExamples.objects.create(title=newtitle, description=newdescription, link=newlink)
