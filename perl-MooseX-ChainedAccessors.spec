%define upstream_name    MooseX-ChainedAccessors
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Accessor class for chained accessors with Moose
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Moose/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Modifies the Accessor Metaclass to use MooseX::ChainedAccessors::Accessor

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 655370
- new version 0.02
- rebuild for updated spec-helper

* Wed Mar 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 513909
- import perl-MooseX-ChainedAccessors


* Wed Mar 03 2010 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist
