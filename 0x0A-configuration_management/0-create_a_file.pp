# This puppet manifest creates a new file
file  {'create-file':
  ensure  =>  'present',
  path    =>  '/tmp/school',
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
  content =>  'I love Puppet',
}
