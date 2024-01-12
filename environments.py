import os # os.environ['VAR_NAME']
import sys
import json

# Ensure all required environment variables are set
try:  
  os.environ['API_KEY']
except KeyError: 
  print('[error]: `API_KEY` environment variable required')
  sys.exit(1)
  
# If HOSTNAME doesn't exist, presume local development and return localhost
print(os.environ.get('HOSTNAME', 'localhost'))
  
if os.environ.get('DEBUG') == 'True':
    print('[info]: app is running in debug mode')
    

os.environ['TESTING'] = 'true'

os.environ['DB_URL'] = 'psql://{user}:{password}@{host}:{port}/{name}'.format(
  user=os.environ['DB_USER'],
  password=os.environ['DB_PASSWORD'],
  host=os.environ['DB_HOST'],
  port=os.environ['DB_PORT'],
  name=os.environ['DB_NAME']
)

# Set DEBUG and TESTING to 'True' if ENV is 'development'
if os.environ.get('ENV') == 'development':
  os.environ.setdefault('DEBUG', 'True') # Only set to True if DEBUG not set
  os.environ.setdefault('TESTING', 'True') # Only set to True if TESTING not set
  
def delete_env():
    auth_api(os.environ['API_KEY']) # Use API_KEY
    os.environ.pop('API_KEY') # Delete API_KEY as it's no longer needed

def print_env():
  print(json.dumps({**{}, **os.environ}, indent=2))