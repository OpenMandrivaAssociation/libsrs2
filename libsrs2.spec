%define	major _2
%define libname %mklibname srs %{major}
%define develname %mklibname srs -d

Summary:	SRS email address rewriting engine
Name:		libsrs2
Version:	1.0.18
Release:	9
License:	BSD
Group:		System/Libraries
URL:		https://www.libsrs2.org/
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
%makeinstall_std

install -d %{buildroot}%{_mandir}/man1
install -m0644 debian/srs.1 %{buildroot}%{_mandir}/man1/

%files -n %{libname}
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h

%files -n srs
%defattr(-,root,root)
%{_bindir}/srs
%{_mandir}/man1/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.18-7mdv2011.0
+ Revision: 620227
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.18-6mdv2010.0
+ Revision: 429832
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.18-5mdv2009.0
+ Revision: 229714
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.18-4mdv2008.0
+ Revision: 83770
- new libname and devel name


* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.18-3mdv2007.0
+ Revision: 93737
- Import libsrs2

* Sat Apr 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.18-3mdk
- rebuild

* Thu Mar 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.18-2mdk
- use the %%mkrel macro
- used naming as in the libalsa2 package

* Thu Oct 21 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.18-1mdk
- initial mandrake package

