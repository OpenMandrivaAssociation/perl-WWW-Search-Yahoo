%define module	WWW-Search-Yahoo

Name:		perl-%{module}
Version:	2.415
Release:	2
License:	GPL or Artistic
Summary:	Backend for searching www.yahoo.com
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{module}-%{version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(I18N::Charset)
BuildArch:	noarch

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
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/WWW
%{_mandir}/*/*



%changelog
* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.415-1mdv2010.0
+ Revision: 371361
- update to new version 2.415

* Mon Jan 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.414-1mdv2009.1
+ Revision: 328532
- update to new version 2.414

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.413-2mdv2009.0
+ Revision: 268881
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.413-1mdv2009.0
+ Revision: 194965
- update to new version 2.413

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.411-1mdv2008.1
+ Revision: 178275
- update to new version 2.411

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2.409-1mdv2008.0
+ Revision: 20710
- 2.409


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.405-2mdv2007.0
- Rebuild

* Wed May 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.405-1mdk
- new version
- fix source URL

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.404-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
	- BuildRequires

* Thu Nov 03 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.404-1mdk
- New release 2.404
- spec cleanup
- fix directory ownership

* Thu Aug 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.403-1mdk
- new version 
- fix sources url for rpmbuildupdate

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 2.399-1mdk
- initial Mandriva package

