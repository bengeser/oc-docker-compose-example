# Containertraining 1 Abschlusstermin Aufgabenstellung

Zum Abschluss des ersten Teiles des OC Container Trainings, möchten wir eine Nextcloud Instanz mit Datenbank Server aufsetzen.

Folgende Einschränkungen sind wünschenswert:
* Nach außen hin soll nur nextcloud erreichbar sein.
* Ein Redis Cache kann genutzt werden um File-Locking zu verbessern
* Die Nutzer und Konfigurationsdaten von Nextcloud und Datenbank sollten beim zerstören der Container erhalten bleiben
   

Empfohlende Images:

* [nextcloud](https://hub.docker.com/_/nextcloud)
* [postgres](https://hub.docker.com/_/postgres)
* [redis](https://hub.docker.com/_/redis)