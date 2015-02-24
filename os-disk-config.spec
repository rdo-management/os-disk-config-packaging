Name:		os-disk-config
Version:	0.0.1
Release:	1%{?dist}
Summary:	Disk configuration and modification tool

Group:		Development/Languages
License:	ASL 2.0
URL:		https://github.com/rdo-management/os-disk-config
Source0:	https://github.com/rdo-management/os-disk-config/archive/%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python2-devel

Requires:	python-blivet

%description
os-disk-config is a disk configuration tool that will partition
a disk based on the input of a JSON or yaml file.

%prep
%setup -q -n %{name}-%{version}

%build
PBR_VERSION=%{version} %{__python} setup.py build

%install
PBR_VERSION=%{version} %{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-disk-config
%{python2_sitelib}/os_disk_config
%{python2_sitelib}/*.egg-info

%changelog
* Thu Feb 12 2015 Ryan Hallisey <rhallise@redhat.com> 0.0.1-1
- Initial build
