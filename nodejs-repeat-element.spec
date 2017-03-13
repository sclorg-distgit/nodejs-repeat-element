%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name repeat-element

Summary:       Create an array by repeating the given value n times
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.1.2
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/repeat-element
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Create an array by repeating the given value n times.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-3
- Rebuilt with updated metapackage

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.1.2-2
- Enable scl macros, fix license macro for el6

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.1.2-1
- Initial package
