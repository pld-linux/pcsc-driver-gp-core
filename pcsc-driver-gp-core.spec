Summary:	PC/SC driver for GemPC 410 serial smart card readers
Summary(pl.UTF-8):	Sterownik PC/SC do czytników kart procesorowych GemPC 410 na porcie szeregowym
Name:		pcsc-driver-gp-core
Version:	2.4.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://pcsclite.alioth.debian.org/musclecard.com/drivers/readers/files/gp-core-%{version}.tar.gz
# Source0-md5:	125fccaccb680009b200690abdbb0eba
Patch0:		gp-core-update.patch
URL:		http://pcsclite.alioth.debian.org/musclecard.com/sourcedrivers.html
BuildRequires:	pcsc-lite-devel >= 0.9.3
Requires:	pcsc-lite >= 0.9.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC/SC driver for GemPC 410 serial smart card readers. This version
supports readers with GemCore 1.118 and 1.21.

%description -l pl.UTF-8
Sterowniki PC/SC do czytników kart GemPC 410 podłączanych do portu
szeregowego. Ta wersja obsługuje czytniki z GemCore 1.118 i 1.21.

%prep
%setup -q -n gp-core-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall -I/usr/include/PCSC -I. -DG_UNIX -DHAVE_PTHREAD_H -DIFDHANDLERv2"

%install
rm -rf $RPM_BUILD_ROOT

install -D libgp_core.so $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers/libgp_core.so
install -d $RPM_BUILD_ROOT/etc/reader.conf.d
cat >$RPM_BUILD_ROOT/etc/reader.conf.d/gp-core.conf <<EOF
FRIENDLYNAME	"Gemplus GemPC410 reader"
DEVICENAME	GEMCORE
LIBPATH		%{_libdir}/pcsc/drivers/libgp_core.so
CHANNELID	0x0103F8
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme
%attr(755,root,root) %{_libdir}/pcsc/drivers/libgp_core.so
%config(noreplace) %verify(not md5 mtime size) /etc/reader.conf.d/gp-core.conf
