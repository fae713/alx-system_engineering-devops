# Install werkzeug using pip3

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
}

# This is a puppet script that installs flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['Werkzeug'], # werkzeug is installed first
}
