# https = True
# httpscertfile = "/path/to/ssl/certificate.cert"
# httpskeyfile = "/path/to/ssl/server.key"

port = 8088

pemdir = "/var/airnotifier/files"

passwordsalt = "d2o0n1g2s0h3e1n1g"
cookiesecret = "airnotifiercookiesecret"
debug = False

mongohost = "localhost"
mongoport = 27017

masterdb = "airnotifier"
collectionprefix = "obj_"
dbprefix = ""
appprefix = "app_"

# If your MongoDB requires authentication, create a user with full permissions
# to the masterdb and enter credentials here. For details, see:
# https://docs.mongodb.com/manual/tutorial/enable-authentication/#procedure
#
# dbuser = "<your DB admin username>"
# dbpass = "<your password>"
# dbauthsource = "admin"
