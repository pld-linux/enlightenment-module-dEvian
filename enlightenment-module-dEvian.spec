
%define		_module_name	dEvian
%define		_module_name_lc	devian

Summary:	Enlightenment DR17 module: %{_module_name}
Summary(pl):	Modu³ Enlightenmenta DR17: kalendarz
Name:		enlightenment-module-%{_module_name}
Version:	0.1.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
# Source0-md5:	c904d7baedb9ffa18da7fae0b907bb2e
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenmentDR17-devel
BuildRequires:	embryo-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	enlightenmentDR17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A module to display images on your desktop.

%prep
%setup -q -n %{_module_name}-%{version}
sed -e 's|datadir=.*|datadir="`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_DATA_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_LIB_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`"|' \
    -i configure.in

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name_lc}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name_lc}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name_lc}/linux-gnu-*/module.so
# violates FHS
%{_libdir}/enlightenment/modules_extra/%{_module_name_lc}/themes
%{_libdir}/enlightenment/modules_extra/%{_module_name_lc}/*.png
%{_libdir}/enlightenment/modules_extra/%{_module_name_lc}/*.jpg
