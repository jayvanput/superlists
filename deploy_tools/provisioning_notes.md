Provisioning a new site
=======================

## Required packages
- nginx
- Python 3
- Git
- pip
- virtualenv

on Ubuntu:
    sudo apt-get instal nginx git python3 python3-pip

## Nginx Virtual host config
- see nginx.template.conf
- replace SITENAME with url

## Upstart Job
- Not sure how to do this in Ubuntu since upstart doesn't exist.
- Look into systemd

## Folder structure
/home/username
    sites
        SITENAME
            database
            source (where the GIT pull happens)
            static
            virtualenv