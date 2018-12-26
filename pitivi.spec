Summary:	Non-linear video editor
Summary(pl.UTF-8):	Nieliniowy edytor filmów
Name:		pitivi
Version:	0.999
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/0.999/%{name}-%{version}.tar.xz
# Source0-md5:	5f321c64dc20086f0f6737b42e73f557
URL:		http://www.pitivi.org/
BuildRequires:	cairo-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel >= 1.32.0
BuildRequires:	gstreamer-devel >= 1.10.2
BuildRequires:	gstreamer-plugins-base-devel >= 1.10.2
BuildRequires:	gstreamer-transcoder-devel >= 1.8.1
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	itstool
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pycairo-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	yelp-tools
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	gstreamer-audiosink >= 1.10.2
Requires:	gstreamer-editing-services >= 1.10.2
Requires:	gstreamer-plugins-good >= 1.10.2
Requires:	gstreamer-transcoder >= 1.8.1
Requires:	gstreamer-videosink >= 1.10.2
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Requires:	python3-gstreamer >= 1.10.2
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
CC="%{__cc}" \
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
meson build \
	--buildtype=plain \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

ninja -C build -v

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT \
ninja -C build install -v

# omitted by meson
install -d $RPM_BUILD_ROOT{%{_datadir}/mime/packages,%{_mandir}/man1}
cp -p docs/pitivi.1 $RPM_BUILD_ROOT%{_mandir}/man1

# junk installed by meson
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pitivi/python/pitivi/{configure.py.in,coptimizations/renderer.c}

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
%doc AUTHORS COPYING NEWS README
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
%{_libdir}/%{name}/python/pitivi/viewer
%{_datadir}/%{name}
%{_datadir}/appdata/org.pitivi.Pitivi.appdata.xml
%{_datadir}/mime/packages/org.pitivi.Pitivi-mime.xml
%{_desktopdir}/org.pitivi.Pitivi.desktop
%{_iconsdir}/hicolor/*x*/apps/org.pitivi.Pitivi.png
%{_iconsdir}/hicolor/*x*/mimetypes/text-x-xges.png
%{_iconsdir}/hicolor/symbolic/apps/org.pitivi.Pitivi-symbolic.svg
%{_mandir}/man1/pitivi.1*
