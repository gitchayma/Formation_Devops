
# -----1: Lancer le code de l'application flask-------
# Dand Dockerfile: Définir une image......

# -----2: Faire le deploiment-------
## creer config-map.yml, 
## creer secret.yml, 
## creer deploy.yml: Ajouter  spec: imagePullPolicy: IfNotPresent dans: spec; contenair

# -----3: Ajouter la config-map et le secret --------
## Dans le fichier dpl on rajoute: 
"""env:
        - name: KEY1            :Aller chercher le KEY de l'app.py
          valueFrom:
            configMapKeyRef:    
              name: flask-data  :Aller chercher comment j'ai nommé configMap.yml
              key: key1         :Aller chercher key de configMap
        - name: PASSWORD        :Aller chercher le PASSWORD de l'app.py
          valueFrom:
            secretKeyRef:
              name: mysecret    :Aller chercher comment j'ai nommé secret.yml
              key: password     :Aller chercher key de secret.yml  """    
              
               
#-----4: Faire le deploiment-------

#-----5: Faire le deploiment------- 
 