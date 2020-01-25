%define		status		stable
%define		pearname	Net_Nmap
Summary:	%{pearname} - A simple wrapper class for the Nmap utility
Summary(pl.UTF-8):	%{pearname} - prosty wrapper dla programu nmap
Name:		php-pear-%{pearname}
Version:	1.0.5
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ee29cb2a0899d44dd427a2b6e8ba6ae6
URL:		http://pear.php.net/package/Net_Nmap/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	nmap
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.5.4
Requires:	php-pear-XML_Parser
Obsoletes:	php-pear-Net_Nmap-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Nmap is a simple interface for Nmap, the free and open source
utility for network exploration or security auditing.

Net_Nmap can be used to auto discovery hosts and services in your
network or simply to parse Nmap XML output.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Net_Nmap to prosty interfejs do programu nmap, nardzędzia do analizy
ruchu i audytu bezpieczeństwa.

Net_Nmap może być użyty do wykrycia maszyn i usług w sieci lub do
analizy raportu XML z nmapa.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Net_Nmap/examples .
mv docs/Net_Nmap/examples/* examples
mv .%{php_pear_dir}/data/Net_Nmap/docs/* docs
rmdir .%{php_pear_dir}/data/Net_Nmap/docs
mv .%{php_pear_dir}/data/Net_Nmap/* .
rmdir .%{php_pear_dir}/data/Net_Nmap
mv docs/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/Nmap
%{php_pear_dir}/Net/Nmap.php
%{_examplesdir}/%{name}-%{version}
