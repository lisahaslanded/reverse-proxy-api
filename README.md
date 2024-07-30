# Reverse Proxy & API

A basic reverse proxy and web application server.

## Description

This system consists of a NGINX reverse proxy that forwards requests through a Wireguard VPN tunnel to a web server hosting a Python Flask application.

The Python application provides an endpoint to roll two dice and return the result: 

    GET /dice → Returns result of rolling two dice

*Note: Vault encryption key has been included for testing and demonstration purpose only. ***Secrets, keys, passwords, etc should NEVER be pushed to code repositories***.

## Getting Started

The following instructions describe how to install the environment and run the application on a local system.

### Dependencies

* Ansible
* Vagrant
* VirtualBox

### Installing

* Clone this repository
  ```
  git clone https://github.com/lisahaslanded/reverse-proxy-api.git
  ```

* Deploy Vagrant boxes
  ```
  vagrant up
  ```

* Configure VPN, servers, application and firewall
  ```
  cd ansible
  ansible-playbook -i inventory.ini main_playbook.yml
  ```

### Executing program

* From browser
  ```
  http://192.168.56.5/dice
  ```

* From command line 
  ```
  curl 192.168.56.5/dice
  ```
  
## Authors

Lisa Mah - lisaemah@gmail.com

## Version History

* 0.1
    * Initial Release

## Acknowledgments and References

* [Vagrant Documentation](https://developer.hashicorp.com/vagrant/docs)
* [Ansible Documentation](https://docs.ansible.com/ansible/latest/)
* [Wireguard Documentation](https://www.wireguard.com/quickstart/#quick-start)
* Plus various resources from stackoverflow.com and the university of youtube.com. :)
