# iTASC 
### M+hub webhook dashboard and data administration site for iTASC trial.

Needs to be run on public URL SSL certified server (i.e. AWS Lightsail) to expose a webhook for D40g JSON basic (set in M+hub)

Based on Django framework with mysql database, see requirements.txt for environment. See settings.py for production guides and links. .env is required for secrets.

- v0.8 ready for cloning from github
- Tested on Lightsail at https://itasc.ddns.net with SSL certificate (no-ip and letsencrypt) 


## TODO after cloning onto new Ligthsail django instance:
- follow this guide https://docs.bitnami.com/aws/infrastructure/django/get-started/get-started/
- create your own .env files with SECRET_KEY, DEBUG, DATABASE_URL AND ALLOWED_HOSTS 
- create SSL certificates

### FUNCTIONS
- Login is required access a. Admin panel and b. iTASC Dashboard
- Admin panel login allows administrators the rights to export of data CSV, creation of other users/groups, editing items
- User login and rights are controlled by Admin 
- Pairings are made to match devices (IMEI) to subjects (PatientID) - A pair is unique one-to-one
- A pairing is deleted (unpaired) in Admin panel, it does not delete the measurements allocated to a patient
- A apired device cannot be allocated to another patient, it must be unpaired first
- Devices (IMEI) are auto added by sending a measure after the webhook (https.../itasc/bp/) is set in M+hub
- PatientID is only added/edited via Admin
- Raw data can be viewed at the webhook URL (from Dashboard edit URL to show ...../itasc/bp/)  

### Admin and User Help
- Admin panel is the main toolbox area (standard Django admin)
- User Help in progress

## Development TODO & NICE To HAVEs in v1
- coloured sys/Dia ranges (like in Admin)
- graphics per device/pairing (see awsb.ddns.net/eliot/ )


## Source and concept from awsb.ddns.net
