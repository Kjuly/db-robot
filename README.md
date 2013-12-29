
Douban Robot
============

https://db-robot.appspot.com

Deploy:

    $ appcfg.py --oauth2 -A db-robot update .

Run locally:

    $ cd path/to/db-robot
    $ dev_appserver.py . --skip_sdk_update_check

Preview locally:

> http://localhost:8080


## Help

    $ ln -s <src-lib> <des-lib>


## Note

`douban_client` needs `pyoauth2` lib:

    $ mv pyoauth2 /framework/
    $ cd framework/douban_client
    $ ln -s ../pyoauth2

Some classes of `douban_client/api` fold need `pyoauth2` lib

    $ cd api
    $ ln -s ../../pyoauth2

`pyoauth2` needs `requests` lib:

    $ cd framework/douban_client/pyoauth2/libs
    $ ln -s /usr/local/lib/python2.7/site-packages/requests

