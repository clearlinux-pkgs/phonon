#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : phonon
Version  : 4.12.0
Release  : 14
URL      : https://download.kde.org/stable/phonon/4.12.0/phonon-4.12.0.tar.xz
Source0  : https://download.kde.org/stable/phonon/4.12.0/phonon-4.12.0.tar.xz
Source1  : https://download.kde.org/stable/phonon/4.12.0/phonon-4.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: phonon-bin = %{version}-%{release}
Requires: phonon-data = %{version}-%{release}
Requires: phonon-lib = %{version}-%{release}
Requires: phonon-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : extra-cmake-modules-data
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : qt6base-dev
BuildRequires : qtdeclarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the phonon package.
Group: Binaries
Requires: phonon-data = %{version}-%{release}
Requires: phonon-license = %{version}-%{release}

%description bin
bin components for the phonon package.


%package data
Summary: data components for the phonon package.
Group: Data

%description data
data components for the phonon package.


%package dev
Summary: dev components for the phonon package.
Group: Development
Requires: phonon-lib = %{version}-%{release}
Requires: phonon-bin = %{version}-%{release}
Requires: phonon-data = %{version}-%{release}
Provides: phonon-devel = %{version}-%{release}
Requires: phonon = %{version}-%{release}

%description dev
dev components for the phonon package.


%package lib
Summary: lib components for the phonon package.
Group: Libraries
Requires: phonon-data = %{version}-%{release}
Requires: phonon-license = %{version}-%{release}

%description lib
lib components for the phonon package.


%package license
Summary: license components for the phonon package.
Group: Default

%description license
license components for the phonon package.


%prep
%setup -q -n phonon-4.12.0
cd %{_builddir}/phonon-4.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710364583
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DPHONON_BUILD_QT5=OFF
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710364583
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/phonon
cp %{_builddir}/phonon-%{version}/COPYING %{buildroot}/usr/share/package-licenses/phonon/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/phonon-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/phonon/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/phonon-%{version}/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/phonon/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/phononsettings

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ar/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/az/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/az/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/be/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/be/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/bg/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/bg/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/bn/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/bs/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/bs/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ca/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ca/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/cs/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/csb/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/csb/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/da/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/da/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/de/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/de/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/el/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/el/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/eo/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/eo/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/es/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/es/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/et/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/et/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/eu/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/fa/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/fa/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/fi/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/fr/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/fy/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ga/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ga/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/gl/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/gu/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/gu/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/he/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/he/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/hi/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/hi/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/hne/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/hne/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/hr/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/hr/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/hu/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/hu/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ia/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ia/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/id/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/id/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/is/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/is/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/it/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/it/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ja/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ja/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ka/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ka/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/kk/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/kk/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/km/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/km/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/kn/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ko/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ku/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ku/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/lt/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/lt/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/lv/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/lv/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/mai/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/mai/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/mk/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/mk/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ml/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ml/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/mr/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/mr/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ms/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/nb/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/nb/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/nds/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/nds/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ne/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ne/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/nl/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/nn/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/oc/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/oc/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/or/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/pa/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/pa/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/pl/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/pt/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ro/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ro/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ru/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ru/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/se/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/se/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/si/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sk/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sl/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sl/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sq/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sq/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sr/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sr/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sv/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ta/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ta/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/te/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/tg/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/th/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/th/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/tr/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/tr/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ug/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ug/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/uk/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/vi/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/vi/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/wa/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/wa/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/phononsettings_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/phonon4qt6/phonon/AbstractAudioOutput
/usr/include/phonon4qt6/phonon/AbstractMediaStream
/usr/include/phonon4qt6/phonon/AbstractVideoOutput
/usr/include/phonon4qt6/phonon/AddonInterface
/usr/include/phonon4qt6/phonon/AudioCaptureDevice
/usr/include/phonon4qt6/phonon/AudioCaptureDeviceModel
/usr/include/phonon4qt6/phonon/AudioChannelDescription
/usr/include/phonon4qt6/phonon/AudioChannelDescriptionModel
/usr/include/phonon4qt6/phonon/AudioDataOutput
/usr/include/phonon4qt6/phonon/AudioOutput
/usr/include/phonon4qt6/phonon/AudioOutputDevice
/usr/include/phonon4qt6/phonon/AudioOutputDeviceModel
/usr/include/phonon4qt6/phonon/AudioOutputInterface
/usr/include/phonon4qt6/phonon/AudioOutputInterface40
/usr/include/phonon4qt6/phonon/AudioOutputInterface42
/usr/include/phonon4qt6/phonon/AvCapture
/usr/include/phonon4qt6/phonon/BackendCapabilities
/usr/include/phonon4qt6/phonon/BackendInterface
/usr/include/phonon4qt6/phonon/Effect
/usr/include/phonon4qt6/phonon/EffectDescription
/usr/include/phonon4qt6/phonon/EffectDescriptionModel
/usr/include/phonon4qt6/phonon/EffectInterface
/usr/include/phonon4qt6/phonon/EffectParameter
/usr/include/phonon4qt6/phonon/EffectWidget
/usr/include/phonon4qt6/phonon/Global
/usr/include/phonon4qt6/phonon/GlobalDescriptionContainer
/usr/include/phonon4qt6/phonon/MediaController
/usr/include/phonon4qt6/phonon/MediaNode
/usr/include/phonon4qt6/phonon/MediaObject
/usr/include/phonon4qt6/phonon/MediaObjectInterface
/usr/include/phonon4qt6/phonon/MediaSource
/usr/include/phonon4qt6/phonon/Mrl
/usr/include/phonon4qt6/phonon/ObjectDescription
/usr/include/phonon4qt6/phonon/ObjectDescriptionData
/usr/include/phonon4qt6/phonon/ObjectDescriptionModel
/usr/include/phonon4qt6/phonon/ObjectDescriptionModelData
/usr/include/phonon4qt6/phonon/Path
/usr/include/phonon4qt6/phonon/PlatformPlugin
/usr/include/phonon4qt6/phonon/SeekSlider
/usr/include/phonon4qt6/phonon/StreamInterface
/usr/include/phonon4qt6/phonon/SubtitleDescription
/usr/include/phonon4qt6/phonon/SubtitleDescriptionModel
/usr/include/phonon4qt6/phonon/VideoCaptureDevice
/usr/include/phonon4qt6/phonon/VideoCaptureDeviceModel
/usr/include/phonon4qt6/phonon/VideoPlayer
/usr/include/phonon4qt6/phonon/VideoWidget
/usr/include/phonon4qt6/phonon/VideoWidgetInterface
/usr/include/phonon4qt6/phonon/VideoWidgetInterface44
/usr/include/phonon4qt6/phonon/VideoWidgetInterfaceLatest
/usr/include/phonon4qt6/phonon/VolumeFaderEffect
/usr/include/phonon4qt6/phonon/VolumeFaderInterface
/usr/include/phonon4qt6/phonon/VolumeSlider
/usr/include/phonon4qt6/phonon/abstractaudiooutput.h
/usr/include/phonon4qt6/phonon/abstractmediastream.h
/usr/include/phonon4qt6/phonon/abstractvideooutput.h
/usr/include/phonon4qt6/phonon/addoninterface.h
/usr/include/phonon4qt6/phonon/audiodataoutput.h
/usr/include/phonon4qt6/phonon/audiodataoutputinterface.h
/usr/include/phonon4qt6/phonon/audiooutput.h
/usr/include/phonon4qt6/phonon/audiooutputinterface.h
/usr/include/phonon4qt6/phonon/backendcapabilities.h
/usr/include/phonon4qt6/phonon/backendinterface.h
/usr/include/phonon4qt6/phonon/effect.h
/usr/include/phonon4qt6/phonon/effectinterface.h
/usr/include/phonon4qt6/phonon/effectparameter.h
/usr/include/phonon4qt6/phonon/effectwidget.h
/usr/include/phonon4qt6/phonon/experimental/abstractaudiodataoutput.h
/usr/include/phonon4qt6/phonon/experimental/abstractvideodataoutput.h
/usr/include/phonon4qt6/phonon/experimental/audiodataoutput.h
/usr/include/phonon4qt6/phonon/experimental/audiodataoutputinterface.h
/usr/include/phonon4qt6/phonon/experimental/audioformat.h
/usr/include/phonon4qt6/phonon/experimental/avcapture.h
/usr/include/phonon4qt6/phonon/experimental/avcaptureinterface.h
/usr/include/phonon4qt6/phonon/experimental/backendcapabilities.h
/usr/include/phonon4qt6/phonon/experimental/backendinterface.h
/usr/include/phonon4qt6/phonon/experimental/export.h
/usr/include/phonon4qt6/phonon/experimental/globalconfig.h
/usr/include/phonon4qt6/phonon/experimental/mediasource.h
/usr/include/phonon4qt6/phonon/experimental/objectdescription.h
/usr/include/phonon4qt6/phonon/experimental/packet.h
/usr/include/phonon4qt6/phonon/experimental/packetpool.h
/usr/include/phonon4qt6/phonon/experimental/phononnamespace.h
/usr/include/phonon4qt6/phonon/experimental/snapshotinterface.h
/usr/include/phonon4qt6/phonon/experimental/videodataoutput.h
/usr/include/phonon4qt6/phonon/experimental/videodataoutput2.h
/usr/include/phonon4qt6/phonon/experimental/videodataoutputinterface.h
/usr/include/phonon4qt6/phonon/experimental/videoframe.h
/usr/include/phonon4qt6/phonon/experimental/videoframe2.h
/usr/include/phonon4qt6/phonon/experimental/videowidget.h
/usr/include/phonon4qt6/phonon/experimental/visualization.h
/usr/include/phonon4qt6/phonon/globalconfig.h
/usr/include/phonon4qt6/phonon/globaldescriptioncontainer.h
/usr/include/phonon4qt6/phonon/mediacontroller.h
/usr/include/phonon4qt6/phonon/medianode.h
/usr/include/phonon4qt6/phonon/mediaobject.h
/usr/include/phonon4qt6/phonon/mediaobjectinterface.h
/usr/include/phonon4qt6/phonon/mediasource.h
/usr/include/phonon4qt6/phonon/mrl.h
/usr/include/phonon4qt6/phonon/objectdescription.h
/usr/include/phonon4qt6/phonon/objectdescriptionmodel.h
/usr/include/phonon4qt6/phonon/path.h
/usr/include/phonon4qt6/phonon/phonon_export.h
/usr/include/phonon4qt6/phonon/phonon_version.h
/usr/include/phonon4qt6/phonon/phonondefs.h
/usr/include/phonon4qt6/phonon/phononnamespace.h
/usr/include/phonon4qt6/phonon/platformplugin.h
/usr/include/phonon4qt6/phonon/pulsesupport.h
/usr/include/phonon4qt6/phonon/seekslider.h
/usr/include/phonon4qt6/phonon/streaminterface.h
/usr/include/phonon4qt6/phonon/videoplayer.h
/usr/include/phonon4qt6/phonon/videowidget.h
/usr/include/phonon4qt6/phonon/videowidgetinterface.h
/usr/include/phonon4qt6/phonon/volumefadereffect.h
/usr/include/phonon4qt6/phonon/volumefaderinterface.h
/usr/include/phonon4qt6/phonon/volumeslider.h
/usr/lib64/cmake/phonon4qt6/Phonon4Qt6Config.cmake
/usr/lib64/cmake/phonon4qt6/Phonon4Qt6ConfigVersion.cmake
/usr/lib64/cmake/phonon4qt6/Phonon4Qt6ExperimentalConfig.cmake
/usr/lib64/cmake/phonon4qt6/Phonon4Qt6ExperimentalConfigVersion.cmake
/usr/lib64/cmake/phonon4qt6/PhononExperimentalTargets-relwithdebinfo.cmake
/usr/lib64/cmake/phonon4qt6/PhononExperimentalTargets.cmake
/usr/lib64/cmake/phonon4qt6/PhononTargets-relwithdebinfo.cmake
/usr/lib64/cmake/phonon4qt6/PhononTargets.cmake
/usr/lib64/libphonon4qt6.so
/usr/lib64/libphonon4qt6experimental.so
/usr/lib64/pkgconfig/phonon4qt6.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libphonon4qt6.so.4
/usr/lib64/libphonon4qt6.so.4.12.0
/usr/lib64/libphonon4qt6experimental.so.4
/usr/lib64/libphonon4qt6experimental.so.4.12.0
/usr/lib64/qt6/plugins/designer/phonon4qt6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/phonon/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/phonon/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/phonon/ff3ed70db4739b3c6747c7f624fe2bad70802987
