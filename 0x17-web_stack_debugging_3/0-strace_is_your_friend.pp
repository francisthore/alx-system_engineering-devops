# Fix the typo in wp-settings.php using exec and sed
exec { 'fix_wp_locale_typo':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    => '/bin:/usr/bin',
  onlyif  => "grep -q 'class-wp-locale.phpp' /var/www/html/wp-settings.php",
}
