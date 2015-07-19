%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# WARNING
# To build this package, you must set LC_ALL to cy
# example :	LC_ALL=cy rpm -ba aspell-cy.speco

%define src_ver 0.50-3
%define languagelocal cymraeg
%define languageeng welsh
%define languageenglazy Welsh
%define languagecode cy
%define lc_ctype cy_CY

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Epoch:		1
Version:	0.50.3
Release:	29
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.sourceforge.net/
Source0:	http://aspell.sourceforge.net/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
BuildRequires:	locales-cy
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	spell-cy
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}

%build
export LC_ALL=cy

./configure
%make

%install
export LC_ALL=cy
%makeinstall_std

# fix doc perms
chmod 644 README

%files
%doc README
%{_libdir}/aspell-*/*

