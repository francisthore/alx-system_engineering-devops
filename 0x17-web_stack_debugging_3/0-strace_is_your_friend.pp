# Create /var/www/html/.maintenance file
file { '/var/www/html/.maintenance':
  ensure => present,
  mode   => '0644',
}

# Ensure wp-content/languages directory exists
file { '/var/www/html/wp-content/languages':
  ensure => directory,
  mode   => '0755',
}

# Ensure wp-includes/languages directory exists
file { '/var/www/html/wp-includes/languages':
  ensure => directory,
  mode   => '0755',
}

# Create /var/www/html/wp-content/db.php file
file { '/var/www/html/wp-content/db.php':
  ensure => present,
  mode   => '0644',
}

# Create /var/www/html/wp-content/object-cache.php file
file { '/var/www/html/wp-content/object-cache.php':
  ensure => present,
  mode   => '0644',
}

# Fix the typo in wp-settings.php
augeas { 'fix_wp_locale_typo':
  context => '/files/var/www/html/wp-settings.php',
  changes => [
    "set *[contains(text(), 'class-wp-locale.phpp')]/text 'require_once(ABSPATH . WPINC . \"/class-wp-locale.php\");'"
  ],
  onlyif  => "match *[contains(text(), 'class-wp-locale.phpp')] size > 0",
}

# Ensure the Apache service is running and restart it if necessary
service { 'apache2':
  ensure    => 'running',
  enable    => true,
  subscribe => Augeas['fix_wp_locale_typo'],
}
