# Recipe API and Web Interface

## **Dieses Projekt wurde im Rahmen der Veranstaltung Inf-Einf-B der Uni Bamberg im WS24/25 entwickelt**

### Informationen zum Projekt:  
Ziel des Projektes war es, ausgehend von einer relativ großen CSV-Datei mit ca 2 Millionen Rezepten, eine API zu erstellen, die anhand von übergebenen Zutaten passende bzw. möglichst gut passende Rezepte findet und zurückgibt. Um dies zu realisieren, habe ich zuerst mit der Recherche begonnen, welche Programmiersprachen und Frameworks sich am besten für mein Projekt eignen. Am Ende ist die Entscheidung auf Python mit Flask für die API gefallen. Als dazugehörige Datenbank habe ich mich für PostgreSQL entschieden, weil hier die Einbindung in Python in Kombination mit Flask gute Anleitungen finden konnte. Die Webanwendung basiert auf HTML, JS und CSS, da ich hier zumindest schon grundlegende Erfahrungen hatte. Anzumerken ist, dass ich das Projekt bereits Ende Dezember fast fertiggestellt hatte, durch neu gelernte Methodik aus den Vorlesungen würde ich einige Design-Entscheidungen noch einmal überdenken.  
Aktuell funktioniert die gesamte Anwendung nur lokal und muss, um sie online zu verwenden bzw. um sie öffentlich zugänglich zu machen, noch an vielen Stellen modifiziert werden. Diesen Schritt habe ich mich bisher noch nicht getraut, weil es mir an vielen Stellen noch an Fachwissen fehlt.  
Um die Anwendung lokal zu starten, kann das `run.sh`-Skript verwendet werden. Es startet die PostgreSQL-Datenbank, die Flask-Anwendung und einen lokalen HTTP-Server, auf dem die Website angezeigt wird. Wenn alles ohne Fehlermeldung startet, kann die Anwendung direkt verwendet werden.  
Generative Ki wurde an einigen stellen, zur lösung von Problemen hinzugezogen, genau wie online Tutorials und beiträge aus Foren.
### Informationen zu den einzelnen Dateien und Programmen  

#### API  

##### main.py  
In diesem Python-Programm wird mithilfe des Flask-Frameworks eine API-Anwendung aufgebaut, die über einen Link verschiedene Zutaten als Eingabewerte bekommt. Das Programm stellt eine Verbindung zu einer lokal gehosteten PostgreSQL-Datenbank her und durchsucht sie mithilfe der übergebenen Parameter nach Rezepten, die möglichst gut auf die angegebenen Zutaten passen.

##### recipes_data.csv  
Ist der Datensatz, auf dem die Datenbank hinter der API basiert. Da der VC die Größe der Datei nicht unterstützt, kann dieses hier gefunden werden: [Kaggle-Dataset](https://www.kaggle.com/datasets/wilmerarltstrmberg/recipe-dataset-over-2m/data)

##### requirements.txt  
Enthält eine Liste der genutzten Python-Bibliotheken. Die Datei ist im .txt-Format, weil sie so leicht mit pip genutzt werden kann, um entsprechende Bibliotheken auf dem eigenen System zu installieren.


#### Frontend  

##### index.html  
Diese Datei enthält den Quellcode der Hauptseite, also das entsprechende Grundgerüst mit Eingabefeld, Beschreibungen und zwei Knöpfen. Einer, um die Suche zu starten, und ein zweiter, um auf die FAQ-Seite zu verweisen. Die Seite wird nach erfolgreichem Aufruf der API auch mit den Ergebnissen gefüllt. Ein entsprechendes Gerüst besteht hier dem entsprechend auch.  

##### faq.html  
In dieser Datei sind einfach einige Blöcke mit Fragen und Antworten angelegt, um die Bedienung und Fragen zum Programm zu erklären.

##### index.js  
Das Script wird von `index.html` verwendet, um den Zugriff auf die API durchzuführen. Die einzige Funktion der Datei wird durch Klicken des Such-Buttons in `index.html` aufgerufen. Diese wandelt alle eingegebenen Buchstaben in Kleinbuchstaben um und entfernt alle Lesezeichen, sodass die Werte aus dem Eingabefeld in den Link eingesetzt werden können. Nach der Rückgabe der API wird die zurückgegebene `.json`-Datei in die einzelnen Rezepte zerlegt, die wiederum in verschiedene Textfelder und Überschriften zerlegt werden. Wenn keine Antwort erhalten wurde bzw. nicht im erwarteten Format, wird eine Fehlermeldung auf der Website angezeigt. Des Weiteren wird der Button bzw. das Absenden der Eingabe gesperrt, wenn die Anfrage noch läuft.  

##### style.css  
Bei der Erstellung dieser Datei habe ich an vielen Stellen auf KI zurückgegriffen, unter anderem, weil es mir persönlich an gestalterischer Kreativität mangelt, aber auch, weil mir CSS nicht besonders liegt. Viele der feineren Abstimmungen habe ich aber dennoch von Hand vorgenommen.  

##### run.sh  
Hierbei handelt es sich einfach um ein Bash-Skript, das die gesamte Anwendung startet, wie oben beschrieben.  

# Disclaimer: Parts of this project were generated with the assistance of AI.
