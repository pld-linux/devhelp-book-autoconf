Summary:	DevHelp book: autoconf
Summary(pl):	Ksi±¿ka do DevHelp'a o autoconf
Name:		devhelp-book-autoconf
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/autoconf.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about autoconf

%description -l pl
Ksi±¿ka do DevHelp o autoconf

%prep
%setup -q -c autoconf -n autoconf

%build
mv -f book autoconf
mv -f book.devhelp autoconf.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/autoconf
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install autoconf.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install autoconf/* $RPM_BUILD_ROOT%{_prefix}/books/autoconf

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
