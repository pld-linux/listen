# $Revision: 1.9 $Date: 2009-07-16 08:26:32 $
Summary:	Feature rich media player for GNOME
Summary(pl.UTF-8):	Pełnowartościowy odtwarzacz dla GNOME
Name:		listen
Version:	0.6.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://download.listen-project.org/lastest/%{name}-%{version}.tar.gz
# Source0-md5:	d5b039a1679246ab6224a4aefe16e1be
Source1:	%{name}
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.listen-project.org/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-gstreamer-devel
BuildRequires:	python-mutagen
BuildRequires:	python-pygtk-devel >= 2:2.6.0
BuildRequires:	python-pywebkitgtk-devel
Requires:	python >= 1:2.3
Requires:	python-Imaging
Requires:	python-gnome-extras-egg
Requires:	python-gnome-extras-gtkhtml
Requires:	python-gstreamer >= 0.8.2
Requires:	python-mad
Requires:	python-pygtk-gtk >= 2:2.6.0
Requires:	python-pyvorbis
Requires:	python-sqlite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Listen is a Music player and management for GNOME.

%description -l pl.UTF-8
Listen jest odtwarzaczem i zarządcą muzyki dla GNOME.

%prep
%setup -q
# %patch0 -p1
# %patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_datadir}/listen
%{_libdir}/%{name}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_datadir}/dbus-1/services/org.gnome.Listen.service
%{_mandir}/man1/listen.1
