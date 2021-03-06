#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB92A5F04EC949121 (sitter@kde.org)
#
Name     : phonon
Version  : 4.11.1
Release  : 10
URL      : https://download.kde.org/stable/phonon/4.11.1/phonon-4.11.1.tar.xz
Source0  : https://download.kde.org/stable/phonon/4.11.1/phonon-4.11.1.tar.xz
Source1  : https://download.kde.org/stable/phonon/4.11.1/phonon-4.11.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: phonon-bin = %{version}-%{release}
Requires: phonon-data = %{version}-%{release}
Requires: phonon-lib = %{version}-%{release}
Requires: phonon-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : extra-cmake-modules-data
BuildRequires : mesa-dev
BuildRequires : phonon-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : qtbase-dev
BuildRequires : qtdeclarative-dev
BuildRequires : qttools-dev

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
%setup -q -n phonon-4.11.1
cd %{_builddir}/phonon-4.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604707326
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DPHONON_BUILD_PHONON4QT5=on
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604707326
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/phonon
cp %{_builddir}/phonon-4.11.1/COPYING %{buildroot}/usr/share/package-licenses/phonon/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/phonon-4.11.1/COPYING.LIB %{buildroot}/usr/share/package-licenses/phonon/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/phonon-4.11.1/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/phonon/ff3ed70db4739b3c6747c7f624fe2bad70802987
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
/usr/share/locale/ca/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ca/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/cs/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/de/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/de/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/es/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/es/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/eu/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/fi/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/fr/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/id/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/id/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/it/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/it/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/ko/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/nl/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/nn/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/pl/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/pt/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sk/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/sr/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/sv/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/uk/LC_MESSAGES/phononsettings_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libphonon_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/phononsettings_qt.qm
/usr/share/phonon4qt5/buildsystem/FindPhononInternal.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/phonon4qt5/KDE/Phonon/AbstractAudioOutput
/usr/include/phonon4qt5/KDE/Phonon/AbstractMediaStream
/usr/include/phonon4qt5/KDE/Phonon/AbstractVideoOutput
/usr/include/phonon4qt5/KDE/Phonon/AddonInterface
/usr/include/phonon4qt5/KDE/Phonon/AudioDevice
/usr/include/phonon4qt5/KDE/Phonon/AudioDeviceEnumerator
/usr/include/phonon4qt5/KDE/Phonon/AudioOutput
/usr/include/phonon4qt5/KDE/Phonon/AudioOutputDevice
/usr/include/phonon4qt5/KDE/Phonon/AudioOutputDeviceModel
/usr/include/phonon4qt5/KDE/Phonon/AudioOutputInterface
/usr/include/phonon4qt5/KDE/Phonon/BackendCapabilities
/usr/include/phonon4qt5/KDE/Phonon/BackendInterface
/usr/include/phonon4qt5/KDE/Phonon/Effect
/usr/include/phonon4qt5/KDE/Phonon/EffectDescription
/usr/include/phonon4qt5/KDE/Phonon/EffectDescriptionModel
/usr/include/phonon4qt5/KDE/Phonon/EffectInterface
/usr/include/phonon4qt5/KDE/Phonon/EffectParameter
/usr/include/phonon4qt5/KDE/Phonon/EffectWidget
/usr/include/phonon4qt5/KDE/Phonon/Experimental/AbstractVideoDataOutput
/usr/include/phonon4qt5/KDE/Phonon/Experimental/AudioDataOutput
/usr/include/phonon4qt5/KDE/Phonon/Experimental/SnapshotInterface
/usr/include/phonon4qt5/KDE/Phonon/Experimental/VideoDataOutput
/usr/include/phonon4qt5/KDE/Phonon/Experimental/VideoDataOutputInterface
/usr/include/phonon4qt5/KDE/Phonon/Experimental/VideoFrame
/usr/include/phonon4qt5/KDE/Phonon/Experimental/VideoFrame2
/usr/include/phonon4qt5/KDE/Phonon/Experimental/Visualization
/usr/include/phonon4qt5/KDE/Phonon/Global
/usr/include/phonon4qt5/KDE/Phonon/MediaController
/usr/include/phonon4qt5/KDE/Phonon/MediaNode
/usr/include/phonon4qt5/KDE/Phonon/MediaObject
/usr/include/phonon4qt5/KDE/Phonon/MediaObjectInterface
/usr/include/phonon4qt5/KDE/Phonon/MediaSource
/usr/include/phonon4qt5/KDE/Phonon/ObjectDescription
/usr/include/phonon4qt5/KDE/Phonon/ObjectDescriptionModel
/usr/include/phonon4qt5/KDE/Phonon/Path
/usr/include/phonon4qt5/KDE/Phonon/PlatformPlugin
/usr/include/phonon4qt5/KDE/Phonon/SeekSlider
/usr/include/phonon4qt5/KDE/Phonon/StreamInterface
/usr/include/phonon4qt5/KDE/Phonon/VideoPlayer
/usr/include/phonon4qt5/KDE/Phonon/VideoWidget
/usr/include/phonon4qt5/KDE/Phonon/VideoWidgetInterface
/usr/include/phonon4qt5/KDE/Phonon/VolumeFaderEffect
/usr/include/phonon4qt5/KDE/Phonon/VolumeFaderInterface
/usr/include/phonon4qt5/KDE/Phonon/VolumeSlider
/usr/include/phonon4qt5/phonon/AbstractAudioOutput
/usr/include/phonon4qt5/phonon/AbstractMediaStream
/usr/include/phonon4qt5/phonon/AbstractVideoOutput
/usr/include/phonon4qt5/phonon/AddonInterface
/usr/include/phonon4qt5/phonon/AudioCaptureDevice
/usr/include/phonon4qt5/phonon/AudioCaptureDeviceModel
/usr/include/phonon4qt5/phonon/AudioChannelDescription
/usr/include/phonon4qt5/phonon/AudioChannelDescriptionModel
/usr/include/phonon4qt5/phonon/AudioDataOutput
/usr/include/phonon4qt5/phonon/AudioOutput
/usr/include/phonon4qt5/phonon/AudioOutputDevice
/usr/include/phonon4qt5/phonon/AudioOutputDeviceModel
/usr/include/phonon4qt5/phonon/AudioOutputInterface
/usr/include/phonon4qt5/phonon/AudioOutputInterface40
/usr/include/phonon4qt5/phonon/AudioOutputInterface42
/usr/include/phonon4qt5/phonon/AvCapture
/usr/include/phonon4qt5/phonon/BackendCapabilities
/usr/include/phonon4qt5/phonon/BackendInterface
/usr/include/phonon4qt5/phonon/Effect
/usr/include/phonon4qt5/phonon/EffectDescription
/usr/include/phonon4qt5/phonon/EffectDescriptionModel
/usr/include/phonon4qt5/phonon/EffectInterface
/usr/include/phonon4qt5/phonon/EffectParameter
/usr/include/phonon4qt5/phonon/EffectWidget
/usr/include/phonon4qt5/phonon/Global
/usr/include/phonon4qt5/phonon/GlobalDescriptionContainer
/usr/include/phonon4qt5/phonon/MediaController
/usr/include/phonon4qt5/phonon/MediaNode
/usr/include/phonon4qt5/phonon/MediaObject
/usr/include/phonon4qt5/phonon/MediaObjectInterface
/usr/include/phonon4qt5/phonon/MediaSource
/usr/include/phonon4qt5/phonon/Mrl
/usr/include/phonon4qt5/phonon/ObjectDescription
/usr/include/phonon4qt5/phonon/ObjectDescriptionData
/usr/include/phonon4qt5/phonon/ObjectDescriptionModel
/usr/include/phonon4qt5/phonon/ObjectDescriptionModelData
/usr/include/phonon4qt5/phonon/Path
/usr/include/phonon4qt5/phonon/PlatformPlugin
/usr/include/phonon4qt5/phonon/SeekSlider
/usr/include/phonon4qt5/phonon/StreamInterface
/usr/include/phonon4qt5/phonon/SubtitleDescription
/usr/include/phonon4qt5/phonon/SubtitleDescriptionModel
/usr/include/phonon4qt5/phonon/VideoCaptureDevice
/usr/include/phonon4qt5/phonon/VideoCaptureDeviceModel
/usr/include/phonon4qt5/phonon/VideoPlayer
/usr/include/phonon4qt5/phonon/VideoWidget
/usr/include/phonon4qt5/phonon/VideoWidgetInterface
/usr/include/phonon4qt5/phonon/VideoWidgetInterface44
/usr/include/phonon4qt5/phonon/VideoWidgetInterfaceLatest
/usr/include/phonon4qt5/phonon/VolumeFaderEffect
/usr/include/phonon4qt5/phonon/VolumeFaderInterface
/usr/include/phonon4qt5/phonon/VolumeSlider
/usr/include/phonon4qt5/phonon/abstractaudiooutput.h
/usr/include/phonon4qt5/phonon/abstractmediastream.h
/usr/include/phonon4qt5/phonon/abstractvideooutput.h
/usr/include/phonon4qt5/phonon/addoninterface.h
/usr/include/phonon4qt5/phonon/audiodataoutput.h
/usr/include/phonon4qt5/phonon/audiodataoutputinterface.h
/usr/include/phonon4qt5/phonon/audiooutput.h
/usr/include/phonon4qt5/phonon/audiooutputinterface.h
/usr/include/phonon4qt5/phonon/backendcapabilities.h
/usr/include/phonon4qt5/phonon/backendinterface.h
/usr/include/phonon4qt5/phonon/effect.h
/usr/include/phonon4qt5/phonon/effectinterface.h
/usr/include/phonon4qt5/phonon/effectparameter.h
/usr/include/phonon4qt5/phonon/effectwidget.h
/usr/include/phonon4qt5/phonon/experimental/abstractaudiodataoutput.h
/usr/include/phonon4qt5/phonon/experimental/abstractvideodataoutput.h
/usr/include/phonon4qt5/phonon/experimental/audiodataoutput.h
/usr/include/phonon4qt5/phonon/experimental/audiodataoutputinterface.h
/usr/include/phonon4qt5/phonon/experimental/audioformat.h
/usr/include/phonon4qt5/phonon/experimental/avcapture.h
/usr/include/phonon4qt5/phonon/experimental/avcaptureinterface.h
/usr/include/phonon4qt5/phonon/experimental/backendcapabilities.h
/usr/include/phonon4qt5/phonon/experimental/backendinterface.h
/usr/include/phonon4qt5/phonon/experimental/export.h
/usr/include/phonon4qt5/phonon/experimental/globalconfig.h
/usr/include/phonon4qt5/phonon/experimental/mediasource.h
/usr/include/phonon4qt5/phonon/experimental/objectdescription.h
/usr/include/phonon4qt5/phonon/experimental/packet.h
/usr/include/phonon4qt5/phonon/experimental/packetpool.h
/usr/include/phonon4qt5/phonon/experimental/phononnamespace.h
/usr/include/phonon4qt5/phonon/experimental/snapshotinterface.h
/usr/include/phonon4qt5/phonon/experimental/videodataoutput.h
/usr/include/phonon4qt5/phonon/experimental/videodataoutput2.h
/usr/include/phonon4qt5/phonon/experimental/videodataoutputinterface.h
/usr/include/phonon4qt5/phonon/experimental/videoframe.h
/usr/include/phonon4qt5/phonon/experimental/videoframe2.h
/usr/include/phonon4qt5/phonon/experimental/videowidget.h
/usr/include/phonon4qt5/phonon/experimental/visualization.h
/usr/include/phonon4qt5/phonon/globalconfig.h
/usr/include/phonon4qt5/phonon/globaldescriptioncontainer.h
/usr/include/phonon4qt5/phonon/mediacontroller.h
/usr/include/phonon4qt5/phonon/medianode.h
/usr/include/phonon4qt5/phonon/mediaobject.h
/usr/include/phonon4qt5/phonon/mediaobjectinterface.h
/usr/include/phonon4qt5/phonon/mediasource.h
/usr/include/phonon4qt5/phonon/mrl.h
/usr/include/phonon4qt5/phonon/objectdescription.h
/usr/include/phonon4qt5/phonon/objectdescriptionmodel.h
/usr/include/phonon4qt5/phonon/path.h
/usr/include/phonon4qt5/phonon/phonon_export.h
/usr/include/phonon4qt5/phonon/phonon_version.h
/usr/include/phonon4qt5/phonon/phonondefs.h
/usr/include/phonon4qt5/phonon/phononnamespace.h
/usr/include/phonon4qt5/phonon/platformplugin.h
/usr/include/phonon4qt5/phonon/pulsesupport.h
/usr/include/phonon4qt5/phonon/seekslider.h
/usr/include/phonon4qt5/phonon/streaminterface.h
/usr/include/phonon4qt5/phonon/videoplayer.h
/usr/include/phonon4qt5/phonon/videowidget.h
/usr/include/phonon4qt5/phonon/videowidgetinterface.h
/usr/include/phonon4qt5/phonon/volumefadereffect.h
/usr/include/phonon4qt5/phonon/volumefaderinterface.h
/usr/include/phonon4qt5/phonon/volumeslider.h
/usr/lib64/cmake/phonon4qt5/Phonon4Qt5Config.cmake
/usr/lib64/cmake/phonon4qt5/Phonon4Qt5ConfigVersion.cmake
/usr/lib64/cmake/phonon4qt5/Phonon4Qt5ExperimentalConfig.cmake
/usr/lib64/cmake/phonon4qt5/Phonon4Qt5ExperimentalConfigVersion.cmake
/usr/lib64/cmake/phonon4qt5/PhononExperimentalTargets-relwithdebinfo.cmake
/usr/lib64/cmake/phonon4qt5/PhononExperimentalTargets.cmake
/usr/lib64/cmake/phonon4qt5/PhononTargets-relwithdebinfo.cmake
/usr/lib64/cmake/phonon4qt5/PhononTargets.cmake
/usr/lib64/libphonon4qt5.so
/usr/lib64/libphonon4qt5experimental.so
/usr/lib64/pkgconfig/phonon4qt5.pc
/usr/lib64/qt5/mkspecs/modules/qt_phonon4qt5.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libphonon4qt5.so.4
/usr/lib64/libphonon4qt5.so.4.11.1
/usr/lib64/libphonon4qt5experimental.so.4
/usr/lib64/libphonon4qt5experimental.so.4.11.1
/usr/lib64/qt5/plugins/designer/phononwidgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/phonon/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/phonon/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/phonon/ff3ed70db4739b3c6747c7f624fe2bad70802987
