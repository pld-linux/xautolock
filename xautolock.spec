Summary:	Utility to fire up programs in case of user inactivity under X
Summary(pl):	Narzêdzie do uruchamiania programów w przypadku nieaktywno¶ci u¿ytkownika pod X
Name:		xautolock
Version:	2.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.ibiblio.org/pub/Linux/X11/screensavers/%{name}-%{version}.tgz
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Utility to fire up programs in case of user inactivity under X.

%description -l pl
Narzêdzie do uruchamiania programów w przypadku nieaktywno¶ci
u¿ytkownika pod X.

%prep
%setup -q

%build
xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog Readme Todo
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
