from dotenv import load_dotenv
import os

load_dotenv()

## Example routers, please edit and add yours
routers_list = [
  dict(address=('dn42.v0tti.com', 22),
    usern=os.getenv('USERN'),
    passw=os.getenv('PASSW'),
    type='bird',
    asn='4242423929',
    location='dn42.v0tti.com',
    jumpserver=False
  )
]