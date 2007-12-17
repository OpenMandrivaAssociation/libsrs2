%define	major _2
%define libname %mklibname srs %{major}
%define develname %mklibname srs -d

Summary:	SRS email address rewriting engine
Name:		libsrs2
Version:	1.0.18
Release:	%mkrel 4
License:	BSD
Group:		System/Libraries
URL:		http://www.libsrs2.org/
Source0:	http://www.libsrs2.org/srs/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	libtool

%description
libsrs2 is the next generation SRS library. SPF verifies that the
Sender address of a mail matches (according to some policy) the
client IP address which submits the mail. When a mail is forwarded,
the sender address must be rewritten to comply with SPF policy. The
Sender Rewriting Scheme, or SRS, provides a standard for this
rewriting which is not vulnerable to attacks by spammers.

%package -n	%{libname}
Summary:	SRS email address rewriting engine
Group:		System/Libraries

%description -n	%{libname}
libsrs2 is the next generation SRS library. SPF verifies that the
Sender address of a mail matches (according to some policy) the
client IP address which submits the mail. When a mail is forwarded,
the sender address must be rewritten to comply with SPF policy. The
Sender Rewriting Scheme, or SRS, provides a standard for this
rewriting which is not vulnerable to attacks by spammers.

%package -n	%{develname}
Summary:	Development tools needed to build programs that use libsrs2
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	libsrs-devel = %{version}-%{release}
Obsoletes:	%{mklibname srs 2 -d}

%description -n	%{develname}
libsrs2 is the next generation SRS library. SPF verifies that the
Sender address of a mail matches (according to some policy) the
client IP address which submits the mail. When a mail is forwarded,
the sender address must be rewritten to comply with SPF policy. The
Sender Rewriting Scheme, or SRS, provides a standard for this
rewriting which is not vulnerable to attacks by spammers.

This package contains development files needed to compile softwares
against the SRS library.

%package -n	srs
Summary:	Command line interface to libsrs2
Group:		System/Servers

%description -n	srs
Command line interface to libsrs2

%prep

%setup -q

%build

%configure2_5x

make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_mandir}/man1
install -m0644 debian/srs.1 %{buildroot}%{_mandir}/man1/

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h

%files -n srs
%defattr(-,root,root)
%{_bindir}/srs
%{_mandir}/man1/*
