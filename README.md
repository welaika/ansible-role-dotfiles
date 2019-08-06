Ansible Role Dotfiles
=====================

[![Build Status](https://travis-ci.org/welaika/ansible-role-dotfiles.svg?branch=master)](https://travis-ci.org/welaika/ansible-role-dotfiles)

Install dotfiles for a specific user.

Dotfiles are fetch from a git repository.

Requirements
------------

Your dotfiles repository *must* have a `install.sh` files in it. Use it to create symlinks. This role won't create symlinks for you.

The user **must** already exist.

Role Variables
--------------

These are the default variables:

```yaml
dotfiles_repo: https://github.com/welaika/server_dotfiles.git # repository with your your dotifles
dotfiles_dependencies: # packages needed by your dotfiles
  - git
  - bash-completion
  - ack-grep
```

Dependencies
------------

None :)

Example Playbook
----------------

User `john_doe` *must* already exist.

```yaml
- hosts: servers
  roles:
    - role: ansible-role-dotfiles
      vars:
        dotfiles_user: "john_doe"  # mandatory
```

License
-------

MIT

Testing
-------

Install molecule

`$ pip3 install --user 'molecule[docker]'`

Start docker and run

`$ molecule test`

Author Information
------------------

made with ❤️ and ☕️ by [weLaika](https://dev.welaika.com)
