#!/bin/bash

sudo apt-get update

# Vagrant desde la web oficial
wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
sudo dpkg -i vagrant_1.8.1_x86_64.deb
vagrant plugin install vagrant-azure
    
# Ansible desde pip
sudo apt-get install -y python-pip python-dev build-essential
sudo pip install paramiko PyYAML jinja2 httplib2 ansible

# Despliegue en Azure
export ANSIBLE_HOSTS=./ansible_hosts
vagrant up --provider=azure

# Despliegue de la app
