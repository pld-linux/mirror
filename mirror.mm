
# Example parameter file for the Debian GNU/Linux "mirror" package
#
# This serves as an illustration for a valid mirror parameter file. See the
# man pages mirror(1) and mirror-master(1) as well as the files in 
# /usr/share/doc/example/mirror/* for details.
#
# This is for illustration. It worked for me when I wrote it, but it might 
# fail for you. No warranties whatsoever. Use at your own risk.
#
# Written by Dirk Eddelbuettel <edd@debian.org>

# NB: Make sure you can write to $home/mm.status. If you run mirror-master as
# a user, touch that file as root and set modes so that user can write to it.
home=/var/log/mirror

# add a  -n  for testing as usual
mirror=/usr/bin/mirror -p$package /etc/mirror/packages/$site >$site:$package

# mirror these if last (successful) mirroring was at least 20h ago
ftp.pld.org.pl:i386 20 0
ftp.pld.org.pl:i586 20 0
ftp.pld.org.pl:i686 20 0
ftp.pld.org.pl:SRPMS 20 0

# When mirror-master stops, the file /var/log/mirror/ftp.ps.pl:PLD
# lists the mirror results for the above example. 
