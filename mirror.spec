%include	/usr/lib/rpm/macros.perl
Summary:	Perl program to mirror FTP sites
Summary(es):	Programa Perl para hacer espejos de sitios FTP
Summary(pl):	Program w perlu do mirrorowania serwerów FTP
Summary(pt_BR):	Programa em perl para fazer espelhos de sítios FTP
Name:		mirror
Version:	2.9
Release:	6
License:	distributable
Group:		Networking/Utilities
Source0:	ftp://src.doc.ic.ac.uk/computing/archiving/mirror/%{name}-%{version}.tar.gz
# Source0-md5: 55178a53c7b4253c9a396a38c5a9cb94
Source1:	%{name}.defaults
Source2:	%{name}.mm
Source3:	%{name}.packages
Patch0:		%{name}-PLD.patch
Patch1:		http://sunsite.org.uk/packages/mirror/ftp.pl_wupatch
Patch2:		%{name}-name_mappings.patch
Requires:	perl-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_libdir 	/usr/share
%define		_localstatedir 	/var

%description
Perl program to mirror FTP sites.

%description -l es
Programa Perl para hacer espejos de sitios FTP

%description -l pl
Program w perlu do mirrorowania serwerów FTP.

%description -l pt_BR
Programa em perl para fazer espelhos de sítios FTP

%prep
%setup -q -c
%patch0 -p1
%patch1 -p0
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mirror,%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_sysconfdir}/mirror/{packages,mm} \
	$RPM_BUILD_ROOT/{home/services/ftp/mirrors,var/log/mirror}

%{__make} install \
	"PLDIR=$RPM_BUILD_ROOT%{_datadir}/mirror" \
	"BINDIR=$RPM_BUILD_ROOT%{_bindir}" \
	"MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1"

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mirror

ln -sf ../../..%{_sysconfdir}/mirror/mirror.defaults $RPM_BUILD_ROOT%{_libdir}/mirror/mirror.defaults
ln -sf ../../bin/mirror $RPM_BUILD_ROOT%{_libdir}/mirror/mirror.pl
ln -sf mirror-master $RPM_BUILD_ROOT%{_bindir}/mm

echo ".so mirror-master.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mm.1

install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/mirror/packages/ftp.pld.org.pl
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/mirror/mm/ftp.pld.org.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt mmin mirror.nightly *.class support/cyber-patches
%doc support/lstest.pl
%ghost /home/services/ftp/mirrors

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
