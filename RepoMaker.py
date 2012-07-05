# Author: cytec <iamcytec@googlemail.com>
# URL: http://github.com/cytec/SynoDLNAtrakt/
#
# This file is part of RepoMaker.

import os
import urllib
import bz2

remote_repolist = [ "http://cytec.us" ]

 

def getPackages(repourl):
	urlstring = "{0}/Packages.bz2".format(repourl)
	packages = urllib.urlopen(urlstring).read()
	packages_dir = "remote_repos/" + repourl.replace("http://","")
	if not os.path.exists(packages_dir):
		os.makedirs(packages_dir)
	bz2packages_file = open(packages_dir + '/Packages.bz2', 'w')
	bz2packages_file.write(packages)
	bz2packages_file.close()
	packages_content = bz2.BZ2File(packages_dir + '/Packages.bz2', 'rb')
	packages_file = open(packages_dir + '/Packages', 'w')
	plain_packages = packages_content.read()
	packages_file.write(plain_packages)
	packages_file.close()

def getDepends(repo, filename):
	path = "remote_repos/{0}/Packages".format(repo)
	
	
for remote_repo in remote_repolist:
	getPackages(remote_repo)