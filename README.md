# RAICoreServices - Public Version (v1.0)

This is the template of Django project of Robotics Laboratory 3 (Smart Lab)

You need to follow this project format before upload your code to the real server

## Outline
- [Installation](#installation)
- [File System](#file-system)
  - [Application](#application)
  - [Template](#template)
  - [Static file](#static-file)
  - [Media file](#media-file)
- [Authentication System](#authentication-system)
  - [User](#user)
  - [Work with views](#work-with-views)


## Installation

1. Install Python3, Django
2. Download this git
3. Run server `python3 manage.py runserver `

Now you can run this project

## File system

<img src="https://github.com/earthsaharat/RAICoreServices_PublicVersion/blob/master/git_supportfile/file_structure_full.png" width="200"/>

### Application
You application/module are stored in 

```
RAICoreServices_PublicVersion/rai_modules/<your_module_name>
```
This folder will contain all of your python file. Such as views.py, urls.py, models.py

> **Module name should be leading by `rai_`. For Example, `rai_exampleapp`**

### Template

Html file

```
RAICoreServices_PublicVersion/rai_modules/<your_module_name>/template/<your_html_file>.html
```

### Static file

Such as css, javascript, image

```
RAICoreServices_PublicVersion/static/<your_module_name>/<your_static>
```

### Media file

When you have database that contain images. Images will save to the folder media. The image field of model in models.py should set argument like this `image = models.ImageField(upload_to='<your_module_name>/image')`

The image that user uploaded, it saved in

```
RAICoreServices_PublicVersion/media/<your_module_name>/image/<image_file>
```

## Authentication System

This project has authentication system with user account and user access permission

### User

Default user is
```
username : admin
password : 1234567890
```

You can add user or edit user in module name **Users** in home page

### Work with views

In your `views.py`, you need to import these code first for enable authentication system in your module
``` python
from rai_modules.rai_user.models import RAIUser
from rai_modules.rai_module_manager.decorator import raimodule_user_verify
```

For the example view

``` python
@raimodule_user_verify(module_id=3)
def home(request):
    raiuser = RAIUser.objects.getFromUser(request.user)
    return render(request,'rai_exampleapp/home.html')
```

The variable `raiuser` is contain user data that logging in to the website while request that page or that view

The code `@raimodule_user_verify(module_id=3)`, you should put before every view function. This code use to verify the user that request the page/view whether the user match with the property that you set or not. You must change module_id to your module ID in the real server.

You can change the property and accessibility in module name **Module Manager**
# raicore_voniq
