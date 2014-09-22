#!/usr/bin/python

### Automation scripts for deployment ###

from invoke import task,run

@task
def build(message):
	pass
	## Run the grunt compiler
	try:
		run("grunt")
	except Exception as e:
		print(e)
		return

	# ## Try to git 
	print(run("git add . --all"))
	print(run("git commit -am 'push message'"))
	print(run("git push staging master"))
