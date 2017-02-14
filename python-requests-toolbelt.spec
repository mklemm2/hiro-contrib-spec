%{?scl:%scl_package python-requests-toolbelt}
%{!?scl:%global pkg_name %{name}}

%global pypi_name requests-toolbelt

Name:           %{?scl_prefix}python-requests-toolbelt
Version:        0.7.1
Release:        1%{?dist}
Summary:        A utility belt for advanced users of python-requests

License:        Apache 2.0
URL:            https://toolbelt.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix_python}python-devel
BuildRequires:  %{?scl_prefix_python}python-setuptools
%{?scl:BuildRequires: %{scl}-build %{scl}-runtime}
%{?scl:Requires: %{scl}-runtime}
%{?scl:Requires: %{scl}-python-requests}

%description
This is just a collection of utilities for pythonrequests_,
but don't really belong in requests proper. The minimum tested requests version
is 2.1.0. In reality, the toolbelt should work with 2.0.1 as well, but some
idiosyncracies prevent effective or sane testing on that version.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
# Explicitly specify --install-purelib %{python_sitelib}, which is now overriden
# to point to vt191, otherwise Python will try to install into the python27
# Software Collection site-packages directory
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib %{python_sitelib}
%{?scl:"}

%files
%{python_sitelib}/requests_toolbelt*

%changelog
* Wed Jan 22 2014 John Doe <jdoe@example.com> - 1.9.1-1
- Built for vt191 SCL.
