Summary:	mupdf based PDF plugin for zathura
Name:		zathura-pdf-mupdf
Version:	0.2.7
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura/plugins/download/%{name}-%{version}.tar.gz
# Source0-md5:	b89b45289c8ec77854de4afc149cd1a4
URL:		https://pwmt.org/projects/zathura-pdf-mupdf/
BuildRequires:	girara-devel >= 0.2.3
BuildRequires:	gtk+3-devel >= 3.2
BuildRequires:	jbig2dec-devel
BuildRequires:	libjpeg-devel
BuildRequires:	openjpeg2-devel
BuildRequires:	pkgconfig
BuildRequires:	mujs-devel
BuildRequires:	mupdf-devel
BuildRequires:	openssl-devel
BuildRequires:	zathura-devel >= 0.2.0
Requires:	zathura >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-pdf-mupdf plugin adds PDF support to zathura by using
the mupdf rendering engine.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%attr(755,root,root) %{_libdir}/zathura/pdf.so
%{_desktopdir}/%{name}.desktop
