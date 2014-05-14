#TODO: devel package
%define		_state		stable
%define		orgname		palapeli
%define		qtver		4.8.0

Summary:	Palapeli
Name:		kde4-%{orgname}
Version:	4.13.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	6278509f2c172691d1210174e96d1b3e
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Palapeli.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/palapeli
%attr(755,root,root) %{_libdir}/kde4/palapeli_jigsawslicer.so
%attr(755,root,root) %{_libdir}/kde4/palapeli_rectslicer.so
%attr(755,root,root) %{_libdir}/kde4/palathumbcreator.so
%attr(755,root,root) %{_libdir}/kde4/palapeli_goldbergslicer.so
%attr(755,root,root) %ghost %{_libdir}/libpala.so.?
%attr(755,root,root) %{_libdir}/libpala.so.*.*.*
%{_datadir}/apps/palapeli
%{_datadir}/kde4/services/ServiceMenus/palapeli_servicemenu.desktop
%{_datadir}/kde4/services/palapeli_jigsawslicer.desktop
%{_datadir}/kde4/services/palapeli_rectslicer.desktop
%{_datadir}/kde4/services/palathumbcreator.desktop
%{_datadir}/kde4/services/palapeli_goldbergslicer.desktop
%{_datadir}/kde4/servicetypes/libpala-slicerplugin.desktop
%{_datadir}/mime/packages/palapeli-mimetypes.xml
%{_desktopdir}/kde4/palapeli.desktop
%{_datadir}/config/palapeli-collectionrc
%{_iconsdir}/hicolor/*x*/apps/palapeli.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-palapeli.png
