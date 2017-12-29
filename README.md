# Roboter Setup

#### EINRICHTEN DER VIRTUELLEN UMGEBUNG

Für die Applikation wird eine Virtuelle Umgebung - `venv` virtual enviroment - eingerichtet.

Ausgangspunkt für die Installation ist das `home` Verzeichnis des Users `pi`.


    mkdir -p projects/django-robot
    cd projects/django-robot/
    sudo pip3 install virtualenv

An dieser Stelle muss ermittelt werden, wo die Python3 Version liegt um anschließend die richtige `venv` aufzusetzen.
Der Befehlt `which python3` liefert den Pfad zu Python 3 `/usr/bin/python3` insofern Python 3 auf dem Raspberry Pi installiert wurde. Ansonst muss dies davor noch druchgeführt werden.

    virtualenv --python=/usr/bin/python3 venv3 && source venv3/bin/activate

Alle weiteren Befehle werden, wenn nicht anders angeführt im folgendend Verzeichnis unter `venv3` ausgeführt:
    
    (venv3) pi@raspberrypi:~/projects/django-robot $

  
###### Zur Überprüfung der Versionen
        BEFEHL                Output    
    pip3 --version      | pip 1.5.6 from /usr/lib/python3/dist-packages (python 3.4)
    python3 --version   | Python 3.4.2
    
    in der virtuellen Umgebung
    pip --version       | pip 9.0.1 from /home/pi/projects/django-robot/venv3/lib/python3.4/site-packages (python 3.4)
    python --version    | Python 3.4.2
    

#### Downlaod der Sourcen
    git clone https://github.com/michael-mammut/roboterWebControl.git
    
#### Installation der benötigten Packages

    pip install django
    pip install djangorestframework
    pip install django-filter
    pip install rpi.gpio
    
#### Konfiguration
m das System im Netz zu betreiben muss der Host  in der Datei `~/projects/django-robot/roboterWebControl/roboterWebControl/settings.py` eingetragen werden.
Das Feld `ALLOWED_HOSTS = ['localhost', '127.0.0.1']` ist um die IP Adresse des Hosts oder der Domain zu erweitern.
Sollte für das Frontend ein zweiter Webserver verwendet werden, so ist dieser ebenfalls hier einzutragen.


#### Starten des Server
Ausgang ist das Verzeichnis `~/projects/django-robot`.

    source venv3/bin/activate 
    cd roboterWebControl/roboterWebControl/  
    python manage.py runserver <your IP>:<Port - mostly 8080>
    
#### Userinterface

Während der Entwicklung steht das provisorische UI über die Addresse
`http://<ip>:8080/movements/` erreichbar.

Steuerung ist über die Maus und Arrow-Keys möglich.
Bei der Verwendung der Arrow-Keys muss jedoch der Fahrprozess über die Taste `S` gestoppt werden.
