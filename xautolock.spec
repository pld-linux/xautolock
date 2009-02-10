Summary:	Utility to fire up programs in case of user inactivity under X
Summary(pl.UTF-8):	Narzędzie do uruchamiania programów w przypadku nieaktywności użytkownika pod X
Name:		xautolock
Version:	2.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.ibiblio.org/pub/Linux/X11/screensavers/%{name}-%{version}.tgz
# Source0-md5:	9526347a202694ad235d731d9d3de91f
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to fire up programs in case of user inactivity under X.

%description -l pl.UTF-8
Narzędzie do uruchamiania programów w przypadku nieaktywności
użytkownika pod X.

%prep
%setup -q

%build
xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT/usr/man/man1/xautolock.1x $RPM_BUILD_ROOT%{_mandir}/man1/xautolock.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog Readme Todo
%attr(755,root,root) %{_bindir}/xautolock
%{_mandir}/man1/xautolock.1*
