# iTASC
M+hub webhook dashboard and data administration site for iTASC trial.

Needs to be run on public URL server (AWS Lightsail) with HTTPS to produce webhook for D40g set in M+hub.

Based on Django framework with mysql, see requirements.txt for environment.

See settings.py for production guides and links. .env required for secrets.

- v0.8 ready for cloning from github
- Tested on Lightsail at https://3.72.60.211/itasc/


## TODO after cloning onto new Ligthsail django instance:
- follow this guide https://docs.bitnami.com/aws/infrastructure/django/get-started/get-started/
- create your own .env files with SECRET_KEY, DEBUG, DATABASE_URL AND ALLOWED_HOSTS 

## NICE To HAVE
- coloured sys/Dia ranges (like in Admin)
- graphics per device/pairing (see awsb.ddns.net/eliot/ 

### FUNCTIONS
- Admin login allows export of data CSV, create users/groups
- Login is required to view data and make pairings, Admin creates Users in Admin console
- Devices can be auto added by adding the webhook (https.../itasc/bp/) in M+hub then taking first measure
- PatientID added via Admin
- Patients paired with devices (1 to 1) in Admin and Pair (if logged-in)
- Data selected/exported to CSV from Admin, Measures OR to JSON by GET (https.../itasc/bp/)

