Name:          jlayer
Summary:       Ogg Vorbis sound engine
Version:       1.0
Release:       %mkrel 1
License:       LGPL
Group:	       Sound
Source0:       %name%version.tar.gz
URL: 	       http://sourceforge.net/projects/javalayer/
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: ant
BuildRequires: java-devel-gcj

%description
JLayer is a JAVA library that decodes, converts and plays MP3 files 
in real-time. JLayer supports MPEG 1/2/2.5 Layer 1/2/3 audio format.

%files 
%defattr(-,root,root)
%{_javadir}/%name-%version.jar
%{_javadir}/%name.jar
%{_javadir}/jl%{version}.jar

#--------------------------------------------------------------------

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/*

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n JLayer%version

%build
#ant all
%{ant} all

%install
install -dm 755 %buildroot%{_javadir}
cp -f jl%{version}.jar %buildroot%{_javadir}/

# jars
install -m644 jl%{version}.jar -D %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r doc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%clean
rm -fr %buildroot
