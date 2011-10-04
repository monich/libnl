# 
# Do not Edit! Generated by:
# spectacle version 0.16
# 
# >> macros
# << macros

Name:       libnl
Summary:    Convenience library for kernel netlink sockets
Version:    1.1
Release:    1
Group:      System/Libraries
License:    LGPL
URL:        http://people.suug.ch/~tgr/libnl/
Source0:    http://people.suug.ch/~tgr/libnl/files/libnl-%{version}.tar.gz
Source100:  libnl.yaml
Patch0:     libnl-1.0-pre5-static.patch
Patch1:     libnl-1.0-pre5-debuginfo.patch
Patch2:     libnl-1.0-pre8-use-vasprintf-retval.patch
Patch3:     libnl-1.0-pre8-more-build-output.patch
Patch4:     libnl-1.1-include-limits-h.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This package contains a convenience library to simplify
using the Linux kernel's netlink sockets interface for
network manipulation



%package devel
Summary:    Libraries and headers for using libnl
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains various headers for using libnl


%prep
%setup -q -n %{name}-%{version}

# libnl-1.0-pre5-static.patch
%patch0 -p1
# libnl-1.0-pre5-debuginfo.patch
%patch1 -p1
# libnl-1.0-pre8-use-vasprintf-retval.patch
%patch2 -p1
# libnl-1.0-pre8-more-build-output.patch
%patch3 -p1
# libnl-1.1-include-limits-h.patch
%patch4 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc COPYING
%{_libdir}/%{name}.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc doc/*
%{_includedir}/netlink/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}-1.pc
# << files devel

