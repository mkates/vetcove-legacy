#!/usr/bin/python

### Automation scripts for deployment

from invoke import task,run

@task
def build():
	## Run the grunt compiler
	try:
		run("grunt _less")
	except Exception as e:
		print(e)

	## Try to git 
	run("git add . --all")
	run("git commit -am 'push message'")
	run("git push staging master")
	print ("Complete")
