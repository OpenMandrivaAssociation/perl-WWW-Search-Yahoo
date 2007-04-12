%define module	WWW-Search-Yahoo
%define name	perl-%{module}
%define version 2.405
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Summary:	Backend for searching www.yahoo.com
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(I18N::Charset)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This class is a Yahoo specialization of WWW::Search. It handles
making and interpreting Yahoo searches http://www.yahoo.com.

This class exports no public interface; all interaction should
be done through WWW::Search objects.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# china is not responding and the tests take forever to finish...
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/WWW
%{_mandir}/*/*

