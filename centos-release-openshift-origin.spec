Summary:   Common release file to establish shared metadata for CentOS PaaS SIG
Name:      centos-release-openshift-origin
Version:   1
Release:   1%{?dist}
License:   GPLv2
Source0:   CentOS-OpenShift-Origin.repo
Source1:   LICENSE
URL:       https://wiki.centos.org/SpecialInterestGroup/PaaS/OpenShift
Provides:  centos-release-openshift-origin = %{version}-%{release}
# This provides the public key
Requires:  centos-release-paas-common
BuildArch: noarch

%description
yum configuration for OpenShift Origin packages as delivered via the 
CentOS PaaS SIG.

%prep
%setup -q -n %{name} -T -c

%install
install -D -m 644 %SOURCE0 %{buildroot}%{_sysconfdir}/yum.repos.d/
install -m 644 %SOURCE1 .

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-OpenShift-Origin.repo

%changelog
* Fri May 20 2016 Troy Dawson <tdawson@redha.com> - 1-1
- Initial version based on centos-release-gluster37
