import os

 

files = ['config-map.yml','secret.yml','dpl.yml','service.yml','ingress-serv.yml']

 

os.system("kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml")

 

for file in files:

    os.system(f'kubectl apply -f {file}')

 