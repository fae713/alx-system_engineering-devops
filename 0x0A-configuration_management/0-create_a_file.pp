/*
This manifest creates a file with the path /tmp/school/
and stores the content 'I love Puppet'
*/

file { '/tmp/school':
ensure  => 'file',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
