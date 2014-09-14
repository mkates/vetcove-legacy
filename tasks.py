#!/usr/bin/python

### Automation scripts for deployment ###

from invoke import task,run

@task
def build():
	## Run the grunt compiler
	try:
		run("grunt _less")
	except Exception as e:
		print(e)
		return

	## Try to git 
	print(run("git add . --all"))
	print(run("git commit -am 'push message'"))
	print(run("git push staging master"))
