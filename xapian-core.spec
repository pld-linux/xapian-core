# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static library
#
Summary:	The Xapian Probabilistic Information Retrieval Library
Name:		xapian-core
Version:	1.0.4
Release:	0.2
License:	GPL
Group:		Applications/Databases
URL:		http://www.xapian.org/
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-gcc43.patch
# Source0-md5:	57cd26fb4a3677bfe05d4c9df5012357
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

%package apidocs
Summary:	Xapian API documentation
Group:		Documentation

%description apidocs
API and internal documentation for Xapian library.

%package libs
Summary:	Xapian search engine libraries
Group:		Development/Libraries

%description libs
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the libraries for applications using Xapian
functionality.

%package devel
Summary:	Files needed for building packages which use Xapian
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for building packages which use
Xapian.

%package static
Summary:	Static Xapian library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xapian library.

%prep
%setup -q
%patch0 -p0

cp -a examples _examples
rm -f _examples/Makefile*

%build
%configure \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static
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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog HACKING INSTALL NEWS PLATFORMS README
%attr(755,root,root) %{_bindir}/xapian-tcpsrv
%attr(755,root,root) %{_bindir}/xapian-progsrv
%attr(755,root,root) %{_bindir}/quartzcheck
%attr(755,root,root) %{_bindir}/quartzcompact
%attr(755,root,root) %{_bindir}/quartzdump
%attr(755,root,root) %{_bindir}/quest
%attr(755,root,root) %{_bindir}/delve
%attr(755,root,root) %{_bindir}/copydatabase
%attr(755,root,root) %{_bindir}/simpleindex
%attr(755,root,root) %{_bindir}/simplesearch
%attr(755,root,root) %{_bindir}/simpleexpand
%attr(755,root,root) %{_bindir}/xapian-compact
%attr(755,root,root) %{_bindir}/xapian-check
%attr(755,root,root) %{_bindir}/xapian-inspect
%{_mandir}/man1/xapian-check.1*
%{_mandir}/man1/xapian-inspect.1*
%{_mandir}/man1/copydatabase.1*
%{_mandir}/man1/delve.1*
%{_mandir}/man1/quartzcheck.1*
%{_mandir}/man1/quartzcompact.1*
%{_mandir}/man1/quartzdump.1*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/xapian-compact.1*
%{_mandir}/man1/xapian-config.1*
%{_mandir}/man1/xapian-progsrv.1*
%{_mandir}/man1/xapian-tcpsrv.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxapian.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxapian.so.15

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xapian-config
%{_includedir}/xapian
%{_includedir}/xapian.h
%{_libdir}/libxapian.so
%{_libdir}/libxapian.la
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
%doc %{_docdir}/%{name}-apidocs-%{version}/apidoc.pdf
%doc %{_docdir}/%{name}-apidocs-%{version}/*.html
%doc %{_docdir}/%{name}-apidocs-%{version}/apidoc
%endif
