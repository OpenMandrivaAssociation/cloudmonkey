%undefine _debugsource_packages

Name:		cloudmonkey
Version:	6.4.0
Release:	1
Source0:	https://github.com/apache/cloudstack-cloudmonkey/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	CLI (Command Line Interface) for Apache CloudStack
URL:		https://github.com/apache/cloudstack-cloudmonkey/
License:	Apache-2.0
Group:		Servers
BuildRequires:	make
BuildRequires:	golang

%description
cloudmonkey ☁️🐵 is a command line interface (CLI) for Apache CloudStack.

It can be used both as an interactive shell and as a command-line tool,
simplifying Apache CloudStack configuration and management.

%prep
%autosetup -p1 -n cloudstack-cloudmonkey-%{version}

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
install -c -m 755 bin/cmk %{buildroot}%{_bindir}/

%files
%{_bindir}/cmk
