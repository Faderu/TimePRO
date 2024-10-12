from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='timepro',
  version='0.0.4',
  description='A package for managing time effectively, including Pomodoro Timer, Task Manager, Deadline Tracker, and more.',
  long_description=open('README.md', encoding='utf-8').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/Faderu/TimePRO',  
  author='KELOMPOK 7 ALGORITMA A',
  author_email='fadhilbosque@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='pomodoro timer task manager deadline tracker', 
  packages=find_packages(),
  install_requires=[''] 
)
