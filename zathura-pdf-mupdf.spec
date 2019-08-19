Summary:	mupdf based PDF plugin for zathura
Summary(pl.UTF-8):	Wtyczka PDF dla zathury oparta na silniku mupdf
Name:		zathura-pdf-mupdf
Version:	0.3.5
Release:	2
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-pdf-mupdf/download/%{name}-%{version}.tar.xz
# Source0-md5:	4b48f04c5275210f566900a70abc79aa
URL:		https://pwmt.org/projects/zathura-pdf-mupdf/
BuildRequires:	cairo-devel
# C11
BuildRequires:	gcc >= 6:4.7
BuildRequires:	girara-devel >= 0.2.3
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.2
BuildRequires:	meson >= 0.43
BuildRequires:	mupdf-devel >= 1.16
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 0.3.9
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.2.3
%requires_eq	mupdf
Requires:	zathura >= 0.3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-pdf-mupdf plugin adds PDF support to zathura by using the
mupdf rendering engine.

%description -l pl.UTF-8
Wtyczka zathura-pdf-mupdf dodaje do zathury obsługę PDF z
wykorzystaniem silnika renderującego mupdf.

%prep
%setup -q

%build
%meson build

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_libdir}/zathura/libpdf-mupdf.so
%{_datadir}/metainfo/org.pwmt.zathura-pdf-mupdf.metainfo.xml
%{_desktopdir}/org.pwmt.zathura-pdf-mupdf.desktop
