%define		_zathura_api_ver	%(pkg-config --variable=apiversion zathura 2> /dev/null || echo -1)
%define		_zathura_abi_ver	%(pkg-config --variable=abiversion zathura 2> /dev/null || echo -1)

Summary:	mupdf based PDF plugin for zathura
Summary(pl.UTF-8):	Wtyczka PDF dla zathury oparta na silniku mupdf
Name:		zathura-pdf-mupdf
Version:	2026.07.18
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-pdf-mupdf/download/%{name}-%{version}.tar.xz
# Source0-md5:	2775e326f660470632b11f195fb330ee
Patch0:		mupdf_1.18.patch
URL:		https://pwmt.org/projects/zathura-pdf-mupdf/
BuildRequires:	cairo-devel
# C23
BuildRequires:	gcc >= 6:14
BuildRequires:	girara-devel >= 2026.02.03
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.2
BuildRequires:	gumbo-parser-devel
BuildRequires:	meson >= 1
BuildRequires:	mupdf-devel >= 1.26.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 2026.07.18
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 2026.02.03
%requires_eq_to	mupdf-libs mupdf-devel
Requires:	zathura >= 2026.07.18
Requires:	zathura(plugin-abi) = %_zathura_abi_ver
Requires:	zathura(plugin-api) = %_zathura_api_ver
Conflicts:	zathura-pdf-poppler
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-pdf-mupdf plugin adds PDF support to zathura by using the
mupdf rendering engine.

%description -l pl.UTF-8
Wtyczka zathura-pdf-mupdf dodaje do zathury obsługę PDF z
wykorzystaniem silnika renderującego mupdf.

%prep
%setup -q
%patch -P0 -p1

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
