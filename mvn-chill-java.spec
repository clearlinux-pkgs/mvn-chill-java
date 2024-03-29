#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-chill-java
Version  : 0.9.3
Release  : 4
URL      : https://github.com/twitter/chill/archive/v0.9.3.tar.gz
Source0  : https://github.com/twitter/chill/archive/v0.9.3.tar.gz
Source1  : https://repo.maven.apache.org/maven2/com/twitter/chill_2.11/0.7.6/chill_2.11-0.7.6.jar
Source2  : https://repo.maven.apache.org/maven2/com/twitter/chill_2.11/0.7.6/chill_2.11-0.7.6.pom
Source3  : https://repo.maven.apache.org/maven2/com/twitter/chill_2.12/0.9.3/chill_2.12-0.9.3.jar
Source4  : https://repo.maven.apache.org/maven2/com/twitter/chill_2.12/0.9.3/chill_2.12-0.9.3.pom
Source5  : https://repo1.maven.org/maven2/com/twitter/chill-java/0.7.6/chill-java-0.7.6.jar
Source6  : https://repo1.maven.org/maven2/com/twitter/chill-java/0.7.6/chill-java-0.7.6.pom
Source7  : https://repo1.maven.org/maven2/com/twitter/chill-java/0.9.3/chill-java-0.9.3.jar
Source8  : https://repo1.maven.org/maven2/com/twitter/chill-java/0.9.3/chill-java-0.9.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-chill-java-data = %{version}-%{release}
Requires: mvn-chill-java-license = %{version}-%{release}

%description
## Chill
[![Build Status](https://secure.travis-ci.org/twitter/chill.png)](http://travis-ci.org/twitter/chill)
[![Codecov branch](https://img.shields.io/codecov/c/github/twitter/chill/develop.svg?maxAge=3600)](https://codecov.io/github/twitter/chill)
[![Latest version](https://index.scala-lang.org/twitter/chill/chill/latest.svg?color=orange)](https://index.scala-lang.org/twitter/chill/chill)
[![Chat](https://badges.gitter.im/twitter/chill.svg)](https://gitter.im/twitter/chill?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package data
Summary: data components for the mvn-chill-java package.
Group: Data

%description data
data components for the mvn-chill-java package.


%package license
Summary: license components for the mvn-chill-java package.
Group: Default

%description license
license components for the mvn-chill-java package.


%prep
%setup -q -n chill-0.9.3

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-chill-java
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-chill-java/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-chill-java/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill_2.11/0.7.6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill_2.11/0.7.6/chill_2.11-0.7.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill_2.11/0.7.6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill_2.11/0.7.6/chill_2.11-0.7.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill_2.12/0.9.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill_2.12/0.9.3/chill_2.12-0.9.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill_2.12/0.9.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill_2.12/0.9.3/chill_2.12-0.9.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill-java/0.7.6
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill-java/0.7.6/chill-java-0.7.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill-java/0.7.6
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill-java/0.7.6/chill-java-0.7.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill-java/0.9.3
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill-java/0.9.3/chill-java-0.9.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill-java/0.9.3
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/twitter/chill-java/0.9.3/chill-java-0.9.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/twitter/chill-java/0.7.6/chill-java-0.7.6.jar
/usr/share/java/.m2/repository/com/twitter/chill-java/0.7.6/chill-java-0.7.6.pom
/usr/share/java/.m2/repository/com/twitter/chill-java/0.9.3/chill-java-0.9.3.jar
/usr/share/java/.m2/repository/com/twitter/chill-java/0.9.3/chill-java-0.9.3.pom
/usr/share/java/.m2/repository/com/twitter/chill_2.11/0.7.6/chill_2.11-0.7.6.jar
/usr/share/java/.m2/repository/com/twitter/chill_2.11/0.7.6/chill_2.11-0.7.6.pom
/usr/share/java/.m2/repository/com/twitter/chill_2.12/0.9.3/chill_2.12-0.9.3.jar
/usr/share/java/.m2/repository/com/twitter/chill_2.12/0.9.3/chill_2.12-0.9.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-chill-java/LICENSE
/usr/share/package-licenses/mvn-chill-java/NOTICE
