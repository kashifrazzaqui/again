from setuptools import setup
setup(name='PyUtils',
	version='1.0',
	description='Python decorators for type and value checking at runtime. Also, some boilerplate code for making classes that support event registration and firing.',
	py_modules = ['decorate', 'events', 'statemachine', 'testrunner'],
	)

