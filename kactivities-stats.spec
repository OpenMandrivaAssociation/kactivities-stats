%define major 1
%define libname %mklibname KF5ActivitiesStats %{major}
%define devname %mklibname KF5ActivitiesStats -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%global optflags %{optflags} -O3

Name: kactivities-stats
Version: 5.116.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: A library for accessing the usage data collected by the activities system
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Config) >= %{version}
BuildRequires: cmake(KF5Activities)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}

%description
A library for accessing the usage data collected by the activities system

%package -n %{libname}
Summary: KDE Frameworks 5 Activities framework
Group: System/Libraries
Requires: qt5-database-plugin-sqlite
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 Activities framework.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Activities library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Activities library.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# Private library
rm -f %{buildroot}%{_libdir}/libkactivitymanagerd_plugin.so

%files
%{_datadir}/qlogging-categories5/kactivities-stats.*categories

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/KF5/KActivitiesStats
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/pkgconfig/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
