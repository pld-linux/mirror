Summary:	Perl program to mirror FTP sites
Summary(pl):	Program w perlu do mirrorowania serwerów FTP
Name:		mirror
Version:	2.9
Release:	2
Copyright:	distributable
BuildArch:	noarch
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://src.doc.ic.ac.uk/computing/archiving/mirror/%{name}-%{version}.tar.gz
Source1:	mirror.defaults
Source2:	mirror.mm
Source3:	mirror.packages
Patch:		%{name}-PLD.patch
BuildRoot:	/tmp/%{name}-%{version}-buildroot

%define 	_libdir 	/usr/share
%define		_localstatedir 	/var
%define		_sysconfdir 	/etc

%description
Perl program to mirror FTP sites

%description -l pl
Program w perlu do mirrorowania serwerów FTP

%prep
%setup -q -c
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/mirror,%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_sysconfdir}/mirror/{packages,mm} \
	$RPM_BUILD_ROOT/{home/ftp/mirrors,var/log/mirror}

make \
    "PLDIR=$RPM_BUILD_ROOT%{_datadir}/mirror" \
    "BINDIR=$RPM_BUILD_ROOT%{_bindir}" \
    "MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1" \
    install

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mirror

ln -sf ../../../etc/mirror/mirror.defaults $RPM_BUILD_ROOT%{_libdir}/mirror/mirror.defaults
ln -sf ../../bin/mirror $RPM_BUILD_ROOT%{_libdir}/mirror/mirror.pl
ln -sf mirror-master $RPM_BUILD_ROOT%{_bindir}/mm

echo ".so mirror-master.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mm.1

install %{SOURCE3} $RPM_BUILD_ROOT/etc/mirror/packages/ftp.pld.org.pl
install %{SOURCE2} $RPM_BUILD_ROOT/etc/mirror/mm/ftp.pld.org.pl


gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/*  *.txt *.html mmin \
	mirror.nightly *.class \
	support/cyber-patches support/lstest.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz support/*.gz
%ghost /home/ftp/mirrors

%dir %{_sysconfdir}/mirror

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mirror/*.defaults

%attr(750,root,root) %dir %{_sysconfdir}/mirror/mm
%attr(640,root,root) %{_sysconfdir}/mirror/mm/*

%attr(750,root,root) %dir %{_sysconfdir}/mirror/packages
%attr(640,root,root) %{_sysconfdir}/mirror/packages/*

%attr(750,root,root) %dir %{_localstatedir}/log/mirror
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*

%attr(-,root,root) %{_datadir}/mirror
