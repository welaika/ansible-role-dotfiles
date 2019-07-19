Ansible Role Dotfiles
=========

[![Build Status](https://travis-ci.org/welaika/ansible-role-dotfiles.svg?branch=master)](https://travis-ci.org/welaika/ansible-role-dotfiles)

Install dotfiles for the user from a given repository.

Requirements
------------

Your dotfiles repository *must* have a `install.sh` files in it. We use it to
creates symlinks for example.

The user you want to install dotfiles to *must* already exists.

Role Variables
--------------

These are the default variables:

```yaml
dotfiles_repo: https://github.com/welaika/server_dotfiles.git # repository with your your dotifles
dotfiles_dependencies: # optional dotfiles dependencies, if you define alias or functions for software that is not installed by default
  - git
  - bash-completion
  - ack-grep
```

Dependencies
------------

Nope :)

Example Playbook
----------------

User `john_doe` *must* already exist.

```yaml
    - hosts: servers
      roles:
        - role: ansible-role-dotfiles
          vars:
            dotfiles_user: "john_doe"
```

License
-------

MIT

Author Information
------------------

made with ❤️ and ☕️ by [weLaika](https://dev.welaika.com)
