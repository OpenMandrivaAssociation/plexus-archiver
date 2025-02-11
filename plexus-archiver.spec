%{?_javapackages_macros:%_javapackages_macros}
Name:           plexus-archiver
Version:        2.4.4
Release:        4.3
Epoch:          0
Summary:        Plexus Archiver Component
License:        ASL 2.0
URL:            https://plexus.codehaus.org/plexus-components/plexus-archiver/
Source0:        https://github.com/sonatype/%{name}/archive/%{name}-%{version}.tar.gz

# PLXCOMP-64 and PLXCOMP-113: Add support for extracting zip and tar symbolic links
# Forwarded upstream: https://github.com/sonatype/plexus-archiver/pull/14
Patch0:         0001-Fix-PLXCOMP-113-and-PLXCOMP-64.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-io
BuildRequires:  plexus-utils
BuildRequires:  apache-commons-compress


%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.


%prep
# funny chars in the archive which upset bsdtar
export LC_ALL=en_US.UTF-8
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%mvn_file :%{name} plexus/archiver

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Sep  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.4-4
- Add patch for extracting symbolic links

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.4.4-2
- Use Requires: java-headless rebuild (#1067528)

* Tue Dec  3 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.4-1
- Update to upstream version 2.4.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.4.2-2
- Update to latest packaging guidelines
- Remove MIT license (only applies to test cases not binary rpm)

* Fri May 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.2-1
- Update to upstream version 2.4.2
- Remove patch for CVE-2012-2098 (accepted upstream)

* Thu Apr 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.3-1
- Update to upstream version 2.3
- Use apache-commons-compress for bzip2 (de)compression
- Resolves: CVE-2012-2098

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:2.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.2-4
- Add ASL 2.0 license text to packages

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 0:2.2-3
- Migration to plexus-containers-container-default

* Mon Nov 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.2-2
- Fix source URL to be stable

* Wed Oct 10 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.2-1
- Update to upstream 2.2.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.1.1-1
- Update to latest upstream release.

* Wed Feb 15 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.1-1
- Update to latest upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 8 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.0.1-2
- BR maven-surefire-provider-junit4.

* Thu Sep 8 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.0.1-1
- Update to 2.0.1 version.

* Wed Jul 27 2011 Jaromir Capik <jcapik@redhat.com> - 0:1.2-2
- Removal of plexus-maven-plugin dependency (not needed)
- Minor spec file changes according to the latest guidelines

* Tue May 17 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-1
- Update to 1.2.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 6 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.1-1
- Update to 1.1.

* Mon Dec 28 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a12.4
- Install depmap and pom to override common poms.

* Thu Dec 24 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a12.3
- Really ignore test failures.

* Thu Dec 24 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a12.2
- Ignore test failures.

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a12.1
- Update to alpha 12.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.4.a7.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.3.a7.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0-0.2.a7.1.2
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.0-0.2.a7.1jpp.1
- Autorebuild for GCC 4.3

* Fri Jan 04 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.1.a7.1jpp.1
- Update to alpha 7

* Thu Feb 15 2007 Matt Wrigne <mwringe@redhat.com> - 0:1.0-0.1.a6.1jpp.1
- Fix rpmlint issues
- Version package to new jpp versioning standards
- Remove javadoc post and postun sections

* Mon Jun 19 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.a6.1jpp
- Upgrade to 1.0-alpha-6

* Wed May 31 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a3.2jpp
- First JPP-1.7 release

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a3.1jpp
- First JPackage build
