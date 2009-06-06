Summary:	Video editor
Summary(pl.UTF-8):	Edytor wideo
Name:		pitivi
Version:	0.13.1
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/0.13/%{name}-%{version}.tar.bz2
# Source0-md5:	a925ac7404f0235d22ec09479696ccd6
Patch0:		%{name}-desktop.patch
URL:		http://www.pitivi.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	python >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	shared-mime-info
Requires:	Zope-Interface
Requires:	gstreamer-audiosink >= 0.10.23
Requires:	gstreamer-gnonlin >= 0.10.11
Requires:	gstreamer-plugins-good
Requires:	gstreamer-videosink >= 0.10.23
Requires:	hicolor-icon-theme
Requires:	python-gstreamer >= 0.10.15
Requires:	python-pycairo
Requires:	python-pygoocanvas
Requires:	python-pygtk-glade >= 2:2.12.0
Requires:	python-pygtk-gtk >= 2:2.12.0
Requires:	python-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PiTiVi is a program for video editing based on the GStreamer.

%description -l pl.UTF-8
PiTiVi jest programem do edycji wideo używającym GStreamera.

%prep
%setup -q
%patch0 -p1

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

%find_lang %{name}

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
%attr(755,root,root) %{_bindir}/pitivi
%{_libdir}/pitivi
%{_datadir}/mime/packages/pitivi.xml
%{_datadir}/pitivi
%{_desktopdir}/pitivi.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_pixmapsdir}/pitivi.png
