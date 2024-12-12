# Recipe API and Web Interface

## Author1: Bruno Welsch / 2170527  
## Video: URL oder "VC"  

## Informationen zum Projekt:  
Ziel des Projektes war es, ausgehend von einer relativ großen CSV-Datei mit 2.231.149 Rezepten, eine API zu erstellen, die anhand von übergebenen Zutaten passende bzw. möglichst gut passende Rezepte findet und zurückgibt. Um dies zu realisieren, habe ich zuerst mit der Recherche begonnen, welche Programmiersprachen und Frameworks sich am besten für mein Projekt eignen. Am Ende ist die Entscheidung auf Python mit Flask für die API gefallen. Als dazugehörige Datenbank habe ich mich für PostgreSQL entschieden, weil hier die Einbindung in Python in Kombination mit Flask schon gut dokumentiert war. Die Webanwendung basiert auf HTML, JS und CSS, da ich hier zumindest schon grundlegende Erfahrungen hatte.

## Informationen zu den einzelnen Dateien und Programmen  

### API  

#### main.py  
In diesem Python-Programm wird mit Hilfe des Flask-Frameworks eine API-Anwendung aufgebaut, die über einen Link verschiedene Zutaten als Eingabewerte bekommt. Das Programm baut eine Verbindung zu einer lokal gehosteten PostgreSQL-Datenbank auf und durchsucht sie mithilfe der übergebenen Parameter nach Rezepten, die möglichst gut auf die angegebenen Zutaten passen.

#### recipes_data.csv.zip  
Ist die komprimierte Version des Datensatzes zur besseren Teilung des Projektes.

#### requirements.txt  
Enthält eine Liste der genutzten Python-Bibliotheken. Die Datei ist im .txt-Format, weil sie so leicht mit pip3 genutzt werden kann, um entsprechende Bibliotheken auf dem eigenen System zu installieren.

### Frontend  

#### index.html  
Diese Datei enthält den Quellcode der Hauptseite, also das entsprechende Grundgerüst mit Eingabefeld, Beschreibungen und zwei Knöpfen. Einer, um die Suche zu starten, und ein zweiter, um auf die FAQ-Seite zu verweisen. Des Weiteren enthält die Datei einen noch leeren `div`, welcher nach erfolgreicher Suche mit Inhalt gefüllt wird.

#### faq.html  
In dieser Datei sind einfach einige Blöcke mit Fragen und Antworten angelegt, um die Bedienung und Fragen zum Programm zu erklären.

#### index.js  
Das Script wird von `index.html` verwendet, um den Zugriff auf die API durchzuführen. Die einzige Funktion der Datei wird durch das Klicken des Such-Knopfes in `index.html` aufgerufen. Diese wandelt alle eingegebenen Buchstaben in Kleinbuchstaben um und entfernt alle Lesezeichen, sodass die Werte aus dem Eingabefeld in den Link eingesetzt werden können. Nach der Rückgabe der API wird die zurückgegebene `.json`-Datei in die einzelnen Rezepte zerlegt, die wiederum in verschiedene Textfelder und Überschriften zerlegt werden. Wenn keine Antwort erhalten wurde bzw. nicht im erwarteten Format, wird eine Fehlermeldung auf der Website ausgegeben.

#### style.css  
Bei der Erstellung dieser Datei habe ich viel Unterstützung von KI-Tools erhalten, einfach aus dem Grund, dass meine persönliche Stärke nicht wirklich im Design liegt und meine Vorkenntnisse in CSS auch eher begrenzt sind. Ziel hier war es, einfach ein übersichtliches Design zu erschaffen, um die Darstellung im Browser nutzerfreundlicher zu machen.

#### run.sh  
Hierbei handelt es sich einfach um ein Bash-Skript, das das Backend startet.

#### stop.sh  
Passend zu `run.sh` ist dies die Datei zum Beenden der Python-App und der Postgre-Datenbank.
