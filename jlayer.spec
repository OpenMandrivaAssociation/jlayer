Name:		jlayer
Summary:	Ogg Vorbis sound engine
Version:	1.0.1
Release:	%mkrel 2
License:	LGPLv2+
Group:		Development/Java
URL:		http://sourceforge.net/projects/javalayer/
Source0:	http://www.javazoom.net/javalayer/sources/%{name}%{version}.tar.gz
BuildRequires:	ant
BuildRequires:	java-rpmbuild
BuildRequires:	java-devel >= 1.6.0
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
JLayer is a JAVA library that decodes, converts and plays MP3 files
in real-time. JLayer supports MPEG 1/2/2.5 Layer 1/2/3 audio format.

%files
%defattr(-,root,root)
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jl%{version}.jar
%{_javadir}/jl.jar

#--------------------------------------------------------------------

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java

%description javadoc
Javadoc for %{name}.

%files javadoc
%defattr(-,root,root)
%{_javadocdir}/*

#--------------------------------------------------------------------

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

%clean
rm -fr %{buildroot}
