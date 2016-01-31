#!/usr/bin/python
import os, sys, errno, yum
#working on ,  build Nginx landing page creator, with error handling
	#default to techquiz port 8888 if no args passed if arg passed created site for it.
class nginxcreator:
	def installapp(self):
		yb = yum.YumBase()
		if not (yb.rpmdb.searchNevra(name='nginx')):
			print ("installing app")
			os.system("yum -y update")
			os.system("yum -y install nginx")
	def main(self,site="testquiz"):
		checknginx = self.installapp()
		if (len(sys.argv) >2): # check of sysargs legth
			print ("two arguements passed , only expecting one ,set to autobuild techquiz by default")
			args = str(len(sys.argv)-1)
			print("number of args passed: " +args)
		if (len(sys.argv) == 2):
			print ('creating test page for '+sys.argv[1])
			site = sys.argv[1]
		else:
			site = "testquiz"
		response = self.nxservblock(site)
		return (response)
	def nxservblock(self,site):
		while True:
			try: # create dirs needed
				if not os.path.exists('/var/www/'):os.makedirs('/var/www/')
				if not os.path.exists('/var/www/' + str(site) + '/'):os.makedirs('/var/www/' + str(site) + '/')
				#nblockf = open('/etc/nginx/conf.d/default.conf', 'w')
				nblockf = open('/etc/nginx/conf.d/'+ str(site) + '.conf', 'w')
				landingpage = open('/var/www/' + str(site) + '/index.html', 'w')
			except IOError as eio: #catchIOerror
				print 'unable to open /var/www/' + str(site) + '/index.html'
			try:
				wsbcontents = self.sbcontents(site)
				wlpcontents = self.createlandingpage()
				nblockf.write(wsbcontents)
				response = landingpage.write(wlpcontents)
				nblockf.close
				landingpage.close
				os.system("service nginx restart")
				return response
			except Exception as inst:
				print 'unable to write to /var/www/' + str(site) + '/index.html'
				nblockf.close
				landingpage.close
	def sbcontents(self,site):
		createsitefile ='''	
server 
	{
	listen 8888;
	#server_name '(?:'+ str(site) +')(?:-api|-tools|-www)\.domain\.com';
	#how to automate this down further with arg specific host headers based on FQDNs
	#would need to fix quotes around site for string concatenation
location / {
		root   /var/www/'''+ str(site) +''';
		index index index.htm index.html;

}
}
'''
		return createsitefile
	def createlandingpage(self):
		createcontent= '''<html>
  <head>
	<title>NWEA tech_quiz sample index.html</title>
  </head>
  <body bgcolor=white>

	<table border="0" cellpadding="10">
	  <tr>
		<td>
		  <h1>Hello, this is the sample page</h1>
		</td>
	  </tr>
	</table>

  </body>
		</html>'''
		return createcontent
a= nginxcreator()
b=a.main()
