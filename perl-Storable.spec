#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Storable
Version  : 3.25
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/Storable-3.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/Storable-3.25.tar.gz
Summary  : 'persistence for Perl data structures'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Storable-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Storable 3.05c
------------------------------------------------------------------------
This program is free software; you can redistribute it and/or modify
it under the same terms as Perl 5 itself.

%package perl
Summary: perl components for the perl-Storable package.
Group: Default
Requires: perl-Storable = %{version}-%{release}

%description perl
perl components for the perl-Storable package.


%prep
%setup -q -n Storable-3.25
cd %{_builddir}/Storable-3.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
## Remove excluded files
rm -f %{buildroot}*/usr/share/man/man3/Storable.3

%files
%defattr(-,root,root,-)

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
