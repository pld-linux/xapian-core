#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_with	sse		# SSE instructions
%bcond_with	sse2		# SSE2 instructions
%bcond_without	static_libs	# static library

%ifarch pentium4 %{x8664} x32
%define	with_sse2	1
%endif
%ifarch pentium3 pentium4 %{x8664} x32
%define	with_sse	1
%endif
Summary:	The Xapian Probabilistic Information Retrieval Library
Summary(pl.UTF-8):	Xapian - biblioteka uzyskiwania informacji probabilistycznych
Name:		xapian-core
Version:	1.4.18
Release:	1
License:	GPL v2+
Group:		Applications/Databases
Source0:	https://oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	dd1b30f9b307b06fab319d3258fe65ee
URL:		https://xapian.org/
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libuuid-devel
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

%description -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania.

%package libs
Summary:	Xapian search engine library
Summary(pl.UTF-8):	Biblioteka silnika wyszukiwania Xapian
Group:		Libraries

%description libs
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the library for applications using Xapian
functionality.

%description libs -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet udostępnia bibliotekę dla
aplikacji wykorzystujących funkcjonalność Xapiana.

%package devel
Summary:	Files needed for building packages which use Xapian
Summary(pl.UTF-8):	Pliki niezbędne do tworzenia pakietów wykorzystujących Xapiana
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7
Requires:	libuuid-devel
Requires:	zlib-devel

%description devel
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for building packages which use
Xapian.

%description devel -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki niezbędne do
tworzenia pakietów wykorzystujących Xapiana.

%package static
Summary:	Static Xapian library
Summary(pl.UTF-8):	Statyczna biblioteka Xapian
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xapian library.

%description static -l pl.UTF-8
Statyczna biblioteka Xapian.

%package apidocs
Summary:	Xapian API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Xapian
Group:		Documentation
BuildArch:	noarch

%description apidocs
API and internal documentation for Xapian library.

%description apidocs -l pl.UTF-8
Dokumentacja API i wewnętrzna biblioteki Xapian.

%prep
%setup -q

cp -a examples _examples
%{__rm} _examples/Makefile*

%build
%configure \
	--enable-sse=%{!?with_sse:no}%{?with_sse:sse%{?with_sse2:2}} \
	--enable-static%{!?with_static_libs:=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	docdir=%{_docdir}/%{name}-apidocs-%{version} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C docs install \
	docdir=%{_docdir}/%{name}-apidocs-%{version} \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a ChangeLog.examples _examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxapian.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* HACKING NEWS PLATFORMS README
%attr(755,root,root) %{_bindir}/copydatabase
%attr(755,root,root) %{_bindir}/quest
%attr(755,root,root) %{_bindir}/simpleexpand
%attr(755,root,root) %{_bindir}/simpleindex
%attr(755,root,root) %{_bindir}/simplesearch
%attr(755,root,root) %{_bindir}/xapian-check
%attr(755,root,root) %{_bindir}/xapian-compact
%attr(755,root,root) %{_bindir}/xapian-delve
%attr(755,root,root) %{_bindir}/xapian-metadata
%attr(755,root,root) %{_bindir}/xapian-pos
%attr(755,root,root) %{_bindir}/xapian-progsrv
%attr(755,root,root) %{_bindir}/xapian-replicate
%attr(755,root,root) %{_bindir}/xapian-replicate-server
%attr(755,root,root) %{_bindir}/xapian-tcpsrv
%{_datadir}/xapian-core
%{_mandir}/man1/copydatabase.1*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/xapian-check.1*
%{_mandir}/man1/xapian-compact.1*
%{_mandir}/man1/xapian-config.1*
%{_mandir}/man1/xapian-delve.1*
%{_mandir}/man1/xapian-metadata.1*
%{_mandir}/man1/xapian-pos.1*
%{_mandir}/man1/xapian-progsrv.1*
%{_mandir}/man1/xapian-replicate.1*
%{_mandir}/man1/xapian-replicate-server.1*
%{_mandir}/man1/xapian-tcpsrv.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxapian.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxapian.so.30

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xapian-config
%attr(755,root,root) %{_libdir}/libxapian.so
%{_libdir}/cmake/xapian
%{_includedir}/xapian
%{_includedir}/xapian.h
%{_pkgconfigdir}/xapian-core.pc
%{_aclocaldir}/xapian.m4
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxapian.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}-apidocs-%{version}
%{_docdir}/%{name}-apidocs-%{version}/*.html
%{_docdir}/%{name}-apidocs-%{version}/apidoc
%endif
