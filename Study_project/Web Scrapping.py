import requests

indeed_resul = requests.get('https://www.indeed.com/jobs?q=python&limit=50&vjk=f6294b6c85e1cb47')

print(indeed_resul)