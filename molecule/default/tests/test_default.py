import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dotfiles_exist(host):
    f = host.file('/home/jerry/.dotfiles')
    assert f.exists


def test_symlink_created(host):
    f = host.file('/home/jerry/.bashrc')
    assert f.linked_to == '/home/jerry/.dotfiles/bashrc'
