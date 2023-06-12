#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : fortune-mod
Version  : 3.20.0
Release  : 17
URL      : https://www.shlomifish.org/open-source/projects/fortune-mod/arcs/fortune-mod-3.20.0.tar.xz
Source0  : https://www.shlomifish.org/open-source/projects/fortune-mod/arcs/fortune-mod-3.20.0.tar.xz
Summary  : Ad hoc headers library for C
Group    : Development/Tools
License  : BSD-4-Clause
Requires: fortune-mod-bin = %{version}-%{release}
Requires: fortune-mod-data = %{version}-%{release}
Requires: fortune-mod-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(cmocka)
BuildRequires : recode-dev
BuildRequires : rinutils-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==================
This is fortune-mod. It now lives at:
* https://github.com/shlomif/fortune-mod

%package bin
Summary: bin components for the fortune-mod package.
Group: Binaries
Requires: fortune-mod-data = %{version}-%{release}

%description bin
bin components for the fortune-mod package.


%package data
Summary: data components for the fortune-mod package.
Group: Data

%description data
data components for the fortune-mod package.


%package man
Summary: man components for the fortune-mod package.
Group: Default

%description man
man components for the fortune-mod package.


%prep
%setup -q -n fortune-mod-3.20.0
cd %{_builddir}/fortune-mod-3.20.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686604946
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1686604946
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## install_append content
mv %{buildroot}/usr/games/fortune %{buildroot}/usr/bin/fortune
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fortune
/usr/bin/rot
/usr/bin/strfile
/usr/bin/unstr

%files data
%defattr(-,root,root,-)
/usr/share/games/fortunes/art
/usr/share/games/fortunes/art.dat
/usr/share/games/fortunes/art.u8
/usr/share/games/fortunes/ascii-art
/usr/share/games/fortunes/ascii-art.dat
/usr/share/games/fortunes/ascii-art.u8
/usr/share/games/fortunes/computers
/usr/share/games/fortunes/computers.dat
/usr/share/games/fortunes/computers.u8
/usr/share/games/fortunes/cookie
/usr/share/games/fortunes/cookie.dat
/usr/share/games/fortunes/cookie.u8
/usr/share/games/fortunes/debian
/usr/share/games/fortunes/debian.dat
/usr/share/games/fortunes/debian.u8
/usr/share/games/fortunes/definitions
/usr/share/games/fortunes/definitions.dat
/usr/share/games/fortunes/definitions.u8
/usr/share/games/fortunes/disclaimer
/usr/share/games/fortunes/disclaimer.dat
/usr/share/games/fortunes/disclaimer.u8
/usr/share/games/fortunes/drugs
/usr/share/games/fortunes/drugs.dat
/usr/share/games/fortunes/drugs.u8
/usr/share/games/fortunes/education
/usr/share/games/fortunes/education.dat
/usr/share/games/fortunes/education.u8
/usr/share/games/fortunes/ethnic
/usr/share/games/fortunes/ethnic.dat
/usr/share/games/fortunes/ethnic.u8
/usr/share/games/fortunes/food
/usr/share/games/fortunes/food.dat
/usr/share/games/fortunes/food.u8
/usr/share/games/fortunes/fortunes
/usr/share/games/fortunes/fortunes.dat
/usr/share/games/fortunes/fortunes.u8
/usr/share/games/fortunes/goedel
/usr/share/games/fortunes/goedel.dat
/usr/share/games/fortunes/goedel.u8
/usr/share/games/fortunes/humorists
/usr/share/games/fortunes/humorists.dat
/usr/share/games/fortunes/humorists.u8
/usr/share/games/fortunes/kids
/usr/share/games/fortunes/kids.dat
/usr/share/games/fortunes/kids.u8
/usr/share/games/fortunes/knghtbrd
/usr/share/games/fortunes/knghtbrd.dat
/usr/share/games/fortunes/knghtbrd.u8
/usr/share/games/fortunes/law
/usr/share/games/fortunes/law.dat
/usr/share/games/fortunes/law.u8
/usr/share/games/fortunes/linux
/usr/share/games/fortunes/linux.dat
/usr/share/games/fortunes/linux.u8
/usr/share/games/fortunes/literature
/usr/share/games/fortunes/literature.dat
/usr/share/games/fortunes/literature.u8
/usr/share/games/fortunes/love
/usr/share/games/fortunes/love.dat
/usr/share/games/fortunes/love.u8
/usr/share/games/fortunes/magic
/usr/share/games/fortunes/magic.dat
/usr/share/games/fortunes/magic.u8
/usr/share/games/fortunes/medicine
/usr/share/games/fortunes/medicine.dat
/usr/share/games/fortunes/medicine.u8
/usr/share/games/fortunes/men-women
/usr/share/games/fortunes/men-women.dat
/usr/share/games/fortunes/men-women.u8
/usr/share/games/fortunes/miscellaneous
/usr/share/games/fortunes/miscellaneous.dat
/usr/share/games/fortunes/miscellaneous.u8
/usr/share/games/fortunes/news
/usr/share/games/fortunes/news.dat
/usr/share/games/fortunes/news.u8
/usr/share/games/fortunes/off/art
/usr/share/games/fortunes/off/art.dat
/usr/share/games/fortunes/off/art.u8
/usr/share/games/fortunes/off/astrology
/usr/share/games/fortunes/off/astrology.dat
/usr/share/games/fortunes/off/astrology.u8
/usr/share/games/fortunes/off/atheism
/usr/share/games/fortunes/off/atheism.dat
/usr/share/games/fortunes/off/atheism.u8
/usr/share/games/fortunes/off/black-humor
/usr/share/games/fortunes/off/black-humor.dat
/usr/share/games/fortunes/off/black-humor.u8
/usr/share/games/fortunes/off/cookie
/usr/share/games/fortunes/off/cookie.dat
/usr/share/games/fortunes/off/cookie.u8
/usr/share/games/fortunes/off/debian
/usr/share/games/fortunes/off/debian.dat
/usr/share/games/fortunes/off/debian.u8
/usr/share/games/fortunes/off/definitions
/usr/share/games/fortunes/off/definitions.dat
/usr/share/games/fortunes/off/definitions.u8
/usr/share/games/fortunes/off/drugs
/usr/share/games/fortunes/off/drugs.dat
/usr/share/games/fortunes/off/drugs.u8
/usr/share/games/fortunes/off/ethnic
/usr/share/games/fortunes/off/ethnic.dat
/usr/share/games/fortunes/off/ethnic.u8
/usr/share/games/fortunes/off/fortunes
/usr/share/games/fortunes/off/fortunes.dat
/usr/share/games/fortunes/off/fortunes.u8
/usr/share/games/fortunes/off/hphobia
/usr/share/games/fortunes/off/hphobia.dat
/usr/share/games/fortunes/off/hphobia.u8
/usr/share/games/fortunes/off/knghtbrd
/usr/share/games/fortunes/off/knghtbrd.dat
/usr/share/games/fortunes/off/knghtbrd.u8
/usr/share/games/fortunes/off/limerick
/usr/share/games/fortunes/off/limerick.dat
/usr/share/games/fortunes/off/limerick.u8
/usr/share/games/fortunes/off/linux
/usr/share/games/fortunes/off/linux.dat
/usr/share/games/fortunes/off/linux.u8
/usr/share/games/fortunes/off/misandry
/usr/share/games/fortunes/off/misandry.dat
/usr/share/games/fortunes/off/misandry.u8
/usr/share/games/fortunes/off/miscellaneous
/usr/share/games/fortunes/off/miscellaneous.dat
/usr/share/games/fortunes/off/miscellaneous.u8
/usr/share/games/fortunes/off/misogyny
/usr/share/games/fortunes/off/misogyny.dat
/usr/share/games/fortunes/off/misogyny.u8
/usr/share/games/fortunes/off/politics
/usr/share/games/fortunes/off/politics.dat
/usr/share/games/fortunes/off/politics.u8
/usr/share/games/fortunes/off/privates
/usr/share/games/fortunes/off/privates.dat
/usr/share/games/fortunes/off/privates.u8
/usr/share/games/fortunes/off/racism
/usr/share/games/fortunes/off/racism.dat
/usr/share/games/fortunes/off/racism.u8
/usr/share/games/fortunes/off/religion
/usr/share/games/fortunes/off/religion.dat
/usr/share/games/fortunes/off/religion.u8
/usr/share/games/fortunes/off/riddles
/usr/share/games/fortunes/off/riddles.dat
/usr/share/games/fortunes/off/riddles.u8
/usr/share/games/fortunes/off/sex
/usr/share/games/fortunes/off/sex.dat
/usr/share/games/fortunes/off/sex.u8
/usr/share/games/fortunes/off/songs-poems
/usr/share/games/fortunes/off/songs-poems.dat
/usr/share/games/fortunes/off/songs-poems.u8
/usr/share/games/fortunes/off/vulgarity
/usr/share/games/fortunes/off/vulgarity.dat
/usr/share/games/fortunes/off/vulgarity.u8
/usr/share/games/fortunes/off/zippy
/usr/share/games/fortunes/off/zippy.dat
/usr/share/games/fortunes/off/zippy.u8
/usr/share/games/fortunes/paradoxum
/usr/share/games/fortunes/paradoxum.dat
/usr/share/games/fortunes/paradoxum.u8
/usr/share/games/fortunes/people
/usr/share/games/fortunes/people.dat
/usr/share/games/fortunes/people.u8
/usr/share/games/fortunes/perl
/usr/share/games/fortunes/perl.dat
/usr/share/games/fortunes/perl.u8
/usr/share/games/fortunes/pets
/usr/share/games/fortunes/pets.dat
/usr/share/games/fortunes/pets.u8
/usr/share/games/fortunes/platitudes
/usr/share/games/fortunes/platitudes.dat
/usr/share/games/fortunes/platitudes.u8
/usr/share/games/fortunes/politics
/usr/share/games/fortunes/politics.dat
/usr/share/games/fortunes/politics.u8
/usr/share/games/fortunes/pratchett
/usr/share/games/fortunes/pratchett.dat
/usr/share/games/fortunes/pratchett.u8
/usr/share/games/fortunes/riddles
/usr/share/games/fortunes/riddles.dat
/usr/share/games/fortunes/riddles.u8
/usr/share/games/fortunes/rules-of-acquisition
/usr/share/games/fortunes/rules-of-acquisition.dat
/usr/share/games/fortunes/rules-of-acquisition.u8
/usr/share/games/fortunes/science
/usr/share/games/fortunes/science.dat
/usr/share/games/fortunes/science.u8
/usr/share/games/fortunes/shlomif-fav
/usr/share/games/fortunes/shlomif-fav.dat
/usr/share/games/fortunes/shlomif-fav.u8
/usr/share/games/fortunes/songs-poems
/usr/share/games/fortunes/songs-poems.dat
/usr/share/games/fortunes/songs-poems.u8
/usr/share/games/fortunes/sports
/usr/share/games/fortunes/sports.dat
/usr/share/games/fortunes/sports.u8
/usr/share/games/fortunes/startrek
/usr/share/games/fortunes/startrek.dat
/usr/share/games/fortunes/startrek.u8
/usr/share/games/fortunes/tao
/usr/share/games/fortunes/tao.dat
/usr/share/games/fortunes/tao.u8
/usr/share/games/fortunes/translate-me
/usr/share/games/fortunes/translate-me.dat
/usr/share/games/fortunes/translate-me.u8
/usr/share/games/fortunes/wisdom
/usr/share/games/fortunes/wisdom.dat
/usr/share/games/fortunes/wisdom.u8
/usr/share/games/fortunes/work
/usr/share/games/fortunes/work.dat
/usr/share/games/fortunes/work.u8
/usr/share/games/fortunes/zippy
/usr/share/games/fortunes/zippy.dat
/usr/share/games/fortunes/zippy.u8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/strfile.1
/usr/share/man/man6/fortune.6
