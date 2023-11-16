Summary:	mupdf based PDF plugin for zathura
Summary(pl.UTF-8):	Wtyczka PDF dla zathury oparta na silniku mupdf
Name:		zathura-pdf-mupdf
Version:	0.4.1
Release:	2
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-pdf-mupdf/download/%{name}-%{version}.tar.xz
# Source0-md5:	470d7ab5e866b81059089a147ccb84ef
Patch0:		mupdf_1.18.patch
URL:		https://pwmt.org/projects/zathura-pdf-mupdf/
BuildRequires:	cairo-devel
# C11
BuildRequires:	gcc >= 6:4.7
BuildRequires:	girara-devel >= 0.2.3
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.2
BuildRequires:	gumbo-parser-devel
BuildRequires:	meson >= 0.56
BuildRequires:	mupdf-devel >= 1.20.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 0.5.2
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.2.3
%requires_eq_to	mupdf-libs mupdf-devel
Requires:	zathura >= 0.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-pdf-mupdf plugin adds PDF support to zathura by using the
mupdf rendering engine.

%description -l pl.UTF-8
Wtyczka zathura-pdf-mupdf dodaje do zathury obsługę PDF z
wykorzystaniem silnika renderującego mupdf.

%prep
%setup -q
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_libdir}/zathura/libpdf-mupdf.so
%{_datadir}/metainfo/org.pwmt.zathura-pdf-mupdf.metainfo.xml
%{_desktopdir}/org.pwmt.zathura-pdf-mupdf.desktop
