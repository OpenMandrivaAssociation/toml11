%define debug_package %{nil}

%define devname %mklibname toml11 -d

Name: toml11
Version: 3.7.1
Release: 2
Source0: https://github.com/ToruNiina/toml11/archive/refs/tags/v%{version}.tar.gz
Summary: TOML library for modern C++ (C++11 or later)
URL: https://github.com/ToruNiina/toml11
License: MIT
Group: System/Libraries
BuildRequires: cmake ninja

%description
toml11 is a C++11 (or later) header-only toml parser/encoder depending only
on C++ standard library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
