FROM alpine

RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN echo "Japan" > /etc/timezone
CMD date    
# c'est la commande finale qu'il sera lancé 

# On veux lancer la commande "docker run tp_jap_tz" il faut creer une image tp_jap_tz 
# qui donne l'heure au japon " docker build -t tp_jap_tz ."
# Donc maintenat on peut lancé " docker run tp_jap_tz" résultat : Mon Aug 28 21:53:26 JST 2023
