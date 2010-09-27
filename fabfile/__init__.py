from fabric.api import *

env.hosts = ["root@65.49.73.73"]

def host_type():
	print local("uname -s")

def setup_git():
	""" create an empty git repo on the server and push the local git repo to that """
	giturl = "%(user)s@%(host)s:~/repos/sample.git" % env
	run("mkdir -p repos/sample.git")
	with cd("repos/sample.git"):
		run("git init --bare")
	local("git remote add production %(giturl)s" % locals())
	local("git push production master")
	
def remove_git():
	""" remove the remote repo and the local reference to that repo """
	local("git remote rm production")
	run("rm -rf repos/sample.git")

def setup_site():
	run("mkdir -p sites")
	with cd("sites"):
		run("git clone ~/repos/sample.git")

def remove_site():
	run("rm -rf sites/sample")

def bootstrap():
	"""docstring for bootstrap"""
	pass

def push():
	local("git push production")
