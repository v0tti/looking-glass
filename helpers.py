import routers
import ipaddress

# this function returns the router object and the command string to run
# other router OS may be added to this dictionary in the same fashion, like IOS, SR-OS, etc.
def get_vars(router_name, cmd, ipprefix):
  if not is_ipv6net(ipprefix):
    return None, None, "{} is not a valid IPv6 address / prefix".format(ipprefix)
  if cmd!="bgp" and not is_ipv6(ipprefix):
    return None, None, "{} is not a valid IPv6 address".format(ipprefix)
  for r in routers.routers_list:
    if router_name == r['address'][0]:
      router = r
  switcher = {
    'bgp': {
      'bird': 'birdc show route table master6 all for {}'.format(ipprefix)
    },
    'traceroute': {
      'bird': 'traceroute6 -w 1 {}'.format(ipprefix)
    },
    'ping': {
      'bird': 'ping -6 -c 5 {}'.format(ipprefix)
    }
  }
  command = switcher.get(cmd).get(router['type'])
  return router, command, None

def is_ipv6net(ip_string):
  try:
    ipaddress.IPv6Network(ip_string)
    return True
  except ipaddress.AddressValueError:
    return False
  except ipaddress.NetmaskValueError:
    return False

def is_ipv6(ip_string):
  try:
    ipaddress.IPv6Address(ip_string)
    return True
  except ipaddress.AddressValueError:
    return False