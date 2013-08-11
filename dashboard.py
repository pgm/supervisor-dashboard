from bottle import route, run, template, view, static_file

import xmlrpclib
import socket
from ConfigParser import ConfigParser
import os.path
import sys

def readConfig(filename):
  hostname = os.path.basename(filename).split(".")[0]

  cp = ConfigParser()
  cp.readfp(open(filename))

  if cp.has_section("include"):
    includeFile = cp.get("include", "files")
    config = readConfig(includeFile)
  else:
    config = {}
  
  t = {}
  if hostname != 'common':
    t['hostname'] = hostname

  if cp.has_section("inet_http_server"):    
    port = cp.get("inet_http_server", "port")
    if port != None:
      t['port'] = port.split(":")[1]
    t['username'] = cp.get("inet_http_server", "username")
    t['password'] = cp.get("inet_http_server", "password")

  for k,v in t.items():
    if v != None:
      config[k] = v
  
  return config

from glob import glob
import itertools

confFiles = sys.argv[1:]
confFiles = list(itertools.chain(*[ glob(c) for c in confFiles]))
confFiles.sort()

@route('/')
@view("index")
def index():
  summary = []

  for fn in confFiles:
    if fn.endswith("common.conf"):
      continue

    config = readConfig(fn)

    user = config['username']
    password = config['password']
    try:
      server = xmlrpclib.Server('http://%s:%s@%s:%s/RPC2' % (user,password,config['hostname'],config['port']))
      serverStatus = server.supervisor.getState()
      statuses = server.supervisor.getAllProcessInfo()
    except socket.error:
      serverStatus = {'statename': 'Unreachable'}
      statuses = []
    
    summary.append( {'hostname': config['hostname'], 'port': config['port'], 'serverStatus': serverStatus['statename'], 'statuses': statuses})
    
  return {'summaries':summary}

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root="./static")

run(host="0.0.0.0",port=9002, debug=True)
