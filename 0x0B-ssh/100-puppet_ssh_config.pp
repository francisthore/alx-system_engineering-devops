# sets the config file for ssh
file {'ssh-config':
  ensure  => 'present',
  path    => '/~/.ssh/config',
  content => 'IdentityFile ~/.ssh/school\nPasswordAuthentication no',
}
