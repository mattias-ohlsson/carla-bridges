Name:           carla-bridges
Version:        2.4.1
Release:        1%{?dist}
Summary:        Carla bridges

# For a breakdown of the licensing, see the Carla package
License:        GPLv2+ and BSD and Boost and ISC and MIT and zlib

URL:            https://kx.studio/Applications:Carla
Source0:        https://github.com/falkTX/Carla/archive/v%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  make
BuildRequires:  binutils
BuildRequires:  pkg-config

# posix32
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel(x86-32)
BuildRequires:  libstdc++-devel(x86-32)

# win32
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-winpthreads-static

# win64
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-winpthreads-static

# wine32 and wine64
BuildRequires:  wine-devel

%description
This package provides the Carla bridges.

%package -n carla-bridge-posix32
Summary:        Carla posix32 bridge
Requires:       Carla

%description -n carla-bridge-posix32
This package provides the Carla posix32 bridge.

%package -n lv2-carla-bridge-posix32
Summary:        Carla LV2 posix32 bridge
Requires:       carla-bridge-posix32
Requires:       lv2-carla

%description -n lv2-carla-bridge-posix32
This package provides the Carla LV2 posix32 bridge.

%package -n carla-bridge-win32
Summary:        Carla win32 bridge
Requires:       Carla
Requires:       wine

%description -n carla-bridge-win32
This package provides the Carla win32 bridge.

%package -n lv2-carla-bridge-win32
Summary:        Carla LV2 win32 bridge
Requires:       carla-bridge-win32
Requires:       lv2-carla

%description -n lv2-carla-bridge-win32
This package provides the Carla LV2 win32 bridge.

%package -n carla-bridge-win64
Summary:        Carla win64 bridge
Requires:       Carla
Requires:       wine

%description -n carla-bridge-win64
This package provides the Carla win64 bridge.

%package -n lv2-carla-bridge-win64
Summary:        Carla LV2 win64 bridge
Requires:       carla-bridge-win64
Requires:       lv2-carla

%description -n lv2-carla-bridge-win64
This package provides the Carla LV2 win64 bridge.

%prep
%autosetup -n Carla-%{version}

%build
%make_build posix32 DEBUG=true
%make_build win32 CC=i686-w64-mingw32-gcc CXX=i686-w64-mingw32-g++ DEBUG=true
%make_build win64 CC=x86_64-w64-mingw32-gcc CXX=x86_64-w64-mingw32-g++ DEBUG=true
%make_build wine32 DEBUG=true
%make_build wine64 DEBUG=true

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}%{_libdir}/carla
%__cp -p bin/carla-bridge-posix32 \
 bin/carla-bridge-win32.exe \
 bin/carla-bridge-win64.exe \
 bin/carla-discovery-posix32 \
 bin/carla-discovery-win32.exe \
 bin/carla-discovery-win64.exe \
 bin/jackbridge-wine32.dll \
 bin/jackbridge-wine64.dll \
 %{buildroot}%{_libdir}/carla/

install -d -m 755 %{buildroot}%{_libdir}/lv2/carla.lv2
ln -s %{_libdir}/carla/carla-bridge-posix32 %{buildroot}%{_libdir}/lv2/carla.lv2/
ln -s %{_libdir}/carla/carla-discovery-posix32 %{buildroot}%{_libdir}/lv2/carla.lv2/
ln -s %{_libdir}/carla/carla-bridge-win32.exe %{buildroot}%{_libdir}/lv2/carla.lv2/
ln -s %{_libdir}/carla/carla-discovery-win32.exe %{buildroot}%{_libdir}/lv2/carla.lv2/
ln -s %{_libdir}/carla/jackbridge-wine32.dll %{buildroot}%{_libdir}/lv2/carla.lv2/
ln -s %{_libdir}/carla/carla-bridge-win64.exe %{buildroot}%{_libdir}/lv2/carla.lv2/
ln -s %{_libdir}/carla/carla-discovery-win64.exe %{buildroot}%{_libdir}/lv2/carla.lv2/
ln -s %{_libdir}/carla/jackbridge-wine64.dll %{buildroot}%{_libdir}/lv2/carla.lv2/

%files -n carla-bridge-posix32
%doc README.md
%license doc/GPL.txt
%{_libdir}/carla/carla-bridge-posix32
%{_libdir}/carla/carla-discovery-posix32

%files -n lv2-carla-bridge-posix32
%{_libdir}/lv2/carla.lv2/carla-bridge-posix32
%{_libdir}/lv2/carla.lv2/carla-discovery-posix32

%files -n carla-bridge-win32
%doc README.md
%license doc/GPL.txt
%{_libdir}/carla/carla-bridge-win32.exe
%{_libdir}/carla/carla-discovery-win32.exe
%{_libdir}/carla/jackbridge-wine32.dll

%files -n lv2-carla-bridge-win32
%{_libdir}/lv2/carla.lv2/carla-bridge-win32.exe
%{_libdir}/lv2/carla.lv2/carla-discovery-win32.exe
%{_libdir}/lv2/carla.lv2/jackbridge-wine32.dll

%files -n carla-bridge-win64
%doc README.md
%license doc/GPL.txt
%{_libdir}/carla/carla-bridge-win64.exe
%{_libdir}/carla/carla-discovery-win64.exe
%{_libdir}/carla/jackbridge-wine64.dll

%files -n lv2-carla-bridge-win64
%{_libdir}/lv2/carla.lv2/carla-bridge-win64.exe
%{_libdir}/lv2/carla.lv2/carla-discovery-win64.exe
%{_libdir}/lv2/carla.lv2/jackbridge-wine64.dll

%changelog
* Sun Jan 09 2022 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.4.1-1
- Update to 2.4.1

* Fri Apr 16 2021 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.3.0-1
- Update to 2.3.0

* Fri Oct 23 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.2.0-1
- Update to 2.2.0

* Tue Jun 16 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.1.1-1
- Update to 2.1.1

* Wed Jun 10 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.1-1
- Initial build
