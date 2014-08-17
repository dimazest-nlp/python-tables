%{?scl:%scl_package python-tables}
%{!?scl:%global pkg_name %{name}}

%global module  tables

Summary:        Hierarchical datasets in Python
Name:           %{?scl_prefix}python-%{module}
Version:        3.1.1
Release:        1%{?dist}
Source0:        http://sourceforge.net/projects/pytables/files/pytables/%{version}/%{module}-%{version}.tar.gz
# Source1:        http://sourceforge.net/project/pytables/pytables/%{version}/pytablesmanual-%{version}.pdf

License:        BSD
Group:          Development/Languages
URL:            http://www.pytables.org

Requires:       %{?scl_prefix}numpy
Requires:       %{?scl_prefix}python-numexpr
%{?scl:Requires: %{scl}-runtime}

BuildRequires:  hdf5-devel >= 1.8 bzip2-devel lzo-devel
BuildRequires:  %{?scl_prefix}Cython
BuildRequires:  %{?scl_prefix}numpy
BuildRequires:  %{?scl_prefix}python-numexpr
BuildRequires:  %{?scl_prefix}python-devel
%{?scl:BuildRequires: %{scl}-build %{scl}-runtime}

BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
PyTables is a package for managing hierarchical datasets and designed
to efficiently and easily cope with extremely large amounts of data.

# %package        doc
# Group:          Development/Languages
# Summary:        Documentation for PyTables
# BuildArch:      noarch

# %description doc
# The %{name}-doc package contains the documentation related to
# PyTables.

%prep
%setup -q -n %{module}-%{version}
echo "import tables; tables.test()" > bench/check_all.py

%build
%{?scl:scl enable %{scl} - << \EOF}
CFLAGS="%{optflags}" %{__python3} setup.py build
%{?scl:EOF}

%check
libdir=`ls build/|grep lib`
export PYTHONPATH=`pwd`/build/$libdir
%{?scl:scl enable %{scl} "}
%{__python3} bench/check_all.py
%{?scl:"}

%install
chmod -x examples/check_examples.sh
for i in utils/*; do sed -i 's|bin/env |bin/|' $i; done

%{?scl:scl enable %{scl} "}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

%files
%doc *.txt LICENSES
%{_bindir}/ptdump
%{_bindir}/ptrepack
%{_bindir}/pt2to3
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{version}-py*.egg-info

# %files doc
# %doc pytablesmanual-%{version}.pdf
# %doc examples/

%changelog
* Sat Aug 16 2014 Dmitrijs Milajevs <dimazest@gmail.com> - 3.1.1-1
- Cleanup and adoptations for Software collections.
- Update to 3.1.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 24 2014 Zbigniew Jędrzejewski-Szmek - 3.0.0-4
- Rebuild for latest blosc

* Fri Jan 10 2014 Zbigniew Jędrzejewski-Szmek - 3.0.0-3
- Move python3 requires to the proper package (#1051691)

* Thu Sep 05 2013 Zbigniew Jędrzejewski-Szmek - 3.0.0-2
- Add python3-tables package

* Wed Aug 21 2013 Thibault North <tnorth@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-3
- Rebuild for hdf5 1.8.11

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Thibault North <tnorth@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Thibault North <tnorth@fedoraproject.org> - 2.3.1-3
- Remove lrucache.py which was deprecated and under AFL license

* Thu Nov 10 2011 Thibault North <tnorth@fedoraproject.org> - 2.3.1-2
- Fixes and subpackage for the docs

* Mon Nov 07 2011 Thibault North <tnorth@fedoraproject.org> - 2.3.1-1
- Fixes and update to 2.3.1
