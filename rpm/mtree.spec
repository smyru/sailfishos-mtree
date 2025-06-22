Name: mtree

# >> macros
# << macros

Summary:    NetBSD mtree utility for mapping and checking directory hierarchies
Version:    20130908
Release:    0
Group:      Applications/Utilities
License:    BSD-2-Clause
URL:        https://github.com/smyru/mtree-netbsd
Source:     https://codeload.github.com/smyru/mtree-netbsd/tar.gz/5282105?dummy=/smyru-mtree-netbsd-5282105.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc

%description
The mtree utility compares a file hierarchy against a specification,
creates a specification for a file hierarchy, or modifies a specification.
%if "%{?vendor}" == "chum"
Type: console-application
PackagedBy: smyru
Categories:
 - FileSystem
 - Utility
 - System
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%configure

%build
# >> build pre
# << build pre

# >> build post
make %{?_smp_mflags} mtree
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
%{__make} install PREFIX="%{buildroot}"/usr
# disable man pages
rm -rf %{buildroot}%{_mandir}
# << install post

%files
%defattr(-,root,root,-)
%defattr(-, root, root, 0755)
%{_sbindir}/mtree
# >> files
# << files
