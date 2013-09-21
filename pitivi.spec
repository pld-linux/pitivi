Summary:	Non-linear video editor
Summary(pl.UTF-8):	Edytor wideo
Name:		pitivi
Version:	0.15.2
Release:	2
License:	LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/0.15/%{name}-%{version}.tar.xz
# Source0-md5:	e0e379fca759025140ac1316819b2173
Patch0:		pitivi-0.15.0-ignore-unknown-stream-types.patch
URL:		http://www.pitivi.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	Zope-Interface
Requires:	gstreamer-audiosink >= 0.10.29
Requires:	gstreamer-gnonlin >= 0.10.16
Requires:	gstreamer-plugins-good
Requires:	gstreamer-videosink >= 0.10.29
Requires:	hicolor-icon-theme
Requires:	python-gstreamer >= 0.10.19
Requires:	python-pycairo
Requires:	python-pygoocanvas
Requires:	python-pygtk-glade >= 2:2.24.0
Requires:	python-pygtk-gtk >= 2:2.24.0
Requires:	python-pyxdg
Requires:	python-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PiTiVi is a program for video editing based on the GStreamer.

%description -l pl.UTF-8
PiTiVi jest programem do edycji wideo używającym GStreamera.

%prep
%setup -q
%patch0 -p0

%build
%{__intltoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_bindir}/pitivi
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/%{name}.1*
