Name:		jlayer
Summary:	Ogg Vorbis sound engine
Version:	1.0.1
Release:	4
License:	LGPLv2+
Group:		Development/Java
URL:		http://sourceforge.net/projects/javalayer/
Source0:	http://www.javazoom.net/javalayer/sources/%{name}%{version}.tar.gz
BuildRequires:	ant
BuildRequires:	java-rpmbuild
BuildRequires:	java-devel >= 1.6.0
BuildArch:	noarch

%description
JLayer is a JAVA library that decodes, converts and plays MP3 files
in real-time. JLayer supports MPEG 1/2/2.5 Layer 1/2/3 audio format.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n JLayer%{version}

%build
%{ant} all

%install
install -dm 755 %{buildroot}%{_javadir}
install -m644 jl%{version}.jar %{buildroot}%{_javadir}/
ln -s jl%{version}.jar %{buildroot}%{_javadir}/jl.jar

# jars
ln -s jl%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s jl%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r doc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jl%{version}.jar
%{_javadir}/jl.jar

%files javadoc
%{_javadocdir}/*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2011.0
+ Revision: 612450
- the mass rebuild of 2010.1 packages

* Sat Feb 20 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 508802
- update to new version 1.0.1
- spec file clean

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 429634
- rebuild
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Anssi Hannula <anssi@mandriva.org> 1.0-2mdv2009.0
+ Revision: 209248
- buildrequires java-rpmbuild
- replace duplicate files with symlinks
- provide jl.jar symlink

* Sun Dec 16 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0-1mdv2008.1
+ Revision: 120781
- import jlayer


