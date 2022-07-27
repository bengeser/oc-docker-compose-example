# Ausblick auf Kubernetes
Docker Compose ist ein praktisches Werkzeug, doch für den produktiven Einsatz scheinen ein paar Dinge noch nicht perfekt zu sein. Kubernetes kann alles, was docker compose kann, bringt aber dazu noch:

* Skalierung über mehr als einen Computer
* Integration mit Cloud Services
* Integration verschiedener Persistentzkonzepte
* Berechtigungen und Sicherheitskonzepte - Wer darf was im Entwicklerteam, wer darf was als Service?
* Services aus mehr als einem Container?
* Integration von Service Meshes
* Zero Downtime Upgrades/Deployments
* Rollback
* Verbessertes Tagging Konzept
* Helm repository als basis für fertige Anwendungen
* Health Checks
* Ingress servers (Traefik, Nginx, Kong -> Voll integriert)