%define check_testcase 0
Name:                activemq
Version:             5.15.15
Release:             2
Summary:             Open source messaging and Integration Patterns server
License:             ASL 2.0
URL:                 http://activemq.apache.org
Source0:             https://github.com/apache/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Requires:            java
BuildRequires:       maven java
BuildArch:           noarch
%description
The most popular and powerful open source messaging and Integration Patterns
server.

%package javadoc
Summary:             Javadoc for %{name}
%description javadoc
This package contains javadoc for %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
%if %{check_testcase}
	mvn package
%else
	mvn package -Dmaven.test.skip=True
%endif

%install
install -d -m755 %{buildroot}/%{_datadir}/javadoc
install -d -m755 %{buildroot}/%{_datadir}/licenses
install -d -m755 %{buildroot}/%{_datadir}/activemq
cd assembly/target
unzip -d ./file apache-activemq*.zip
cd ./file/apache-activemq*
rm -rf bin/win* bin/*.bat
chmod 755 bin/%{name}
for dir in bin examples webapps webapps-demo conf lib docs;do
	if [ "$dir" = "docs" || "$dir" = "examples" ]
	then 
		cp -arf $dir %{buildroot}/%{_datadir}/javadoc
	else
		cp -arf $dir %{buildroot}/%{_datadir}/activemq

	fi
done
cp README.txt  %{buildroot}/%{_datadir}/activemq
cp LICENSE %{buildroot}/%{_datadir}/licenses
cp NOTICE %{buildroot}/%{_datadir}/licenses
rm -rf ../../file
cd %{_builddir}

%files
%{_datadir}/activemq
%license %{_datadir}/licenses/*

%files javadoc
%{_datadir}/javadoc

%changelog
* Sat Aug 28 2021 lingsheng <lingsheng@huawei.com> - 5.15.15-2
- Fix activemq permission and remove windows related files

* Mon Jul 19 2021 xuping <xuping33@huawei.com> - 5.15.15-1
- package init
