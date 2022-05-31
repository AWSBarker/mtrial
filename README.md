# iTASC
M+hub webhook dashboard and data administration site for iTASC trial.

Needs to be run on public URL server (AWS Lightsail) with HTTPS to produce webhook for D40g set in M+hub.

Based on Django framework with mysql, see requirements.txt for environment.

See settings.py for production guides and links.

## TODO before release:
- v0.8 ready for cloning.
- Tested on Lightsail at https://..... /itasc/

## NICE To HAVE
- coloured sys/Dia ranges (like in Admin)

### FUNCTIONS
- Admin login allows export of data CSV, create users/groups
- Login required to view data and make pairings
- Devices added by adding webhook (https.../itasc/bp/) in M+hub then taking first measure
- PatientID added via Admin
- Patients paired with devices (1 to 1) in Admin and via Login
- Data selected/exported to CSV from Admin, Measures OR to JSON by GET (https.../itasc/bp/)

