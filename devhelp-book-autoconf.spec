Summary:	DevHelp book: autoconf
Summary(pl):	Ksi±¿ka do DevHelpa o autoconfie
Name:		devhelp-book-autoconf
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/autoconf.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about autoconf.

%description -l pl
Ksi±¿ka do DevHelpa o autoconfie.

%prep
%setup -q -c -n autoconf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/books/autoconf

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/books/autoconf/autoconf.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/autoconf

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
