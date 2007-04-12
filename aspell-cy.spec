%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# WARNING
# To build this package, you must set LC_ALL to cy
# example : LC_ALL=cy rpm -ba aspell-cy.speco

%define src_ver 0.50-3
%define languagelocal cymraeg
%define languageeng welsh
%define languageenglazy Welsh
%define languagecode cy
%define lc_ctype cy_CY

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.3
Release:	%mkrel 11
Group:		System/Internationalization
Source:		http://aspell.sourceforge.net/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPL
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides: spell-cy

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
BuildRequires:	locales-cy

# Mandrake Stuff
Requires:	locales-%{languagecode}
Provides:	aspell-dictionary

Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build
export LC_ALL=cy

./configure
%make

%install
rm -fr $RPM_BUILD_ROOT

export LC_ALL=cy

make DESTDIR=$RPM_BUILD_ROOT install

# fix doc perms
chmod 644 README

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_libdir}/aspell-*/*


