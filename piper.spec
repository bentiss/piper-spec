Name:           piper
Version:        0.1
Release:        2%{?dist}
Summary:        Piper is a GTK-based utility to configure gaming mice.

License:        GPLv2
URL:            https://github.com/libratbag/piper
Source0:        https://github.com/libratbag/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-setuptools python3-devel
BuildRequires:  desktop-file-utils
Requires:       ratbagd-python

%description
Piper is a GTK-based utility to access, inspect and configure mice with
multiple hardware profiles and/or resolutions.

%prep
%setup -q -n %{name}-%{version}

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
* Fri Mar 18 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.1-2
- remove git snapshots hooks in the specfile

* Tue Mar 08 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.1-1.20160308:f475a78a6
- git snapshot

* Tue Mar 08 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.1-1
- Initial release
