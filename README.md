[[00300 Index Einführung Informatik]]
# Recipe Api and Web Interface
### Author1: Bruno Welsch / 2170527
### Video: URL oder "VC"
### Informationen zum Projekt:
Ziel des Projektes war es ausgehend von einer relativ großen CSV Datei mit 2.231.149 Rezepten, eine API zu erstellen die anhand von übergebenen Zutaten, passende bzw. möglichst gut passende Rezepte zu finden und zurück zugeben. Um dies zu realisieren, habe ich zuerst mit der Recherche begonnen, welche Programmier Sprachen und Frameworks sich am besten eignen für mein Projekt. Am Ende ist die Entscheidung auf Python mit Flask für die API gefallen, als dazugehörige Datenbank habe ich mich für PostgreSQL entschieden, weil hier die Einbindung in Python in Kombination mit Flask schon gut Dokumentiert war. Die Webanwendung Basiert auf HTML, JS und CSS, da ich hier mit zumindest schon grundlegende Erfahrungen hatte. 

---
### Informationen zu den einzelnen Dateien und Programmen
#### API
##### main.py
In diesem Python Programm wird mit Hilfe des Flask-Frameworks, eine API Anwendung aufgebaut, die über einen Link verschiedene zutaten als Eingabewerte bekommt. Das Programm baut eine Verbindung zu einer Local gehosteten PostgreSQL-Datenbank auf, und durchsucht sie mithilfe der übergebenen Parameter nach Rezepten die möglicht gut auf die Angegeben zutaten Passen. 
