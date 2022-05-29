# itasc
M+hub webhook dashboard and data administration site for iTASC.

Needs to be run in production server with Gunicorn, Nginx, mysql/mariadb to produce webhook (public URL) 

Requirements : python 3.9, django, (see requirements.txt)

## TODO before release:
- dockerise

## NICE To HAVE
- coloured sys/Dia ranges, set in admin

### FUNCTIONS
- Admin login allows export of data CSV, create users/groups
- Login required to view data
- Devices added by adding webhook (http.../itasc/bp/) in M+hub then measure
- Patient added via Admin
- Patients paired with devices (1 to 1) in Admin and Login
- Data selected/exported to CSV from Admin, Measures OR to JSON by GET (http.../itasc/bp/)
-
