# Puppet manifest to fix nging ULIMIT
exec { 'replace_15_with_4096':
	command => 'sed -i "s/15/4096/g" /etc/default/nginx',
	onlyif  => 'grep -q "15" /etc/default/nginx',
	notify  => Exec['restart_nginx'],
}

# Restart nginx
exec {'restart_nginx':
	command     => 'service nginx restart',
	refreshonly => true,
}
