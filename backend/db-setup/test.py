import psycopg2
# If we opt for a cloud based database approach, these logins can be used
# This program connects to an online database and loads in a schema
params = {
  'database': 'cs261-database',
  'user': 'cs261-group',
  'password': 'project=ep-patient-glitter-740977;nqFbPj5Ll7ps',
  'host': 'ep-patient-glitter-740977.eu-central-1.aws.neon.tech',
  'port': 5432
}

# Connect to your postgres DB
conn = psycopg2.connect(**params)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute(open("schema.sql","r").read())

conn.commit()

# This is how you log in to the database through Django

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'cs261-database',
#         'USER': 'cs261-group',
#         'PASSWORD': 'nqFbPj5Ll7ps',
#         'HOST': 'ep-patient-glitter-740977.eu-central-1.aws.neon.tech',
#         'PORT': '5432',
#     }
# }