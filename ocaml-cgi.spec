%define up_name cgi
%define name	ocaml-%{up_name}
%define version	0.8
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Objective Caml library for writing CGIs
Source: 	http://www.lri.fr/~filliatr/ftp/ocaml/cgi/%{up_name}-%{version}.tar.bz2
URL:		http://www.lri.fr/~filliatr/ftp/ocaml/cgi
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This library provides a function to parse the CGI arguments, parse_args,
the result being an association list

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/cgi
make install TARGETDIR=%{buildroot}/%{ocaml_sitelib}/cgi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING LGPL
%dir %{ocaml_sitelib}/cgi
%{ocaml_sitelib}/cgi/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/cgi/*
%exclude %{ocaml_sitelib}/cgi/*.cmi
