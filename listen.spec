# $Revision: 1.2 $Date: 2006-02-08 15:21:48 $
#
Summary:	Future rich media player for GNOME
Summary(pl):	Pełnowartościowy odtwarzacz dla GNOME
Name:		listen
Version:	0.2.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://listengnome.free.fr/packages/src/%{name}-%{version}.tar.gz
# Source0-md5:	67a755437a3c3db2d7640fdc959a7419
Source1:	%{name}
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://listengnome.free.fr/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
Requires:	python >= 2.3
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

%description -l pl
Listen jest odtwarzaczem i zarządcą muzyki dla GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog
%attr(755,root,root) %{_bindir}/listen
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
