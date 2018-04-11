%define debug_package %{nil}
Summary:        aws sdk for c++
Group:          Development/Libraries
Name:           aws-sdk-cpp
Version:        1.4.33
Release:        2%{?dist}
Vendor:         VMware, Inc.
Distribution:   Photon
License:        Apache 2.0
Url:            https://github.com/aws/aws-sdk-cpp
Source0:        aws-sdk-cpp-%{version}.tar.gz
%define sha1    aws-sdk-cpp=5db6bed30cb85c59c7a3a58034f222007e6a9e49
Requires:       openssl-devel
Requires:       curl-devel
Requires:       zlib-devel
Requires:       aws-sdk-core = %{version}-%{release}
Requires:       aws-sdk-kinesis = %{version}-%{release}
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
The AWS SDK for C++ provides a modern C++ (version C++ 11 or later) interface for Amazon Web Services (AWS).

%package -n     aws-sdk-core
Summary:        aws sdk core
Group:          Development/Libraries
Requires:       aws-core-libs = %{version}-%{release}

%description -n aws-sdk-core
aws sdk cpp core

%package -n     aws-core-libs
Summary:        aws core libs
Group:          Development/Libraries
Requires:       openssl-devel
Requires:       curl-devel
Requires:       zlib-devel

%description -n aws-core-libs
aws core libs

%package -n     aws-sdk-kinesis
Summary:        aws sdk kinesis
Group:          Development/Libraries
Requires:       aws-sdk-core = %{version}-%{release}

%description -n aws-sdk-kinesis
aws sdk cpp for kinesis

%package -n     aws-kinesis-libs
Summary:        aws kinesis libs
Group:          Development/Libraries
Requires:       aws-core-libs = %{version}-%{release}

%description -n aws-kinesis-libs
aws kinesis libs

%prep
%setup

%build
mkdir build
cd build
cmake \
-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
-DCMAKE_BUILD_TYPE=Release ..
make %{?_smp_mflags}


%install
cd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_lib64dir}/cmake

%clean
rm -rf %{buildroot}/*

# Pre-install
%pre

    # First argument is 1 => New Installation
    # First argument is 2 => Upgrade

# Post-install
%post

    # First argument is 1 => New Installation
    # First argument is 2 => Upgrade

    /sbin/ldconfig

# Pre-uninstall
%preun

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

# Post-uninstall
%postun

    /sbin/ldconfig

    # First argument is 0 => Uninstall
    # First argument is 1 => Upgrade

%files
    %defattr(-,root,root,0755)
    %exclude %{_includedir}/aws/core
    %exclude %{_includedir}/aws/kinesis
    %exclude %{_lib64dir}/pkgconfig/aws-cpp-sdk-core.pc
    %exclude %{_lib64dir}/pkgconfig/aws-cpp-sdk-kinesis.pc
    %exclude %{_lib64dir}/libaws-cpp-sdk-core.so
    %exclude %{_lib64dir}/libaws-cpp-sdk-core.so
    %{_lib64dir}/*
    %{_includedir}/*

%files -n aws-sdk-core
    %defattr(-,root,root,0755)
    %{_includedir}/aws/core/*
    %{_lib64dir}/pkgconfig/aws-cpp-sdk-core.pc

%files -n aws-core-libs
    %defattr(-,root,root,0755)
    %{_lib64dir}/libaws-cpp-sdk-core.so

%files -n aws-sdk-kinesis
    %defattr(-,root,root,0755)
    %{_includedir}/aws/kinesis/*
    %{_lib64dir}/pkgconfig/aws-cpp-sdk-kinesis.pc

%files -n aws-kinesis-libs
    %defattr(-,root,root,0755)
    %{_lib64dir}/libaws-cpp-sdk-kinesis.so

%changelog
*   Thu Apr 12 2018 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.4.33-2
-   Split core and kinesis to separate pkgs
*   Wed Apr 11 2018 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.4.33-1
-   Initial build.  First version