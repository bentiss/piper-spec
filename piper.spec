%global gitdate 20160308
%global gitversion f475a78a6

Name:           piper
Version:        0.1
Release:        1%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
Summary:        Piper is a GTK-based utility to configure gaming mice.

License:        GPLv2
URL:            https://github.com/libratbag/piper
%if 0%{?gitdate}
Source0:        %{name}-%{gitdate}.tar.xz
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        https://github.com/libratbag/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildArch:      noarch
BuildRequires:  python3-setuptools python3-devel
BuildRequires:  desktop-file-utils
Requires:       ratbagd-python

%description
Piper is a GTK-based utility to access, inspect and configure mice with
multiple hardware profiles and/or resolutions.

%prep
%setup -q -n %{name}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
%py3_build

%install
%py3_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%{_bindir}/piper
%{python3_sitelib}/*
%{_datadir}/applications/piper.desktop

%changelog
* Tue Mar 08 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.1-1.20160308:f475a78a6
- git snapshot

* Tue Mar 08 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.1-1
- Initial release
