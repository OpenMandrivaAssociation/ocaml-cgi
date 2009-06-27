%define up_name cgi
%define name	ocaml-%{up_name}
%define version	0.8
%define release	%mkrel 8

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
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/cgi
make install TARGETDIR=%{buildroot}/%{_libdir}/ocaml/cgi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING LGPL
%dir %{_libdir}/ocaml/cgi
%{_libdir}/ocaml/cgi/*.cmi

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/cgi/*
%exclude %{_libdir}/ocaml/cgi/*.cmi
