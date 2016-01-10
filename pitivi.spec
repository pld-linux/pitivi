Summary:	Non-linear video editor
Summary(pl.UTF-8):	Nieliniowy edytor filmów
Name:		pitivi
Version:	0.95
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/0.95/%{name}-%{version}.tar.xz
# Source0-md5:	7bb0bca1b25ef592f0105c3ad93b8c20
URL:		http://www.pitivi.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel >= 1.32.0
BuildRequires:	gstreamer-devel >= 1.6.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.6.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pycairo-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	gstreamer-audiosink >= 1.6.0
Requires:	gstreamer-editing-services >= 1.6.0
Requires:	gstreamer-plugins-good >= 1.6.0
Requires:	gstreamer-videosink >= 1.6.0
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Requires:	python3-gstreamer >= 1.6.0
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PiTiVi is a program for video editing based on the GStreamer.

%description -l pl.UTF-8
PiTiVi jest programem do edycji wideo używającym GStreamera.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/python/pitivi/timeline/renderer.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README RELEASE
%attr(755,root,root) %{_bindir}/pitivi
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/python
%dir %{_libdir}/%{name}/python/pitivi
%{_libdir}/%{name}/python/pitivi/*.py
%{_libdir}/%{name}/python/pitivi/__pycache__
%{_libdir}/%{name}/python/pitivi/dialogs
%dir %{_libdir}/%{name}/python/pitivi/timeline
%{_libdir}/%{name}/python/pitivi/timeline/*.py
%{_libdir}/%{name}/python/pitivi/timeline/__pycache__
%attr(755,root,root) %{_libdir}/%{name}/python/pitivi/timeline/renderer.so
%{_libdir}/%{name}/python/pitivi/undo
%{_libdir}/%{name}/python/pitivi/utils
%{_datadir}/%{name}
%{_datadir}/appdata/pitivi.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*x*/apps/pitivi.png
%{_mandir}/man1/pitivi.1*
