%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup}

%global module	tables	

Summary:	Hierarchical datasets in Python
Name:		python-%{module}
Version:	2.3.1
Release:	3%{?dist}
Source0:	http://sourceforge.net/projects/pytables/files/pytables/%{version}/%{module}-%{version}.tar.gz

License:	BSD
Group:		Development/Languages
URL:		http://www.pytables.org
Requires:	numpy >= 1.4.1
Requires:	python-numexpr >= 1.4.1

BuildRequires:	hdf5-devel >= 1.6.10 bzip2-devel lzo-devel
BuildRequires:	Cython >= 0.13 numpy >= 1.4.1 python-numexpr >= 1.4.1
BuildRequires:	python2-devel


%description
PyTables is a package for managing hierarchical datasets and designed 
to efficiently and easily cope with extremely large amounts of data.

%package	doc
Group:		Development/Languages
Summary:	Documentation for PyTables
BuildArch:	noarch

%description doc
The %{name}-doc package contains the documentation related to 
PyTables.

%prep 
%setup -q -n %{module}-%{version}

rm LICENSES/LRUCACHE.txt
rm tables/misc/lrucache.py

%build
python setup.py build

%check
libdir=`ls build/|grep lib`
export PYTHONPATH=`pwd`/build/$libdir
echo "import tables; tables.test()" > bench/check_all.py
python bench/check_all.py

%install
rm -rf %{buildroot}
chmod -x examples/check_examples.sh
for i in utils/*; do sed -i 's|bin/env |bin/|' $i; done

python setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc *.txt LICENSES
%{_bindir}/nctoh5
%{_bindir}/ptdump
%{_bindir}/ptrepack
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}-py*.egg-info

%files doc
%doc doc/*.pdf
%doc examples/

%changelog
* Mon Nov 14 2011 Thibault North <tnorth@fedoraproject.org> - 2.3.1-3
- Remove lrucache.py which was deprecated and under AFL license

* Thu Nov 07 2011 Thibault North <tnorth@fedoraproject.org> - 2.3.1-2
- Fixes and subpackage for the docs

* Mon Nov 07 2011 Thibault North <tnorth@fedoraproject.org> - 2.3.1-1
- Fixes and update to 2.3.1


