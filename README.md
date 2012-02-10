Django Twitter Bootstrap
=========================
The goal of Django Twitter Bootstrap is quite simple - provide a base Django project which handles the build process of Twitter Bootstrap 2.0 via django-compress.  Basically, using this template, it will be easy to see how you can include more LESS files (and even coffeescript) and have Django build (and with DEBUG = False, concat and compress) these files for production use.

Requirements
------------
You must have lessc and node globally accessible. On OSX, I used Macports to install node, added a symbolic link to /usr/bin/node and then used Node Package Manager (npm) to install lessc via the following:
    
    npm install --global less

If you can run the test pages (no syncdb required), then you're golden.

Updates
-------
I will keep an eye on Twitter Bootstrap and update my code as necessary. If I'm behind, let me know!

I Need Help With...
--------------------
I would love for someone to help me standardize this project a little further. Ideally without too many more requirements, better logging and media support would be great settings for a starter project like this!

Enjoy!