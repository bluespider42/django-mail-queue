[![Build Status](https://travis-ci.org/Privex/django-mail-queue.png?branch=master)](https://travis-ci.org/Privex/django-mail-queue)
[![PyPi Version](https://img.shields.io/pypi/v/privex-mail-queue.svg)](https://pypi.org/project/privex-mail-queue/)
![License Button](https://img.shields.io/pypi/l/privex-mail-queue)

Django Mail Queue
=================

This is a fork of http://github.com/dstegelman/django-mail-queue maintained by [Privex Inc.](https://www.privex.io/)

Privex publishes the fork under the PyPi package `privex-mail-queue` (since v3.2.0) to avoid conflicts
with the original version.

This fork is considered to be actively maintained by Privex for both bug fixes and feature additions since
December 2018. 

If our fork has helped you, consider 
[grabbing a VPS or Dedicated Server from Privex](https://www.privex.io/) - prices start at as little 
as US$0.99/mo (yes that's 99 cents a month, and we take cryptocurrency!)

Mail Queue provides an easy and simple way to send email.  Each email is saved and queued up either in
real time or with Celery.  As always, feedback, bugs, and suggestions are welcome.



Install
========

### Download and install from PyPi using pip (recommended)

```sh
pip3 install privex-mail-queue
```

### (Alternative) Manual install from Git

**Option 1 - Use pip to install straight from Github**

```sh
pip3 install git+https://github.com/Privex/django-mail-queue
```

**Option 2 - Clone and install manually**

```bash
# Clone the repository from Github
git clone https://github.com/Privex/django-mail-queue
cd django-mail-queue

# RECOMMENDED MANUAL INSTALL METHOD
# Use pip to install the source code
pip3 install .

# ALTERNATIVE MANUAL INSTALL METHOD
# If you don't have pip, or have issues with installing using it, then you can use setuptools instead.
python3 setup.py install
```

Quickstart
============

First install the package into your project (see above).

Open settings.py and add mailqueue to your INSTALLED_APPS:

```python
INSTALLED_APPS = (
    'mailqueue',
)
```

Add the below settings, and adjust as needed:

```python

# If you're using Celery, set this to True
MAILQUEUE_CELERY = False

# Enable the mail queue. If this is set to False, the mail queue will be disabled and emails will be 
# sent immediately instead.
MAILQUEUE_QUEUE_UP = True

# Maximum amount of emails to send during each queue run
MAILQUEUE_LIMIT = 50

# If MAILQUEUE_STORAGE is set to True, will ignore your default storage settings
# and use Django's filesystem storage instead (stores them in MAILQUEUE_ATTACHMENT_DIR) 
MAILQUEUE_STORAGE = False
MAILQUEUE_ATTACHMENT_DIR = 'mailqueue-attachments'

```

Once you've added mailqueue to your `INSTALLED_APPS` plus the basic config in settings.py, run the 
migrations to create the tables needed:


```bash
python manage.py migrate
```


To send emails in the queue (without Celery), use the management command:

```bash
# Send up to MAILQUEUE_LIMIT emails now
python manage.py send_queued_messages

# You can use --limit / -l to override the settings.py limit for a specific run
python manage.py send_queued_messages --limit 10
python manage.py send_queued_messages -l 10
```

If not using Celery, simply add a cron to your system to run `manage.py send_queued_messages` every minute (or however
often you want).



Documentation
-------------

http://readthedocs.org/docs/django-mail-queue/en/latest/

Mail Queue provides an admin interface to view all attempted emails and actions for resending failed messages.

![Screenshot of Email List](https://cdn.privex.io/github/privex-mail-queue/pmq-message-list.png)

![Screenshot of Email Actions](https://cdn.privex.io/github/privex-mail-queue/pmq-message-actions.png)


Support/Help/Spam/Hate Mail
---------------------------

If you have questions/problems/suggestions the quickest way to reach me to is simply add a GitHub issue to this project.

Running the Tests Locally
-------------------------

```
pip install django
pip install -r requirements.txt

py.test mailqueue
```
