%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define modname cgi

Summary:	Objective Caml library for writing CGIs
Name:		ocaml-%{modname}
Version:	0.8
Release:	9
License:	GPLv2+
Group:		Development/Other
Url:		http://www.lri.fr/~filliatr/ftp/ocaml/cgi
Source0:	http://www.lri.fr/~filliatr/ftp/ocaml/cgi/%{modname}-%{version}.tar.bz2
BuildRequires:	ocaml

%description
This library provides a function to parse the CGI arguments, parse_args,
the result being an association list.

%files
%doc CHANGES COPYING LGPL
%dir %{_libdir}/ocaml/cgi
%{_libdir}/ocaml/cgi/*.cmi

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
This package contains the development files needed to build applications
using %{name}.

%files devel
%{_libdir}/ocaml/cgi/*
%exclude %{_libdir}/ocaml/cgi/*.cmi

#----------------------------------------------------------------------------

%prep
%setup -q -n %{modname}-%{version}

%build
%configure
%make

%install
install -d -m 755 %{buildroot}%{_libdir}/ocaml/cgi
make install TARGETDIR=%{buildroot}%{_libdir}/ocaml/cgi

chmod 0644 %{buildroot}%{_libdir}/ocaml/cgi/cgi.mli

