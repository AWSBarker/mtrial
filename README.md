# itasc
M+hub webhook dashboard and data administration site for iTASC.

Needs to be run in production server with Gunicorn, Nginx and mysql/mariadb 

Requirements : python 3.9, django, (see requirements.txt)

## TODO before release:
- dockerise

## NICE To HAVE
- coloured sys/Dia ranges, set in admin

### FUNCTIONS
A. Admin login allows export of data CSV, create users/groups
B. Login required to view data
C. Devices added by adding webhook (http.../itasc/bp/) in M+hub then measure
D. Patient added via Admin
E. Patients paired with devices (1 to 1) in Admin and Login
F. Data selected/exported to CSV from Admin, Measures OR to JSON by GET (http.../itasc/bp/)
G.
