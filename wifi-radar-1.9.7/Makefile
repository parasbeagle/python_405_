#
# $Id: Makefile 47 2006-03-27 23:09:45Z finley $
#  vi:set filetype=make:
#

SHELL = /bin/sh

#
# These settings are what I would expect for most modern Linux distros, 
# and are what work for me unmodified on Ubuntu. -BEF-
# 
sbindir 	= /usr/sbin
initdir 	= /etc/init.d
sysconfdir 	= /etc/wifi-radar
mandir 		= /usr/share/man
pixmapsdir 	= /usr/share/pixmaps
appsdir 	= /usr/share/applications

srcdir = .
top_srcdir = .
top_builddir = .

VERSION = $(shell cat VERSION)

TOPDIR := $(CURDIR)


.PHONY: all
all:	wifi-radar.localized

.PHONY: install
install:	all
	test -d ${sysconfdir} || install -d -m 755 ${sysconfdir}
	test -e ${sysconfdir}/wifi-radar.conf || install -m 644 wifi-radar.conf	${sysconfdir}
	
	test -d ${sbindir} || install -d -m 755 ${sbindir}
	install -m 755 wifi-radar.localized	${sbindir}/wifi-radar
	
	test -d ${mandir}/man1 || install -d -m 755 ${mandir}/man1
	install -m 644 wifi-radar.1 		${mandir}/man1
	
	test -d ${mandir}/man5 || install -d -m 755 ${mandir}/man5
	install -m 644 wifi-radar.conf.5 	${mandir}/man5
	
	test -d ${initdir} || install -d -m 755 ${initdir}
	install -m 755 init_script 			${initdir}/wifi-radar
	
	test -d ${pixmapsdir} || install -d -m 755 ${pixmapsdir}
	install -m 644 pixmaps/wifi-radar.svg	${pixmapsdir}
	install -m 644 pixmaps/wifi-radar.png	${pixmapsdir}
	
	test -d ${appsdir} || install -d -m 755 ${appsdir}
	install -m 644 wifi-radar.desktop	${appsdir}
	

wifi-radar.localized:	wifi-radar
	cp wifi-radar wifi-radar.tmp
	perl -pi -e 's#^WIFI_RADAR_VERSION\s+=.*#WIFI_RADAR_VERSION = "${VERSION}"#' wifi-radar.tmp
	perl -pi -e 's#^CONF_FILE\s+=.*#CONF_FILE = "${sysconfdir}/wifi-radar.conf"#' wifi-radar.tmp
	mv wifi-radar.tmp wifi-radar.localized

.PHONY: tarball
tarball: $(TOPDIR)/tmp/wifi-radar-$(VERSION).tar.bz2.sign
$(TOPDIR)/tmp/wifi-radar-$(VERSION).tar.bz2.sign: $(TOPDIR)/tmp/wifi-radar-$(VERSION).tar.bz2
	cd $(TOPDIR)/tmp && gpg --detach-sign -a --output wifi-radar-$(VERSION).tar.bz2.sign wifi-radar-$(VERSION).tar.bz2
	cd $(TOPDIR)/tmp && gpg --verify wifi-radar-$(VERSION).tar.bz2.sign

$(TOPDIR)/tmp/wifi-radar-$(VERSION).tar.bz2:
	rm -fr $(TOPDIR)/tmp
	mkdir -p $(TOPDIR)/tmp/
	svn export . $(TOPDIR)/tmp/wifi-radar-$(VERSION)
	find $(TOPDIR)/tmp/wifi-radar-$(VERSION) -type f -exec chmod ug+r  {} \;
	find $(TOPDIR)/tmp/wifi-radar-$(VERSION) -type d -exec chmod ug+rx {} \;
	chmod 755 $(TOPDIR)/tmp/wifi-radar-$(VERSION)/wifi-radar
	cd $(TOPDIR)/tmp && tar -ch wifi-radar-$(VERSION) | bzip2 > wifi-radar-$(VERSION).tar.bz2
	ls -l $(TOPDIR)/tmp/



.PHONY: clean
clean:
	rm -f  wifi-radar.localized
	rm -fr tmp/

.PHONY: distclean
distclean: clean

