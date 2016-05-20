centos-release-openshift-origin provides the YUM repository file for 
packages of the CentOS PaaS SIG that are used with OpenShift Origin.

This package needs to get build against the following targets so that the
packages land at the right tag for inclusion in CentOS Extras:

 - core7-extras-common-el7.centos (tag: core7-extras-common-candidate)

Building the package can be done like this:


    $ rpmbuild -bs \
               --define "_sourcedir $PWD" --define "_srcrpmdir $PWD" \
               --define "dist .el7.centos" \
               centos-release-openshift-origin.spec

    $ cbs build core7-extras-common-el7.centos \
          centos-release-openshift-origin-1-2.el7.centos.src.rpm

