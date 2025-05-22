%define		_zathura_api_ver	%(pkg-config --variable=apiversion zathura 2> /dev/null || echo -1)
%define		_zathura_abi_ver	%(pkg-config --variable=abiversion zathura 2> /dev/null || echo -1)

Summary:	mupdf based PDF plugin for zathura
Summary(pl.UTF-8):	Wtyczka PDF dla zathury oparta na silniku mupdf
Name:		zathura-pdf-mupdf
Version:	0.4.4
Release:	4
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-pdf-mupdf/download/%{name}-%{version}.tar.xz
# Source0-md5:	f9fe42196f621833a0b57025bd88a119
Patch0:		mupdf_1.18.patch
URL:		https://pwmt.org/projects/zathura-pdf-mupdf/
BuildRequires:	cairo-devel
# C17
BuildRequires:	gcc >= 6:8.1.0
BuildRequires:	girara-devel >= 0.2.3
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.2
BuildRequires:	gumbo-parser-devel
BuildRequires:	meson >= 0.61
BuildRequires:	mupdf-devel >= 1.24.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 0.5.2
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.2.3
%requires_eq_to	mupdf-libs mupdf-devel
Requires:	zathura >= 0.5.2
Requires:	zathura(plugin-abi) = %_zathura_abi_ver
Requires:	zathura(plugin-api) = %_zathura_api_ver
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
