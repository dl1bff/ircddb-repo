#
#
# ircddb-repo
#   installs the ircDDB repo file and gpg key
#
# Copyright (C) 2017   Michael Dirska, DL1BFF (dl1bff@mdx.de)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#



Name: ircddb-repo
Version: 1.0
Release: 2
License: GPLv2
Group: Networking/Daemons
Summary: ircDDB repository file and GPG key
URL: http://ircddb.net
Packager: Michael Dirska DL1BFF <dl1bff@mdx.de>
Source0: ircddb-repo.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

%description
This RPM contains the ircDDB repo file and the gpg key


%prep
%setup -n ircddb-repo



%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/yum.repos.d/
cp %{name}.repo %{buildroot}/etc/yum.repos.d/
mkdir -p %{buildroot}/etc/pki/rpm-gpg/
cp RPM-GPG-KEY-%{name} %{buildroot}/etc/pki/rpm-gpg/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
/etc/yum.repos.d/%{name}.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-%{name}
%doc README.md LICENSE


