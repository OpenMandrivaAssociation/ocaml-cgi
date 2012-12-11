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


%changelog
* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-8mdv2010.0
+ Revision: 390029
- rebuild

  + Florent Monnier <blue_prawn@mandriva.org>
    - site-lib hierarchy doesn't exist anymore

* Tue Dec 09 2008 Pixel <pixel@mandriva.com> 0.8-7mdv2009.1
+ Revision: 312253
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.8-6mdv2009.0
+ Revision: 254189
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-4mdv2008.1
+ Revision: 178365
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-3mdv2008.0
+ Revision: 77597
- fix missing interdependency

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-2mdv2008.0
+ Revision: 77587
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage


* Tue Feb 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-1mdv2007.0
+ Revision: 122959

* Tue Feb 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-1mdv2007.1
- first mdv release

