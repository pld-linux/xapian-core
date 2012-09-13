#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static library
#
Summary:	The Xapian Probabilistic Information Retrieval Library
Summary(pl.UTF-8):	Xapian - biblioteka uzyskiwania informacji probabilistycznych
Name:		xapian-core
Version:	1.2.12
Release:	1
License:	GPL v2+
Group:		Applications/Databases
Source0:	http://oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	faf33a3945edbe4c848627750856cbeb
URL:		http://www.xapian.org/
BuildRequires:	libstdc++-devel
BuildRequires:	libuuid-devel
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

%description libs 
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
Requires:	libstdc++-devel
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING INSTALL NEWS PLATFORMS README
%attr(755,root,root) %{_bindir}/copydatabase
%attr(755,root,root) %{_bindir}/delve
%attr(755,root,root) %{_bindir}/quest
%attr(755,root,root) %{_bindir}/simpleexpand
%attr(755,root,root) %{_bindir}/simpleindex
%attr(755,root,root) %{_bindir}/simplesearch
%attr(755,root,root) %{_bindir}/xapian-check
%attr(755,root,root) %{_bindir}/xapian-chert-update
%attr(755,root,root) %{_bindir}/xapian-compact
%attr(755,root,root) %{_bindir}/xapian-inspect
%attr(755,root,root) %{_bindir}/xapian-metadata
%attr(755,root,root) %{_bindir}/xapian-progsrv
%attr(755,root,root) %{_bindir}/xapian-replicate
%attr(755,root,root) %{_bindir}/xapian-replicate-server
%attr(755,root,root) %{_bindir}/xapian-tcpsrv
%{_mandir}/man1/copydatabase.1*
%{_mandir}/man1/delve.1*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/xapian-check.1*
%{_mandir}/man1/xapian-chert-update.1*
%{_mandir}/man1/xapian-compact.1*
%{_mandir}/man1/xapian-config.1*
%{_mandir}/man1/xapian-inspect.1*
%{_mandir}/man1/xapian-metadata.1*
%{_mandir}/man1/xapian-progsrv.1*
%{_mandir}/man1/xapian-replicate.1*
%{_mandir}/man1/xapian-replicate-server.1*
%{_mandir}/man1/xapian-tcpsrv.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxapian.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxapian.so.22

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xapian-config
%attr(755,root,root) %{_libdir}/libxapian.so
%{_libdir}/libxapian.la
%{_libdir}/cmake/xapian
%{_includedir}/xapian
%{_includedir}/xapian.h
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
%{_docdir}/%{name}-apidocs-%{version}/apidoc.pdf
%{_docdir}/%{name}-apidocs-%{version}/*.html
%{_docdir}/%{name}-apidocs-%{version}/apidoc
%endif
