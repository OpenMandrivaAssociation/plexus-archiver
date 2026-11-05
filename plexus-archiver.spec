Name:		plexus-archiver
Version:	4.4.0
Release:	1
Summary:	Plexus archiver component
Group:		Development/Java
License:	ASL 2.0
URL:		https://codehaus-plexus.github.io/plexus-archiver/
Source0:	https://github.com/codehaus-plexus/plexus-archiver/archive/refs/tags/plexus-archiver-%{version}.tar.gz
BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	plexus-pom
BuildRequires:	plexus-utils
BuildRequires:	plexus-io
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(org.apache.commons:commons-compress)
BuildRequires:	mvn(org.slf4j:slf4j-api)
BuildRequires:	mvn(org.iq80.snappy:snappy)
BuildRequires:	mvn(org.tukaani:xz)
BuildRequires:	mvn(javax.inject:javax.inject)
# provided scope: sources import javax.annotation
BuildRequires:	mvn(com.google.code.findbugs:jsr305)
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

%description
Creates and extracts zip, tar, jar, and related archives. 4.4.0 is the
last release before the native zstd-jni dependency. Snappy support is a
direct import of org.iq80.snappy, not a reflection lookup.

%prep
%autosetup -n plexus-archiver-plexus-archiver-%{version}

%files -f .mfiles
%doc LICENSE README.md ReleaseNotes.md
