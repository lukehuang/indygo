import os, subprocess

PWD = os.path.join(os.path.dirname(__file__), "..")

def perform_syncdb(settings):
	subprocess.call(["python", "manage.py", "syncdb",
											"--noinput",
											"--settings=settings.%s" % settings])

def run_supervisord(conf, *options):
	valid_options = {"--nodaemon": "-n"}
	add_options   = []
	for option in options:
		if option in valid_options:
			add_options.append(valid_options[option])
	confdir = os.path.abspath(os.path.join(PWD, "etc", "supervisor"))
	def valid_conf(c):
		for f in os.listdir(confdir):
			try:
				name, ending = f.split(".")
			except:
				name = f
			if name == c or f == c:
				return f
		return False
	found_conf = valid_conf(conf)
	if found_conf:
		confpath = os.path.join(confdir, found_conf)
		print confpath
		if add_options:
			subprocess.call(["supervisord", " ".join(add_options), "-c", confpath])
		else:
			subprocess.call(["supervisord", "-c", confpath])
	
def valid_settings():
	all_valid = []
	for f in os.listdir(os.path.join(PWD, "settings")):
		try:
			name, ending = f.split(".")
		except:
			name = f
		if name != "__init__" and ending != "pyc" and not name.startswith(".") and name != "common":
			all_valid.append(name)
	return all_valid


