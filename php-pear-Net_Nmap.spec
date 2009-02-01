%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Nmap
%define		_status		stable
%define		_pearname	Net_Nmap
Summary:	%{_pearname} - A simple wrapper class for the Nmap utility
Summary(pl.UTF-8):	%{_pearname} - prosty wrapper dla programu nmap
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c61d66bf4bf5f0eaf9b746a00ceac04a
URL:		http://pear.php.net/package/Net_Nmap/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	nmap
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.0
Requires:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Nmap is a simple interface for Nmap, the free and open source
utility for network exploration or security auditing.

Net_Nmap can be used to auto discovery hosts and services in your
network or simply to parse Nmap XML output.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Net_Nmap to prosty interfejs do programu nmap, nardzędzia do analizy
ruchu i audytu bezpieczeństwa.

Net_Nmap może być użyty do wykrycia maszyn i usług w sieci lub do
analizy raportu XML z nmapa.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/Nmap
%{php_pear_dir}/Net/Nmap.php
%{php_pear_dir}/data/Net_Nmap

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Net_Nmap
