from setuptools import *

kwargs = {
	"author" : "Frankie Primerano",
	"author_email" : "max00355@gmail.com",
	"description" : "Hey is a terminal helper that allows you to execute commands using plain old English.",
	"entry_points" : {"console_scripts" : ["hey=hey.hey:main"]},
	"name" : "hey",
	"packages" : ["hey"],
	"version" : "0.1.0",
}

setup(**kwargs)
