%define pkgname jquery-rails
Summary:	jQuery and the jQuery-ujs driver for your Rails 3+ application
Name:		ruby-%{pkgname}
Version:	3.1.1
Release:	3
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	2b52aa4c8d361542c0af531007069c57
URL:		http://rubygems.org/gems/jquery-rails
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %(locale -a | grep -q '^en_US$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
Requires:	ruby-rack-ssl >= 1.3.2
Requires:	ruby-railties
Requires:	ruby-thor
Conflicts:	ruby-rack-ssl >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#rack-ssl (~> 1.3.2)

%description
jQuery and the jQuery-ujs driver for your Rails 3+ application.

%description -l pl.UTF-8
Streownik jQuery i jQuery-ujs dla aplikacji Rails w wersji 3+.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

# UTF8 locale needed for doc generation
export LC_ALL=en_US.UTF-8
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri
#rm -r ri/{Class,Date,DateTime}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir}/rails,%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
%{__mv} $RPM_BUILD_ROOT%{ruby_rubylibdir}/{,rails}/generators
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%{ruby_rubylibdir}/jquery
%{ruby_rubylibdir}/jquery-rails.rb
%dir %{ruby_rubylibdir}/rails/generators/jquery
%dir %{ruby_rubylibdir}/rails/generators/jquery/install
%{ruby_rubylibdir}/rails/generators/jquery/install/install_generator.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Jquery
