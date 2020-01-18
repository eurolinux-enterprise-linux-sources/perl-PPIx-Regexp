Name:           perl-PPIx-Regexp
Version:        0.034
Release:        3%{?dist}
Summary:        Represent a regular expression of some sort
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PPIx-Regexp/
Source0:        http://search.cpan.org/CPAN/authors/id/W/WY/WYANT/PPIx-Regexp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(PPI::Document) >= 1.117
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Task::Weaken)
# Optional run-time:
BuildRequires:  perl(Encode)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
# Optional testsL
BuildRequires:  perl(charnames)
# Text::CSV is not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# Encode is optional.
Requires:       perl(Exporter)
Requires:       perl(PPI::Document) >= 1.117
Requires:       perl(Task::Weaken)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(PPI::Document\\)$

%description
The purpose of the PPIx-Regexp package is to parse regular expressions in a
manner similar to the way the PPI package parses Perl. This class forms the
root of the parse tree, playing a role similar to PPI::Document.

%prep
%setup -q -n PPIx-Regexp-%{version}
chmod -x eg/*
sed -i '1 s|/usr/local/bin/perl|%{__perl}|' eg/*

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes eg LICENSES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.034-3
- Mass rebuild 2013-12-27

* Fri May 24 2013 Petr Pisar <ppisar@redhat.com> - 0.034-2
- Specify all dependencies

* Mon May 13 2013 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.034 bump

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 0.033-1
- 0.033 bump

* Fri Feb 08 2013 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Mon Feb 04 2013 Petr Pisar <ppisar@redhat.com> - 0.031-1
- 0.031 bump

* Thu Jan 24 2013 Petr Pisar <ppisar@redhat.com> - 0.030-1
- 0.030 bump

* Mon Jan 14 2013 Petr Pisar <ppisar@redhat.com> - 0.029-1
- 0.029 bump

* Tue Aug 21 2012 Petr Pisar <ppisar@redhat.com> - 0.028-5
- Run-require Exporter

* Thu Aug 16 2012 Petr Pisar <ppisar@redhat.com> - 0.028-4
- Specify all dependencies

* Wed Aug 15 2012 Daniel Mach <dmach@redhat.com> - 0.028-3.1
- Rebuild for perl 5.16

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.028-2
- Perl 5.16 rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.028-1
- 0.028 bump

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 0.027-1
- 0.027 bump

* Mon Feb 27 2012 Petr Pisar <ppisar@redhat.com> - 0.026-1
- 0.026 bump

* Mon Jan 23 2012 Petr Pisar <ppisar@redhat.com> - 0.025-1
- 0.025 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Petr Pisar <ppisar@redhat.com> - 0.024-1
- 0.024 bump

* Fri Dec 09 2011 Petr Pisar <ppisar@redhat.com> - 0.023-1
- 0.023 bump

* Fri Nov 25 2011 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 0.021-1
- 0.021 bump
- Remove RPM 4.8 filter

* Mon Jul 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.020-3
- add new filter

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.020-2
- Perl mass rebuild

* Mon Apr 04 2011 Petr Pisar <ppisar@redhat.com> - 0.020-1
- 0.020 bump

* Wed Mar 02 2011 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.019 bump

* Thu Feb 17 2011 Petr Pisar <ppisar@redhat.com> - 0.018-1
- 0.018 bump
- Remove BuildRoot stuff

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Petr Pisar <ppisar@redhat.com> - 0.017-1
- 0.017 bump

* Thu Jan 06 2011 Petr Pisar <ppisar@redhat.com> - 0.016-1
- 0.016 bump

* Wed Oct 27 2010 Petr Pisar <ppisar@redhat.com> - 0.015-1
- 0.015 bump

* Mon Oct 18 2010 Petr Pisar <ppisar@redhat.com> - 0.014-1
- 0.014 bump

* Mon Oct 04 2010 Petr Pisar <ppisar@redhat.com> - 0.012-1
- 0.012 bump

* Wed Sep 22 2010 Petr Pisar <ppisar@redhat.com> - 0.011-1
- 0.011 bump
- Remove unversioned Requires

* Thu Sep 16 2010 Petr Pisar <ppisar@redhat.com> - 0.010-1
- 0.010 bump

* Tue Jun  8 2010 Petr Pisar <ppisar@redhat.com> - 0.007-1
- Specfile autogenerated by cpanspec 1.78 (bug #598553).
