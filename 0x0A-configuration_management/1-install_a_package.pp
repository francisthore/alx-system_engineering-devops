# this manifest installs flask
package { 'werkzeug' :
  ensure   => '2.1.1',
  provider => 'pip3'
}
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
