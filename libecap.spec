# eCap: The Code in the Middle (http://www.e-cap.org/)
Name: libecap
Version: 0.0.3
Release: 2%{dist}
Vendor: The Measurement Factory
License: GPL
Group: System Environment/Libraries
Packager: ClearFoundation
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
Summary: eCAP is an interface that lets Squid and other servers to use embedded adaptation modules
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
eCAP is a software interface that allows a network application, such as an HTTP
proxy or an ICAP server, to outsource content analysis and adaptation to a
loadable module.

%package devel
Summary: eCAP development files
Group: Development/Libraries
Requires: libecap = 0.0.3
BuildArch: noarch

%description devel
eCAP is a software interface that allows a network application, such as an HTTP
proxy or an ICAP server, to outsource content analysis and adaptation to a
loadable module.

# Build
%prep
%setup -q
./bootstrap.sh
%{configure}

%build
make %{?_smp_mflags}

# Install
%install
make install DESTDIR=$RPM_BUILD_ROOT

# Clean-up
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Post install
%post
/sbin/ldconfig

# Post uninstall
%postun
/sbin/ldconfig

# Files
%files
%defattr(-,root,root)
%{_libdir}/libecap.so*

# Developer files
%files devel
%defattr(-,root,root)
%{_libdir}/libecap.a
%{_libdir}/libecap.la
%{_includedir}/libecap

# vi: expandtab shiftwidth=4 softtabstop=4 tabstop=4
