# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate anyhow

Name:           rust-%{crate}
Version:        1.0.40
Release:        1%{?dist}
Summary:        Flexible concrete Error type built on std::error::Error

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/anyhow
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Flexible concrete Error type built on std::error::Error.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages
which use "backtrace" feature of "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sun Mar 28 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.40-1
- Update to version 1.0.40.
- Fixes RHBZ#1943642

* Sun Mar 21 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.39-1
- Update to version 1.0.39.
- Fixes RHBZ#1941120

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.38-1
- Update to version 1.0.38.
- Fixes RHBZ#1914718

* Tue Dec 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.37-1
- Update to version 1.0.37.
- Fixes RHBZ#1911354

* Sat Dec 26 12:15:27 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.36-1
- Update to 1.0.36

* Mon Dec 07 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.35-1
- Update to version 1.0.35.
- Fixes RHBZ#1904750

* Thu Nov 05 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.34-1
- Update to version 1.0.34.
- Fixes RHBZ#1893913

* Wed Oct 07 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.33-1
- Update to version 1.0.33.

* Wed Jul 29 2020 Josh Stone <jistone@redhat.com> - 1.0.32-1
- Update to 1.0.32

* Fri May 15 2020 Josh Stone <jistone@redhat.com> - 1.0.31-1
- Update to 1.0.31

* Wed May 13 2020 Josh Stone <jistone@redhat.com> - 1.0.30-1
- Update to 1.0.30

* Wed Apr 01 2020 Josh Stone <jistone@redhat.com> - 1.0.28-1
- Update to 1.0.28

* Sun Mar 15 09:06:14 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.27-1
- Update to 1.0.27

* Fri Feb 14 10:34:04 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.26-1
- Initial package
