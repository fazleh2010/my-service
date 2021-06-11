%define __jar_repack 0
Name: my-service
Version: 1.0
Release: 1
Summary: my-service
License: (c) null
Group: Applications/System
autoprov: yes
autoreq: yes
BuildArch: noarch
BuildRoot: /home/elahi/a-teanga/my-service/target/rpm/my-service/buildroot

%description

%install
if [ -d $RPM_BUILD_ROOT ];
then
  mv /home/elahi/a-teanga/my-service/target/rpm/my-service/tmp-buildroot/* $RPM_BUILD_ROOT
else
  mv /home/elahi/a-teanga/my-service/target/rpm/my-service/tmp-buildroot $RPM_BUILD_ROOT
fi

%files

 "/usr/share/my-service/"
%dir %attr(700,sne,sne) "/var/lib/my-service/"
%dir %attr(700,sne,sne) "/var/log/my-service/"
%attr(755,-,-)  "/usr/bin/my-service"
%attr(755,-,-)  "/etc/init.d/my-service"
%config   "/etc/default/my-service"
%config   "/etc/clarind/my-service.yaml"

%pre
/usr/bin/getent group sne > /dev/null || /usr/sbin/groupadd sne
                            /usr/bin/getent passwd sne > /dev/null || /usr/sbin/useradd -r -d /var/lib/my-service -m -g sne sne

%post
chkconfig --add my-service;
                            if [ $1 -eq 0 ]; then
                            /sbin/service my-service start
                            elif [ $1 -ge 1 ]; then
                            /sbin/service my-service restart
                            fi

%preun
if [ $1 -eq 0 ] ; then
                            /sbin/service my-service stop;chkconfig --del my-service
                            fi
