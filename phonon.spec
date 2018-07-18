#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB92A5F04EC949121 (sitter@kde.org)
#
Name     : phonon
Version  : 4.10.1
Release  : 1
URL      : https://download.kde.org/stable/phonon/4.10.1/phonon-4.10.1.tar.xz
Source0  : https://download.kde.org/stable/phonon/4.10.1/phonon-4.10.1.tar.xz
Source99 : https://download.kde.org/stable/phonon/4.10.1/phonon-4.10.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: phonon-lib
Requires: phonon-data
Requires: phonon-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Designer)
BuildRequires : pulseaudio-dev
BuildRequires : qtdeclarative-dev

%description
No detailed description available

%package data
Summary: data components for the phonon package.
Group: Data

%description data
data components for the phonon package.


%package dev
Summary: dev components for the phonon package.
Group: Development
Requires: phonon-lib
Requires: phonon-data
Provides: phonon-devel

%description dev
dev components for the phonon package.


%package lib
Summary: lib components for the phonon package.
Group: Libraries
Requires: phonon-data
Requires: phonon-license

%description lib
lib components for the phonon package.


%package license
Summary: license components for the phonon package.
Group: Default

%description license
license components for the phonon package.


%prep
%setup -q -n phonon-4.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531882784
mkdir clr-build
pushd clr-build
%cmake .. -DPHONON_BUILD_PHONON4QT5=on
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1531882784
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/phonon
cp COPYING.LIB %{buildroot}/usr/share/doc/phonon/COPYING.LIB
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/phonon/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.Phonon4Qt5.AudioOutput.xml
/usr/share/phonon4qt5/buildsystem/COPYING-CMAKE-SCRIPTS
/usr/share/phonon4qt5/buildsystem/FindPackageHandleStandardArgs.cmake
/usr/share/phonon4qt5/buildsystem/FindPhononInternal.cmake
/usr/share/phonon4qt5/buildsystem/MacroEnsureVersion.cmake
/usr/share/phonon4qt5/buildsystem/MacroLogFeature.cmake
/usr/share/phonon4qt5/buildsystem/MacroOptionalFindPackage.cmake
/usr/share/phonon4qt5/buildsystem/MacroPushRequiredVars.cmake
/usr/share/phonon4qt5/buildsystem/PhononMacros.cmake
/usr/share/phonon4qt5/buildsystem/PhononQt4.cmake
/usr/share/phonon4qt5/buildsystem/PhononQt5.cmake
/usr/share/phonon4qt5/buildsystem/cmake_uninstall.cmake.in
/usr/share/qt5/mkspecs/modules/qt_phonon4qt5.pri

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libphonon4qt5.so.4
/usr/lib64/libphonon4qt5.so.4.10.1
/usr/lib64/libphonon4qt5experimental.so.4
/usr/lib64/libphonon4qt5experimental.so.4.10.1
/usr/lib64/qt5/plugins/designer/phononwidgets.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/phonon/COPYING.LIB
/usr/share/doc/phonon/cmake_COPYING-CMAKE-SCRIPTS
